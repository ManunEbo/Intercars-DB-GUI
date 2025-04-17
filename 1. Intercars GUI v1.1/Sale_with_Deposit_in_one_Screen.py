from kivy.uix.screenmanager import Screen, ScreenManager
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


class Sale_with_Deposit_in_one_Screen(Screen):

    def __init__(self, **kwargs):
        super(Sale_with_Deposit_in_one_Screen, self).__init__(**kwargs)
        self.Split_payment = "No"
        self.Payment_method = ""
        self.Transfer_Reference = ""
        self.Card_nbr = 0
        self.Debit_type = ""
        self.Expiry_date = "null"
        self.Start_date = "null"
        self.Sale_date = ""
        self.Deposit_Date = ""
        self.Trans_Date = ""
        self.Trans_time = ""
        self.Auth_code = 0
        self.Amount = ""
        self.Receipt_Nbr = 0
        self.Staff_id = 1

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # Retrieving live deposits
    sql_deposit_retr = """select
		a.Fname,
        b.Deposit_date
        from icp.Deposit b left join
        	 icp.Names a
             on a.Customer_id = b.Customer_id
             left join icp.Sale c
             on b.V5C_id = c.V5C_id left join
             icp.V5C d
             on b.V5C_id = d.V5C_id
        	 where c.Sale_Date is null and b.Deposit_Date > (current_date() - 21);"""

    mydata = pd.read_sql_query(sql_deposit_retr, mydb)

    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    # Converting to a list
    Dep_list = list(map(tuple, Ar_shape))

    Live_Deposit_list = ["{0}, {1}".format(x[0], x[1]) for x in Dep_list]

    # Retrieving selected live deposit
    def SD1_selected_Live_Deposit(self, value):
        x = value.split(',')
        self.Deposit_Date = x[1]

    # Payment method
    def SD1_dep_sal_option_choice(self, value):
        self.Payment_method = value

    # Debit type
    def SD1_Debit_type(self, value):
        self.Debit_type = value

    # Card Expiry Date
    def SD1_card_Exp_on_save(self, instance, value, date_range):
        self.Expiry_date = value
        self.ids.SD1_Card_Expiry_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Expiry_date)

    # click cancel
    def SD1_card_Exp_on_cancel(self, instance, value):
        pass

    def SD1_card_Exp_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD1_card_Exp_on_save, on_cancel=self.SD1_card_Exp_on_cancel)
        date_dialog.open()

    # Card Start Date
    def SD1_card_start_on_save(self, instance, value, date_range):
        self.Start_date = value
        self.ids.SD1_Card_Start_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Start_date)

    # click cancel
    def SD1_card_start_on_cancel(self, instance, value):
        pass

    def SD1_card_start_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD1_card_start_on_save,
                         on_cancel=self.SD1_card_start_on_cancel)
        date_dialog.open()

    # Transaction Date
    # ****** Note: The deposit date is retrieved with the live deposits above ******
    def SD1_transaction_on_save(self, instance, value, date_range):
        self.Trans_Date = value
        self.Sale_date = value
        self.ids.SD1_transaction_Date_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_Date)

    # click cancel
    def SD1_transaction_on_cancel(self, instance, value):
        pass

    def SD1_transaction_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD1_transaction_on_save,
                         on_cancel=self.SD1_transaction_on_cancel)
        date_dialog.open()

    # Get time
    def SD1_get_time(self, instance, time):
        self.Trans_time = time
        self.ids.SD1_transaction_time_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_time)

    # Cancel
    def SD1_on_time_cancel(self, instance, time):
        pass

    def show_SD1_time_picker(self):
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
        time_dialog.bind(on_cancel=self.SD1_on_time_cancel, time=self.SD1_get_time)
        time_dialog.open()

    # submit to database
    def SD1_submit(self):

        # Programme flows for variables to ensure that blank values are handled correctly
        # in preparation for database insert

        if self.ids.SD1_transfer_ref_textf.text is None:
            self.Transfer_Reference = ""
        else:
            self.Transfer_Reference = self.ids.SD1_transfer_ref_textf.text

        if self.ids.SD1_card_nbr_textf.text is None:
            self.Card_nbr = ""
        else:
            self.Card_nbr = self.ids.SD1_card_nbr_textf.text

        if self.ids.SD1_auth_textf.text is None:
            self.Auth_code = ""
        else:
            self.Auth_code = self.ids.SD1_auth_textf.text

        self.Amount = self.ids.SD1_Amount_textf.text

        if self.ids.SD1_Receipt_nbr_textf.text is None:
            self.Receipt_Nbr = ""
        else:
            self.Receipt_Nbr = self.ids.SD1_Receipt_nbr_textf.text

        # ***************** Variables extracted from other screens *****************
        v5_x = self.manager.get_screen('deposit_or_sale').ids.veh_select_spin_id.text.split(',')
        v5c_id = v5_x[0]

        sql_string1 = "set @Split_pay ='{0}';".format(self.Split_payment.strip())
        sql_string2 = "set @V5C_ID = {0};".format(v5c_id.strip())
        sql_string3 = "set @Payment_method ='{0}';".format(self.Payment_method.strip())
        sql_string4 = "set @Transfer_Reference = '{0}';".format(self.Transfer_Reference.strip())
        sql_string5 = "set @Card_nbr = {0};".format(self.Card_nbr.strip())
        sql_string6 = "set @Debit_Type ='{0}';".format(self.Debit_type.strip())
        sql_string7 = "set @Exp_Date = '{0}';".format(self.Expiry_date)
        sql_string8 = "set @Start_Date ='{0}';".format(self.Start_date)
        sql_string9 = "set @Trans_Date = '{0}';".format(self.Trans_Date)
        sql_string10 = "set @Trans_time = '{0}';".format(self.Trans_time)
        sql_string11 = "set @Auth_code = {0};".format(self.Auth_code.strip())
        sql_string12 = "set @Amount = {0};".format(self.Amount.strip())
        sql_string13 = "set @Sale_Amount = {0};".format(self.Amount.strip())
        sql_string14 = "set @Receipt_Nbr = {0};".format(self.Receipt_Nbr.strip())
        sql_string15 = "set @Sale_date = '{0}';".format(self.Sale_date)
        sql_string16 = "set @Deposit_Date = '{0}';".format(self.Deposit_Date)
        sql_string17 = "set @Staff_id = {0};".format(self.Staff_id.strip())
        sql_string18 = "set @Split_Amount = 0;"
        sql_string19 = "call Customer_Insert_call();"

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
        mydb.commit()
        mydb.close()

        self.manager.current = "customerscreen"
