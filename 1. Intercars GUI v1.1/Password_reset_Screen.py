from kivy.uix.screenmanager import Screen, ScreenManager
import pandas as pd
import numpy as np

import os
DB_USER_1 = os.environ['DB_USER_1']
DB_PASSWORD_1 = os.environ['DB_PASSWORD_1']

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user=DB_USER_1,
    password=DB_PASSWORD_1,
    database="icp",
    auth_plugin='mysql_native_password'
)


class Password_reset_Screen(Screen):

    def __init__(self, **kwargs):
        super(Password_reset_Screen, self).__init__(**kwargs)
        self.Staff_id = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    sql_str = """ select b.Staff_id,a.Fname,a.Lname from icp.Names a left join icp.Staff b on a.Staff_id = b.Staff_id where a.Staff_id is Not null; """

    mydata = pd.read_sql_query(sql_str, mydb)

    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    # Converting to a list
    Array_tup = list(map(tuple, Ar_shape))

    staff_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup]

    def selected_staff(self, value):
        x = value.split(',')

        self.Staff_id = x[0]

    def Reset_password(self):

        # Checking if the password given matchs the current password on the account
        sql_pwd_check_string = """ SELECT cast(AES_DECRYPT(UNHEX(Passwd), '{0}', iv)as char) from icp.Staff where Staff_id={1};""".format(
            self.ids.Previous_passwd_textf.text, self.Staff_id)
        print(sql_pwd_check_string)
        PwdCheck = mydb.cursor()
        PwdCheck.execute(sql_pwd_check_string)
        Check = PwdCheck.fetchone()
        if Check[0] == None:
            self.ids.Previous_passwd_lbl.text = "Previous Password\n[color=#D50000][b]Incorrect password[/b][/color]"
        else:
            print(Check[0])
            # Checking to see if the new password and it's confirmation match
            if self.ids.New_passwd_textf.text != self.ids.Confirm_new_passwd_textf.text:
                self.ids.Confirm_new_passwd_lbl.text = "Confirm new password\n[color=#D50000][b]Mismatch[/b][/color]"

            else:
                sql_string1 = "set @random_bytes = RANDOM_BYTES(16);"
                sql_string2 = "set @pssw1 = '{0}';".format(self.ids.New_passwd_textf.text.strip())
                sql_string3 = "set @key1 = '{0}';".format(
                    self.ids.New_secret_key_textf.text.strip())
                sql_string4 = "set @Staff_id = {0}".format(self.Staff_id.strip())
                sql_string5 = "set @pwd = HEX(AES_ENCRYPT(@key1,@pssw1,@random_bytes));"
                sql_string6 = "update icp.Staff set Passwd = @pwd, iv = @random_bytes where Staff_id = @Staff_id;"

                print(sql_string1)
                print(sql_string2)
                print(sql_string3)
                print(sql_string4)
                print(sql_string5)
                print(sql_string6)

                mycursor = mydb.cursor()
                mycursor.execute(sql_string1)
                mycursor.execute(sql_string2)
                mycursor.execute(sql_string3)
                mycursor.execute(sql_string4)
                mycursor.execute(sql_string5)
                mycursor.execute(sql_string6)

                mydb.commit()
                mydb.close()

                self.manager.current = "staff_screen"

    def clear(self):
        self.ids.Staff_select_spin_id.text = "Select"
        self.ids.Previous_passwd_textf.text = ""
        self.ids.New_passwd_textf.text = ""
        self.ids.Confirm_new_passwd_textf.text = ""
        self.ids.New_secret_key_textf.text = ""
        self.ids.Previous_passwd_lbl.text = "Previous Password"
