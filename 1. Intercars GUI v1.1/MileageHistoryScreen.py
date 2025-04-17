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

class MileageHistoryScreen(Screen):
    def __init__(self, **kwargs):
        super(MileageHistoryScreen, self).__init__(**kwargs)
        self.V5c_id = ""
        self.Mileage_Date = ""

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
    v5c_list_MHist = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in custom_list]

    def selected_id_MHist(self, value):
        x = value.split(',')
        self.V5c_id = x[0]

    # Mileage date
    def Mileage_Date_on_save(self, instance, value, date_range):
        self.Mileage_Date = value
        self.ids.Mileage_Date_lbl.text = "Mileage date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Mileage_Date)

    # click cancel
    def Mileage_Date_on_cancel(self, instance, value):
        pass

    def Mileage_Date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2000,
            max_year=2050,)
        date_dialog.bind(on_save=self.Mileage_Date_on_save, on_cancel=self.Mileage_Date_on_cancel)
        date_dialog.open()

    def Submit_Mileage(self):

        sql_string1 = "set @V5C_id ={0};".format(self.V5c_id.strip())
        sql_string2 = "set @Vehicle_Reg_MOT_Date ='{0}';".format(
            self.ids.Reg_MOT_Date_textf.text.strip())
        sql_string3 = "set @Source  ='{0}';".format(self.ids.Source_textf.text.strip())
        sql_string4 = "set @Mileage ={0};".format(self.ids.Mileage_textf.text)
        sql_string5 = "set @Date = '{0}';".format(self.Mileage_Date)
        sql_string6 = "call icp_Mileage_History_call();"

        mycursor = mydb.cursor()
        mycursor.execute(sql_string1)
        mycursor.execute(sql_string2)
        mycursor.execute(sql_string3)
        mycursor.execute(sql_string4)
        mycursor.execute(sql_string5)
        mycursor.execute(sql_string6)

        mydb.commit()
        mydb.close()

        self.manager.current = "vehiclescreen"
