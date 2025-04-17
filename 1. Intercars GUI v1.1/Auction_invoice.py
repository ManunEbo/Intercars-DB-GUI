from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker
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


class Auction_invoice(Screen):

    def __init__(self, **kwargs):
        super(Auction_invoice, self).__init__(**kwargs)
        self.V5c_id = ""
        self.Vehicle_reg = ""
        self.Auction_id = ""
        self.Auction_name = ""
        self.Vendor_id = ""
        self.Vendor_name = ""
        self.Invoice_Date = ""
        self.Date_first_Reg = ""
        self.MOT_Flag = ""
        self.MOT_Y_N = ""
        self.MOT_Expiry_date = ""
        self.Cash_Flag = ""
        self.Cash_Y_N = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # ******************************************************************************************
    # retrieving V5C_id to match the vehicles on the auction invoice
    sql_str = """ select a.V5C_id,
                    a.Model,
                    a.Reg_numb
                    from icp.V5C a
                    left join icp.Sale b
                    on a.V5C_id = b.V5C_id
                    left join icp.Auction_invoice c
                    on a.V5C_id = c.V5C_id
                    where b.V5C_id is null and c.V5C_id is null;"""

    mydata = pd.read_sql_query(sql_str, mydb)

    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    # Converting to a list
    Array_tup = list(map(tuple, Ar_shape))

    Auct_vehicle_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup]

    def Auct_selected_vehicle(self, value):
        x = value.split(',')
        self.V5c_id = x[0]
        self.Vehicle_reg = x[2]

    # ******************************************************************************************
    # creating a list of auction houses
    sql_str1 = """select a.Auction_id, b.Entity_Name
                from icp.Auction a left join
                icp.Entity b
                on a.Auction_id = b.Auction_id
                where b.Auction_id is not null;"""

    mydata1 = pd.read_sql_query(sql_str1, mydb)

    # converting the pandas dataframe into a numpy array
    num_data1 = mydata1.to_numpy()

    # Reshaping the data
    Ar_shape1 = num_data1.reshape(num_data1.shape)
    # Converting to a list
    Array_tup1 = list(map(tuple, Ar_shape1))

    Auct_Houses_list = ["{0}, {1}".format(x[0], x[1]) for x in Array_tup1]

    def Auct_house_select(self, value):
        x = value.split(',')
        self.Auction_id = x[0]
        self.Auction_name = x[1]

    # ******************************************************************************************
    # creating a list of Vendors

    sql_str2 = """select a.Vendor_id, b.Entity_Name
                    from icp.Vendor a left join
                    icp.Entity b
                    on a.Vendor_id = b.Vendor_id
                    where b.Vendor_id is not null;"""

    mydata2 = pd.read_sql_query(sql_str2, mydb)

    # converting the pandas dataframe into a numpy array
    num_data2 = mydata2.to_numpy()

    # Reshaping the data
    Ar_shape2 = num_data2.reshape(num_data2.shape)
    # Converting to a list
    Array_tup2 = list(map(tuple, Ar_shape2))

    Vendor_list = ["{0}, {1}".format(x[0], x[1]) for x in Array_tup2]

    def Vendor_select(self, value):
        x = value.split(',')
        self.Vendor_id = x[0]
        self.Vendor_name = x[1]

    # Invoice_Date
    def Invoice_Date_on_save(self, instance, value, date_range):
        self.Invoice_Date = value
        self.ids.Invoice_Date_id.text = "Invoice date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Invoice_Date)

    # click cancel
    def Invoice_Date_on_cancel(self, instance, value):
        pass

    def Invoice_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Invoice_Date_on_save, on_cancel=self.Invoice_Date_on_cancel)
        date_dialog.open()

    # Date first reg
    def Date_first_Reg_on_save(self, instance, value, date_range):
        self.Date_first_Reg = value
        self.ids.Date_first_Reg_id.text = "Date first reg:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Date_first_Reg)

    # click cancel
    def Date_first_Reg_on_cancel(self, instance, value):
        pass

    def Date_first_Reg_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Date_first_Reg_on_save,
                         on_cancel=self.Date_first_Reg_on_cancel)
        date_dialog.open()

    # MOT indicator, has vehicle got an MOT?
    yn = [(0, "No"),
          (1, "Yes")]

    MOT_YesNo = ["{0}, {1}".format(x[0], x[1]) for x in yn]

    def MOT_YesNo_select(self, value):
        x = value.split(',')
        self.MOT_Flag = x[0]
        self.MOT_Y_N = x[1]

    # MOT expiry date
    def MOT_Expiry_date_on_save(self, instance, value, date_range):
        self.MOT_Expiry_date = value
        self.ids.MOT_Expiry_date_id.text = "MOT expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.MOT_Expiry_date)

    # click cancel
    def MOT_Expiry_date_on_cancel(self, instance, value):
        pass

    def MOT_Expiry_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,
        )
        date_dialog.bind(on_save=self.MOT_Expiry_date_on_save,
                         on_cancel=self.MOT_Expiry_date_on_cancel)
        date_dialog.open()

    # Cash payment indicator, was the vehicle paid for using cash
    cash_yn = [(0, "No"),
               (1, "Yes")]

    Cash_YesNo = ["{0}, {1}".format(x[0], x[1]) for x in cash_yn]

    def Cash_YesNo_select(self, value):
        x = value.split(',')
        self.Cash_Flag = x[0]
        self.Cash_Y_N = x[1]

    def Submit_Auction_invoice(self):

        sql_string1 = "set @V5C_id = {0};".format(self.V5c_id.strip())
        sql_string2 = "set @Auction_id = {0};".format(self.Auction_id.strip())
        sql_string3 = "set @Vendor_id = {0};".format(self.Vendor_id.strip())
        sql_string4 = "set @Invoice_nbr = '{0}';".format(self.ids.Invoice_nbr_textf.text.strip())
        sql_string5 = "set @Invoice_Date = '{0}';".format(self.Invoice_Date)
        sql_string6 = "set @Reg_nbr = '{0}';".format(self.ids.Reg_nbr_textf.text.strip())
        sql_string7 = "set @Make = '{0}';".format(self.ids.Make_textf.text.strip())
        sql_string8 = "set @Model = '{0}';".format(self.ids.Model_textf.text.strip())
        sql_string9 = "set @Date_first_Reg = '{0}';".format(self.Date_first_Reg)
        sql_string10 = "set @MOT = '{0}';".format(self.MOT_Flag.strip())
        sql_string11 = "set @MOT_Expiry_date = '{0}';".format(self.MOT_Expiry_date)
        sql_string12 = "set @Mileage = '{0}';".format(self.ids.Mileage_textf.text.strip())
        sql_string13 = "set @Cash_Payment = '{0}';".format(self.Cash_Flag.strip())
        sql_string14 = "set @Price = {0};".format(self.ids.Price_textf.text.strip())
        sql_string15 = "set @Buyers_Fee = {0};".format(self.ids.Buyers_Fee_textf.text.strip())
        sql_string16 = "set @Assurance_Fee = {0};".format(self.ids.Assurance_Fee_textf.text.strip())
        sql_string17 = "set @Other_Fee = {0};".format(self.ids.Other_Fee_textf.text.strip())
        sql_string18 = "set @Storage_Fee = {0};".format(self.ids.Storage_Fee_textf.text.strip())
        sql_string19 = "set @Cash_Handling_fee = {0};".format(
            self.ids.Cash_Handling_fee_textf.text.strip())
        sql_string20 = "set @Auction_VAT = {0};".format(self.ids.Auction_VAT_textf.text.strip())
        sql_string21 = "set @Total = {0};".format(self.ids.Total_textf.text.strip())
        sql_string22 = "call icp_Auction_invoice_call();"

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
        print(sql_string18)
        print(sql_string19)
        print(sql_string20)
        print(sql_string21)

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
        mycursor.execute(sql_string19)
        mycursor.execute(sql_string20)
        mycursor.execute(sql_string21)
        mycursor.execute(sql_string22)

        mydb.commit()
        mydb.close()

        self.manager.current = "auction_menu_screen"
