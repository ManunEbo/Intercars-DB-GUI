from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker


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


class Op_Miscellaneous_ReceiptScreen(Screen):

    def __init__(self, **kwargs):
        super(Op_Miscellaneous_ReceiptScreen, self).__init__(**kwargs)
        self.Receipt_date = ""
        self.Receipt_time = ""
        self.VAT_Flag = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # Transaction date
    def Misc_Receipt_date_on_save(self, instance, value, date_range):
        self.Receipt_date = value
        self.ids.Misc_Receipt_date_lbl.text = "Receipt date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Receipt_date)

    # click cancel
    def Misc_Receipt_date_on_cancel(self, instance, value):
        pass

    def Misc_Receipt_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Misc_Receipt_date_on_save,
                         on_cancel=self.Misc_Receipt_date_on_cancel)
        date_dialog.open()

    # Get time
    def Receipt_get_time(self, instance, time):
        self.Receipt_time = time
        self.ids.Misc_receipt_time_id.text = "Receipt time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Receipt_time)

    # Cancel
    def Receipt_on_time_cancel(self, instance, time):
        pass

    def show_Misc_receipt_time_picker(self):
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
        time_dialog.bind(on_cancel=self.Receipt_on_time_cancel, time=self.Receipt_get_time)
        time_dialog.open()

    # Creating the VAT flag
    def VAT_Receip(self, value):
        self.VAT_Flag = value

    # Update icp.Op_Service
    def Submit_Miscellaneous_Receipt(self):

        sql_string1 = "set @Venue = '{0}';".format(self.ids.Venue_textf.text.strip())
        sql_string2 = "set @Vat_registration = '{0}';".format(
            self.ids.Vat_registration_textf.text.strip())
        sql_string3 = "set @Item = '{0}';".format(self.ids.Item_textf.text.strip())
        sql_string4 = "set @Price = {0};".format(self.ids.Price_textf.text.strip())
        sql_string5 = "set @Quantity = {0};".format(self.ids.Quantity_textf.text.strip())
        sql_string6 = "set @Total = {0};".format(self.ids.Total_textf.text.strip())
        sql_string7 = "set @Auth_Code = {0};".format(self.ids.Auth_code_textf.text.strip())
        sql_string8 = "set @Receipt_nbr = {0};".format(self.ids.Receipt_nbr_textf.text.strip())
        sql_string9 = "set @Receipt_date = '{0}';".format(self.Receipt_date)
        sql_string10 = "set @Receipt_time = '{0}';".format(self.Receipt_time)
        sql_string11 = "set @VAT_Flag = '{0}';".format(self.VAT_Flag.strip())

        if self.VAT_Flag == "Y":
            grss_Price = float(self.ids.Price_textf.text)*float(self.ids.Quantity_textf.text)
            Net_price = (float(self.ids.Price_textf.text)*float(self.ids.Quantity_textf.text))/1.2

            sql_string12 = "set @Gross_Price = {0};".format(grss_Price.strip())
            sql_string13 = "set @VAT_rate = 0.2;"
            sql_string14 = "set @Net = {0};".format(Net_price.strip())
            sql_string15 = "set @VAT = {0};".format(grss_Price - Net_price)

        sql_string16 = "call Op_misc_receipt_Call();"

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

        if self.VAT_Flag == "Y":
            print(sql_string12)
            print(sql_string13)
            print(sql_string14)
            print(sql_string15)

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

        if self.VAT_Flag == "Y":
            mycursor.execute(sql_string12)
            mycursor.execute(sql_string13)
            mycursor.execute(sql_string14)
            mycursor.execute(sql_string15)

        mycursor.execute(sql_string16)

        mydb.commit()
        mydb.close()

        self.manager.current = "operation_screen"
