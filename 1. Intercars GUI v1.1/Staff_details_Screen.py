from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker

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


class Staff_details_Screen(Screen):

    def __init__(self, **kwargs):
        super(Staff_details_Screen, self).__init__(**kwargs)
        self.DOB = ""
        self.Password = ""
        self.Age_Group = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # DOB
    def Staff_DOB_on_save(self, instance, value, date_range):
        self.DOB = value
        self.ids.Staff_DOB_lbl.text = "DOB:\n[color=#76FF03][b]{0}[/b][/color]".format(self.DOB)

    # click cancel
    def Staff_DOB_on_cancel(self, instance, value):
        pass

    def Staff_DOB_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1960,
            max_year=2030,)
        date_dialog.bind(on_save=self.Staff_DOB_on_save, on_cancel=self.Staff_DOB_on_cancel)
        date_dialog.open()

    # Validate Password
    def verify(self):
        if self.ids.Passwd_textf.text == self.ids.Passwd_confirm_textf.text:
            self.Password = self.ids.Passwd_textf.text
        else:
            self.ids.Passwd_confirm_lbl.text = "Confirm Password\n[color=#D50000][b]Mismatch[/b][/color]"

    def staff_agegroup_clicked(self, value):
        self.Age_Group = value

    def Submit_Staff(self):

        # ***************** Variables extracted from other screens *****************

        Fname = self.manager.get_screen('staff_screen').ids.Fname_textf.text

        if self.manager.get_screen('staff_screen').ids.Mname_textf == "":
            Mname = ""
        else:
            Mname = self.manager.get_screen('staff_screen').ids.Mname_textf.text

        Lname = self.manager.get_screen('staff_screen').ids.Lname_textf.text

        Passwd1 = '{0}'.format(self.manager.get_screen('staff_screen').ids.Passwd_textf.text)

        Secrete_code = '{0}'.format(self.manager.get_screen(
            'staff_screen').ids.Secrete_code_textf.text)

        sql_string1 = "set @Fname = '{0}';".format(Fname.strip())
        sql_string2 = "set @Mname = '{0}';".format(Mname.strip())
        sql_string3 = "set @Lname = '{0}';".format(Lname.strip())
        sql_string4 = 'set @DOB = "{0}";'.format(self.DOB)

        sql_string5 = "set @random_bytes = RANDOM_BYTES(16);"
        sql_string6 = "set @p_wd = '{0}';".format(Passwd1.strip())
        sql_string7 = "set @s_code = '{0}';".format(Secrete_code.strip())
        sql_string8 = "set @Passwd = HEX(AES_ENCRYPT(@s_code,@p_wd ,@random_bytes));"

        sql_string9 = "set @Addr1 = '{0}';".format(self.ids.Addr1_textf.text.strip())
        sql_string10 = "set @Addr2 = '{0}';".format(self.ids.Addr2_textf.text.strip())
        sql_string11 = "set @Addr3 = '{0}';".format(self.ids.Addr3_textf.text.strip())
        sql_string12 = "set @Addr4 = '{0}';".format(self.ids.Addr4_textf.text.strip())
        sql_string13 = "set @Addr5 = '{0}';".format(self.ids.Addr5_textf.text.strip())
        sql_string14 = "set @Addr6 = '{0}';".format(self.ids.Addr6_textf.text.strip())
        sql_string15 = "set @email = '{0}';".format(self.ids.email_textf.text.strip())
        sql_string16 = "set @tel = '{0}';".format(self.ids.Tel_textf.text.strip())
        sql_string17 = "set @Age_Group = '{0}';".format(self.Age_Group.strip())
        sql_string18 = "call Staff_Insert_call();"

        print(sql_string1)
        print(sql_string2)
        print(sql_string3)
        print(sql_string4)
        print(sql_string5)
        print(sql_string6)
        print(sql_string7)
        print(sql_string8)
        print(sql_string9)
        print(sql_string10)
        print(sql_string11)
        print(sql_string12)
        print(sql_string13)
        print(sql_string14)
        print(sql_string15)
        print(sql_string16)
        print(sql_string17)

        mycursor = mydb.cursor()
        mycursor.execute(sql_string1)
        mycursor.execute(sql_string2)
        mycursor.execute(sql_string3)
        mycursor.execute(sql_string4)
        mycursor.execute(sql_string5)
        mycursor.execute(sql_string6)
        mycursor.execute(sql_string7)
        mycursor.execute(sql_string8)
        mycursor.execute(sql_string9)
        mycursor.execute(sql_string10)
        mycursor.execute(sql_string11)
        mycursor.execute(sql_string12)
        mycursor.execute(sql_string13)
        mycursor.execute(sql_string14)
        mycursor.execute(sql_string15)
        mycursor.execute(sql_string16)
        mycursor.execute(sql_string17)
        mycursor.execute(sql_string18)
        mydb.commit()
        mydb.close()

        self.manager.current = "menuscreen"
