from kivy.uix.screenmanager import Screen, ScreenManager


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


class MOT_GarageScreen(Screen):
    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def Submit_MOT_garage(self):

        sql_string1 = "set @Entity_Name = '{0}';".format(self.ids.Entity_Name_textf.text.strip())
        sql_string2 = "set @VAT_Registration_Number = '{0}';".format(
            self.ids.VAT_Reg_Number_textf.text.strip())
        sql_string3 = "set @Fname = '{0}';".format(self.ids.Fname_textf.text.strip())
        sql_string4 = "set @Mname = '{0}';".format(self.ids.Mname_textf.text.strip())
        sql_string5 = "set @Lname = '{0}';".format(self.ids.Lname_textf.text.strip())
        sql_string6 = "set @Addr1 = '{0}';".format(self.ids.Addr1_textf.text.strip())
        sql_string7 = "set @Addr2 = '{0}';".format(self.ids.Addr2_textf.text.strip())
        sql_string8 = "set @Addr3 = '{0}';".format(self.ids.Addr3_textf.text.strip())
        sql_string9 = "set @Addr4 = '{0}';".format(self.ids.Addr4_textf.text.strip())
        sql_string10 = "set @Addr5 = '{0}';".format(self.ids.Addr5_textf.text.strip())
        sql_string11 = "set @Addr6 = '{0}';".format(self.ids.Addr6_textf.text.strip())
        sql_string12 = "set @email = '{0}';".format(self.ids.email_textf.text.strip())
        sql_string13 = "set @Tel = '{0}';".format(self.ids.Tel_textf.text.strip())
        sql_string14 = "insert into icp.MOT_Garage() values();"

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

        mydb.commit()
        mydb.close()

        self.manager.current = "garage_screen"
