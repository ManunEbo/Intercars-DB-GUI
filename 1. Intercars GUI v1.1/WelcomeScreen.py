from kivy.uix.screenmanager import Screen
import pandas as pd
import numpy as np
import mysql.connector
import sql_import

class WelcomeScreen(Screen):

    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        self.Staff_id = ""

    def logger(self):
        # database connection
        cnn = sql_import.db_connection(self)
        # Checking if the password given matchs the current password on the account
        sql_pwd_check_string = """ SELECT cast(AES_DECRYPT(UNHEX(Passwd), '{0}', iv)as char) from icp.Staff where Staff_id=(select Staff_id from icp.Names where Fname='{1}');""".format(
            self.ids.password.text, self.ids.user.text)
        PwdCheck = cnn.cursor()
        PwdCheck.execute(sql_pwd_check_string)
        Check = PwdCheck.fetchone()
        cnn.close()
        if Check[0] == None:
            self.ids.welcome_label.text = "{0}\n[color=#D50000][b][size=16]Invalid username or password[/size][/b][/color]".format(
                self.ids.user.text)

        else:
            sql_str = "select b.Staff_id from icp.Names a left join icp.Staff b on a.Staff_id = b.Staff_id where a.Fname = '{0}' and a.Staff_id is not null;".format(
                self.ids.user.text)

            # database connection
            cnn = sql_import.db_connection(self)

            mydata = pd.read_sql_query(sql_str, cnn)

            # converting the pandas dataframe into a numpy array
            num_data = mydata.to_numpy()

            # Reshaping the data
            Ar_shape = num_data.reshape(num_data.shape)
            # Converting to a list
            Array_tup = list(map(tuple, Ar_shape))

            Staff = ["{0}".format(x[0]) for x in Array_tup]
            self.Staff_id = Staff[0]
            self.manager.current = 'menuscreen'
            return
            cnn.close()

    def clear(self):
        self.ids.welcome_label.text = "Welcome"
        self.ids.user.text = ""
        self.ids.password.text = ""
