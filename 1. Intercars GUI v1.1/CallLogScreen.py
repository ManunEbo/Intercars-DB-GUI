from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
import pandas as pd
import numpy as np
import mysql.connector

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


class CallLogScreen(Screen):
    def __init__(self, **kwargs):
        super(CallLogScreen, self).__init__(**kwargs)
        self.V5C_id = ""
        self.Vehicle_of_interest = ""
        self.Customer_sex = ""
        self.Date_of_call = ""
        self.Time_of_Call = ""
        self.Deposit_flag = ""

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
    Vehicle_log_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in custom_list]

    def selected_vehicle(self, value):
        x = value.split(',')
        self.V5C_id = x[0]
        self.Vehicle_of_interest = "{0} {1}".format(x[1], x[2])

    def Customer_sex_log(self, value):
        self.Customer_sex = value

    # Date of call
    def Date_of_call_on_save(self, instance, value, date_range):
        self.Date_of_call = value
        self.ids.Date_of_call_lbl.text = "Date of call:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Date_of_call)

    # click cancel
    def Date_of_call_on_cancel(self, instance, value):
        pass

    def Date_of_call_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Date_of_call_on_save, on_cancel=self.Date_of_call_on_cancel)
        date_dialog.open()

    # Time of call
    def get_time_of_call(self, instance, time):
        self.Time_of_Call = time
        self.ids.Time_of_call_id.text = "Time of call:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Time_of_Call)
    # Cancel

    def time_of_call_cancel(self, instance, time):
        pass

    def show_time_of_call_picker(self):
        time_dialog = MDTimePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            text_color="#76FF03",
            text_toolbar_color="#000000",
            selector_color="#000000",
            text_current_color="#76FF03",
            text_button_color="#000000",
            input_field_background_color="#000000",
            input_field_text_color="#616161",
        )
        time_dialog.bind(on_cancel=self.time_of_call_cancel, time=self.get_time_of_call)
        time_dialog.open()

    def Deposit_flag_extract(self, value):
        self.Deposit_flag = value

    def Submit_Call_log(self):

        sql_string1 = "set @Name ='{0}';".format(self.ids.Name_textf.text.strip())
        sql_string2 = "set @Customer_sex ='{0}';".format(self.Customer_sex.strip())
        sql_string3 = "set @Tel ={0};".format(self.ids.Tel_textf.text.strip())
        sql_string4 = "set @City_or_village ='{0}';".format(
            self.ids.City_or_village_textf.text.strip().upper())
        sql_string5 = "set @Vehicle_of_interest ='{0}';".format(self.Vehicle_of_interest.strip())
        sql_string6 = "set @V5C_id ='{0}';".format(self.V5C_id.strip())
        sql_string7 = "set @Date_of_call ='{0}';".format(self.Date_of_call)
        sql_string8 = "set @Time_of_Call ='{0}';".format(self.Time_of_Call)
        sql_string9 = "set @Deposit_flag = {0};".format(self.Deposit_flag.strip())
        sql_string10 = "call Op_call_Log_call();"

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

        mydb.commit()
        mydb.close()

        self.manager.current = "vehiclescreen"
