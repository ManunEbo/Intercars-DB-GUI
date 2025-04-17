from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker
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


class MOTRefusalScreen(Screen):
    def __init__(self, **kwargs):
        super(MOTRefusalScreen, self).__init__(**kwargs)
        self.V5c_id = ""
        self.Test_Date = ""
        self.Ref_Reason1 = ""
        self.Ref_Reason2 = ""
        self.Ref_Reason3 = ""
        self.Ref_Reason4 = ""
        self.Ref_Reason5 = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    sql_str = """ select a.V5C_id,
    a.Model,
    a.Reg_numb
    from icp.V5C a
    left join icp.Sale b
    on a.V5C_id = b.V5C_id
    where b.V5C_id is null; """

    mydata = pd.read_sql_query(sql_str, mydb)

    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    # Converting to a list
    Array_tup = list(map(tuple, Ar_shape))

    custom_list = Array_tup
    v5c_list_MR = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in custom_list]

    def selected_id_mr(self, value):
        x = value.split(',')
        self.V5c_id = x[0]

    # Test date
    def Test_Date_r_on_save(self, instance, value, date_range):
        self.Test_Date = value
        self.ids.Test_Date_r_lbl.text = "Test date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Test_Date)

    # click cancel
    def Test_Date_r_on_cancel(self, instance, value):
        pass

    def Test_Date_r_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2000,
            max_year=2050,)
        date_dialog.bind(on_save=self.Test_Date_r_on_save, on_cancel=self.Test_Date_r_on_cancel)
        date_dialog.open()

    def Submit_MOTRefusal(self):
        sql_string1 = "set @V5C_ID ={0};".format(self.V5c_id)
        sql_string2 = "set @Vehicle_Reg_MOT_Date ='{0}';".format(self.ids.Reg_MOT_Date_r_textf.text)
        sql_string3 = "set @Test_comp = '{0}';".format(self.ids.Test_comp_textf.text)
        sql_string4 = "set @Test_Addr = '{0}';".format(self.ids.Test_Addr_r_textf.text)
        sql_string5 = "set @Test_Date = '{0}';".format(Test_Date)

        if self.ids.Ref_Reason1_textf.text is None:
            self.Ref_Reason1 = ""
        else:
            self.Ref_Reason1 = self.ids.Ref_Reason1_textf.text
        sql_string6 = "set @Ref_Reason1 ='{0}';".format(self.Ref_Reason1.strip())

        if self.ids.Ref_Reason2_textf.text is None:
            self.Ref_Reason2 = ""
        else:
            self.Ref_Reason2 = self.ids.Ref_Reason2_textf.text
        sql_string7 = "set @Ref_Reason2 ='{0}';".format(self.Ref_Reason2.strip())

        if self.ids.Ref_Reason3_textf.text is None:
            self.Ref_Reason3 = ""
        else:
            self.Ref_Reason3 = self.ids.Ref_Reason3_textf.text
        sql_string8 = "set @Ref_Reason3 ='{0}';".format(self.Ref_Reason3.strip())

        if self.ids.Ref_Reason4_textf.text is None:
            self.Ref_Reason4 = ""
        else:
            self.Ref_Reason4 = self.ids.Ref_Reason4_textf.text
        sql_string9 = "set @Ref_Reason4 ='{0}';".format(self.Ref_Reason4.strip())

        if self.ids.Ref_Reason5_textf.text is None:
            self.Ref_Reason5 = ""
        else:
            self.Ref_Reason5 = self.ids.Ref_Reason5_textf.text
        sql_string10 = "set @Ref_Reason5 ='{0}';".format(self.Ref_Reason5.strip())

        sql_string11 = "call icp_MOT_Refusal_call();"

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

        mydb.commit()
        mydb.close()

        self.manager.current = "vehiclescreen"
