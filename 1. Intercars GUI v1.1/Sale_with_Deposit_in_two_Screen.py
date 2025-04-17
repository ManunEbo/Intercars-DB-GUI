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


class Sale_with_Deposit_in_two_Screen(Screen):

    def __init__(self, **kwargs):
        super(Sale_with_Deposit_in_two_Screen, self).__init__(**kwargs)
        self.Split_payment = "Yes"
        self.Nbr_splits = 2

        self.Payment_method1 = ""
        self.Transfer_Reference1 = ""
        self.Card_nbr1 = ""
        self.Debit_Type1 = ""
        self.Expiry_Date_1 = ""
        self.Start_Date1 = ""
        self.Trans_Date_1 = ""
        self.Trans_time_1 = ""
        self.Auth_code1 = ""
        self.Amount1 = 0
        self.Receipt_Nbr1 = ""

        # Second payment
        self.Payment_method2 = ""
        self.Transfer_Reference2 = ""
        self.Card_nbr2 = ""
        self.Debit_Type2 = ""
        self.Expiry_Date_2 = ""
        self.Start_Date2 = ""
        self.Trans_Date_2 = ""
        self.Trans_time_2 = ""
        self.Auth_code2 = ""
        self.Amount2 = 0
        self.Receipt_Nbr2 = ""

        self.Sale_date = ""
        self.Deposit_Date = ""
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
             on b.V5C_id = c.V5C_id
        	 where c.Sale_Date is null and b.Deposit_Date > (current_date() - 21);"""

    mydata = pd.read_sql_query(sql_deposit_retr, mydb)

    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    # Converting to a list
    Dep_list = list(map(tuple, Ar_shape))

    SD2_Live_Deposit_list = ["{0}, {1}".format(x[0], x[1]) for x in Dep_list]

    def SD2_selected_Live_Deposit(self, value):
        x = value.split(',')
        self.Deposit_Date = x[1]

    # **********************************************************************************
    #               Payment method 1
    # **********************************************************************************

    def SD2_1_dep_sal_option_choice(self, value):
        self.Payment_method1 = value

    def SD2_Debit_type1(self, value):
        self.Debit_Type1 = value

    # D2 Card Expiry Date 1
    def SD2_card_Exp_1_on_save(self, instance, value, date_range):
        self.Expiry_Date_1 = value
        self.ids.SD2_Card_Expiry_1_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Expiry_Date_1)

    # click cancel
    def SD2_card_Exp_1_on_cancel(self, instance, value):
        pass

    # Sale card expiry date
    def SD2_card_Exp_date_picker1(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD2_card_Exp_1_on_save,
                         on_cancel=self.SD2_card_Exp_1_on_cancel)
        date_dialog.open()

    # Card Start Date
    def SD2_card_start_1_on_save(self, instance, value, date_range):
        self.Start_Date1 = value
        self.ids.SD2_Card_Start_1_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Start_Date1)

    # click cancel
    def SD2_card_start_1_on_cancel(self, instance, value):
        pass

    def SD2_card_start_date_1_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD2_card_start_1_on_save,
                         on_cancel=self.SD2_card_start_1_on_cancel)
        date_dialog.open()

    # Transaction  Date
    # Note Deposit date is retrieved in the live deposits above
    def SD2_transaction_1_on_save(self, instance, value, date_range):
        self.Trans_Date_1 = value
        self.Sale_date = value
        self.ids.SD2_transaction_Date_1_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_Date_1)

    # click cancel
    def SD2_transaction_1_on_cancel(self, instance, value):
        pass

    def SD2_transaction_date_1_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD2_transaction_1_on_save,
                         on_cancel=self.SD2_transaction_1_on_cancel)
        date_dialog.open()

    # Get time
    def SD2_get_time_1(self, instance, time):
        self.Trans_time_1 = time
        self.ids.SD2_transaction_time_1_id.text = "Transaction Time 1:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_time_1)

    # Cancel
    def SD2_on_time_1_cancel(self, instance, time):
        pass

    def SD2_show_Trans_1_time_picker1(self):
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
        time_dialog.bind(on_cancel=self.SD2_on_time_1_cancel, time=self.SD2_get_time_1)
        time_dialog.open()

    # **********************************************************************************
    #               Second Payment
    # **********************************************************************************

    def SD2_dep_sal_option_choice2(self, value):
        self.Payment_method2 = value

    def SD2_Debit_type2(self, value):
        self.Debit_Type2 = value

    # D2 Card Expiry Date 1
    def SD2_card_Exp_2_on_save(self, instance, value, date_range):
        self.Expiry_Date_2 = value
        self.ids.SD2_Card_Expiry_2_id.text = "Card Expiry Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Expiry_Date_2)

    # click cancel
    def SD2_card_Exp_2_on_cancel(self, instance, value):
        pass

    # Deposit card expiry date
    def SD2_card_Exp_date_picker2(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD2_card_Exp_2_on_save,
                         on_cancel=self.SD2_card_Exp_2_on_cancel)
        date_dialog.open()

    # Card Start Date
    def SD2_card_start_2_on_save(self, instance, value, date_range):
        self.Start_Date2 = value
        self.ids.SD2_Card_Start_2_id.text = "Card Start Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Start_Date2)

    # click cancel
    def SD2_card_start_2_on_cancel(self, instance, value):
        pass

    def SD2_Card_start_date_2_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD2_card_start_2_on_save,
                         on_cancel=self.SD2_card_start_2_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    def SD2_transaction_2_on_save(self, instance, value, date_range):
        self.Trans_Date_2 = value
        self.ids.SD2_transaction_Date_2_id.text = "Transaction Date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_Date_2)

    # click cancel
    def SD2_transaction_2_on_cancel(self, instance, value):
        pass

    def SD2_transaction_date_2_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.SD2_transaction_2_on_save,
                         on_cancel=self.SD2_transaction_2_on_cancel)
        date_dialog.open()

    # Get time
    def SD2_get_time_2(self, instance, time):
        self.Trans_time_2 = time
        self.ids.SD2_transaction_time_2_id.text = "Transaction Time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_time_2)

    # Cancel
    def SD2_on_time_2_cancel(self, instance, time):
        pass

    def SD2_show_time_picker2(self):
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
        time_dialog.bind(on_cancel=self.SD2_on_time_2_cancel, time=self.SD2_get_time_2)
        time_dialog.open()

    # **********************************************************************************
    #               submit to database
    # **********************************************************************************

    def SD2_submit(self):

        # **********************************************************************************
        #               First Payment
        # **********************************************************************************
        if self.ids.SD2_transfer_ref_1_textf.text is None:
            self.Transfer_Reference1 = ""
        else:
            self.Transfer_Reference1 = self.ids.SD2_transfer_ref_1_textf.text

        if self.ids.SD2_card_nbr_1_textf.text == "":
            self.Card_nbr1 = ""
        else:
            self.Card_nbr1 = self.ids.SD2_card_nbr_1_textf.text

        if self.ids.SD2_auth_1_textf.text == "":
            self.Auth_code1 = ""
        else:
            self.Auth_code1 = self.ids.SD2_auth_1_textf.text

        if self.ids.SD2_Amount_1_textf.text is None:
            self.Amount1 = ""
        else:
            self.Amount1 = self.ids.SD2_Amount_1_textf.text

        if self.ids.SD2_Receipt_nbr_1_textf.text == "":
            self.Receipt_Nbr1 = ""
        else:
            self.Receipt_Nbr1 = self.ids.SD2_Receipt_nbr_1_textf.text

        # **********************************************************************************
        #               Second Payment
        # **********************************************************************************

        if self.ids.SD2_transfer_ref_2_textf.text is None:
            self.Transfer_Reference2 = ""
        else:
            self.Transfer_Reference2 = self.ids.SD2_transfer_ref_2_textf.text

        if self.ids.SD2_card_nbr_2_textf.text == "":
            self.Card_nbr2 = ""
        else:
            self.Card_nbr2 = self.ids.SD2_card_nbr_2_textf.text

        if self.ids.SD2_auth_2_textf.text == "":
            self.Auth_code2 = ""
        else:
            self.Auth_code2 = self.ids.SD2_auth_2_textf.text

        if self.ids.SD2_Amount_2_textf.text is None:
            self.Amount2 = ""
        else:
            self.Amount2 = self.ids.SD2_Amount_2_textf.text

        if self.ids.SD2_Receipt_nbr_2_textf.text == "":
            self.Receipt_Nbr2 = ""
        else:
            self.Receipt_Nbr2 = self.ids.SD2_Receipt_nbr_2_textf.text

        # **********************************************************************************
        #               Variables extracted from other screens
        # **********************************************************************************

        v5_x = self.manager.get_screen('deposit_or_sale').ids.veh_select_spin_id.text.split(',')
        v5c_id = v5_x[0]

        # **********************************************************************************
        #               SQL strings
        # **********************************************************************************

        sql_string1 = "set @Split_pay ='{0}';".format(self.Split_payment.strip())
        sql_string2 = "set @Nbr_splits = {0};".format(self.Nbr_splits.strip())
        sql_string3 = "set @V5C_ID = {0};".format(v5c_id.strip())

        # First payment
        sql_string4 = "set @Payment_method1 ='{0}';".format(self.Payment_method1.strip())
        sql_string5 = "set @Transfer_Reference1 = '{0}';".format(self.Transfer_Reference1.strip())
        sql_string6 = "set @Card_Nbr1= {0};".format(self.Card_nbr1.strip())
        sql_string7 = "set @Debit_Type1 ='{0}';".format(self.Debit_Type1.strip())
        sql_string8 = "set @Exp_Date1 = '{0}';".format(self.Expiry_Date_1)
        sql_string9 = "set @Start_Date1 ='{0}';".format(self.Start_Date1)
        sql_string10 = "set @Trans_Date1 = '{0}';".format(self.Trans_Date_1)
        sql_string11 = "set @Trans_time1 = '{0}';".format(self.Trans_time_1)
        sql_string12 = "set @Auth_code1 = {0};".format(self.Auth_code1.strip())
        sql_string13 = "set @Split_Amount1 = {0};".format(self.Amount1.strip())
        sql_string14 = "set @Receipt_Nbr1 = {0};".format(self.Receipt_Nbr1.strip())

        # Second payment
        sql_string15 = "set @Payment_method2 = '{0}';".format(self.Payment_method2.strip())
        sql_string16 = "set @Transfer_Reference2 = '{0}';".format(self.Transfer_Reference2.strip())
        sql_string17 = "set @Card_Nbr2 = {0};".format(self.Card_nbr2.strip())
        sql_string18 = "set @Debit_Type2 ='{0}';".format(self.Debit_Type2.strip())
        sql_string19 = "set @Exp_Date2 = '{0}';".format(self.Expiry_Date_2)
        sql_string20 = "set @Start_Date2 ='{0}';".format(self.Start_Date2)
        sql_string21 = "set @Trans_Date2 = '{0}';".format(self.Trans_Date_2)
        sql_string22 = "set @Trans_time2 = '{0}';".format(self.Trans_time_2)
        sql_string23 = "set @Auth_code2 = {0};".format(self.Auth_code2.strip())
        sql_string24 = "set @Split_Amount2 = {0};".format(self.Amount2.strip())
        sql_string25 = "set @Receipt_Nbr2 = {0};".format(self.Receipt_Nbr2.strip())

        sql_string26 = "set @Sale_Amount = @Split_Amount1 + @Split_Amount2;"
        sql_string27 = "set @Deposit_Date = '{0}';".format(self.Deposit_Date)
        sql_string28 = "set @Sale_date = '{0}';".format(self.Sale_date)
        sql_string29 = "set @Staff_id = {0};".format(self.Staff_id.strip())
        sql_string30 = "call Customer_Insert_call();"

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
        print(sql_string22)
        print(sql_string23)
        print(sql_string24)
        print(sql_string25)
        print(sql_string26)
        print(sql_string27)
        print(sql_string28)
        print(sql_string29)

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
        mycursor.execute(sql_string23)
        mycursor.execute(sql_string24)
        mycursor.execute(sql_string25)
        mycursor.execute(sql_string26)
        mycursor.execute(sql_string27)
        mycursor.execute(sql_string28)
        mycursor.execute(sql_string29)
        mycursor.execute(sql_string30)

        mydb.commit()
        mydb.close()

        self.manager.current = "customerscreen"
