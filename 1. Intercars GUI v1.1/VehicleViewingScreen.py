from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
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

class VehicleViewingScreen(Screen):

    def __init__(self, **kwargs):
        super(VehicleViewingScreen, self).__init__(**kwargs)
        self.V5C_id = ""
        self.Vehicle_of_interest = ""
        self.Customer_Age_Bracket = ""
        self.Customer_sex = ""
        self.Viewing_date = ""
        self.Viewing_time = ""
        self.Deposit_Flag = ""
        self.Sale_Flag = ""

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
    Vehicle_v_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in custom_list]

    def selected_vehicle_v(self, value):
        x = value.split(',')
        self.V5C_id = x[0]
        self.Vehicle_of_interest = "{0} {1}".format(x[1], x[2])

    def Viewing_agegroup(self, value):
        self.Customer_Age_Bracket = value

    def Customer_sex_v(self, value):
        self.Customer_sex = value

    # Viewing date
    def Viewing_date_on_save(self, instance, value, date_range):
        self.Viewing_date = value
        self.ids.Viewing_date_lbl.text = "Viewing date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Viewing_date)

    # click cancel
    def Viewing_date_on_cancel(self, instance, value):
        pass

    def Viewing_date_picker(self):
        # set minimum year to 2014
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Viewing_date_on_save, on_cancel=self.Viewing_date_on_cancel)
        date_dialog.open()

    # Time of call
    def get_viewing_time(self, instance, time):

        self.Viewing_time = time
        self.ids.Viewing_time_id.text = "Viewing time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Viewing_time)
    # Cancel

    def viewing_time_cancel(self, instance, time):
        pass

    def show_viewing_time_picker(self):
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
        time_dialog.bind(on_cancel=self.viewing_time_cancel, time=self.get_viewing_time)
        time_dialog.open()

    def Deposit_Flag_v(self, value):
        self.Deposit_Flag = value

    def Sale_Flag_v(self, value):
        self.Sale_Flag = value

    def Submit_Viewing(self):
        sql_string1 = "set @Vehicle_of_interest ='{0}';".format(self.Vehicle_of_interest.strip())
        sql_string2 = "set @V5C_id ={0};".format(self.V5C_id.strip())
        sql_string3 = "set @Nbr_Vehicles_viewed = {0};".format(
            self.ids.Nbr_Vehicles_viewed_textf.text.strip())
        sql_string4 = "set @Customer_Age_Bracket ='{0}';".format(self.Customer_Age_Bracket.strip())
        sql_string5 = "set @Customer_sex ='{0}';".format(self.Customer_sex.strip())
        sql_string6 = "set @City_or_village = '{0}';".format(
            self.ids.City_or_village_textf.text.strip().upper())
        sql_string7 = "set @Viewing_date ='{0}';".format(self.Viewing_date)
        sql_string8 = "set @Viewing_time = '{0}';".format(self.Viewing_time)
        sql_string9 = "set @Deposit_Flag = '{0}';".format(self.Deposit_Flag.strip())
        sql_string10 = "set @Sale_Flag ='{0}';".format(self.Sale_Flag.strip())
        sql_string11 = "call Op_vehicle_viewing_call();"

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
