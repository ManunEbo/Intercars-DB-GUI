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


class Deposit_in_two_Screen(Screen):

    def __init__(self, **kwargs):
        super(Deposit_in_two_Screen, self).__init__(**kwargs)
        self.Split_payment = "Yes"
        self.Nbr_splits = 2

        self.Deposit_Payment_method1 = ""
        self.Deposit_Transfer_Reference1 = ""
        self.Deposit_Card_nbr1 = ""
        self.Deposit_Debit_Type1 = ""
        self.Deposit_Expiry_Date_1 = ""
        self.Deposit_Start_Date1 = ""
        self.Deposit_Trans_Date_1 = ""
        self.Deposit_Trans_time_1 = ""
        self.Deposit_Auth_code1 = ""
        self.Deposit_Amount1 = 0
        self.Deposit_Receipt_Nbr1 = ""

        # Second payment
        self.Deposit_Payment_method2 = ""
        self.Deposit_Transfer_Reference2 = ""
        self.Deposit_Card_nbr2 = ""
        self.Deposit_Debit_Type2 = ""
        self.Deposit_Expiry_Date_2 = ""
        self.Deposit_Start_Date2 = ""
        self.Deposit_Trans_Date_2 = ""
        self.Deposit_Trans_time_2 = ""
        self.Deposit_Auth_code2 = ""
        self.Deposit_Amount2 = 0
        self.Deposit_Receipt_Nbr2 = ""

        self.Deposit_date = "null"
        self.Staff_id = 1

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # **********************************************************************************
    # Payment method 1
    # **********************************************************************************
    def D2_1_dep_sal_option_choice(self, value):
        self.Deposit_Payment_method1 = value

    def D2_Deposit_Debit_type1(self, value):
        self.Deposit_Debit_Type1 = value

    # D2 Card Expiry Date 1
    # click ok
    def D2_Deposit_card_Exp_1_on_save(self, instance, value, date_range):
        self.Deposit_Expiry_Date_1 = value
        self.ids.D2_Card_Expiry_1_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Expiry_Date_1)

    # click cancel
    def D2_Deposit_card_Exp_1_on_cancel(self, instance, value):
        pass

    # Deposit card expiry date
    def D2_Deposit_card_Exp_date_picker1(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.D2_Deposit_card_Exp_1_on_save,
                         on_cancel=self.D2_Deposit_card_Exp_1_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def D2_Deposit_card_start_1_on_save(self, instance, value, date_range):
        self.Deposit_Start_Date1 = value
        self.ids.D2_Card_Start_1_id.text = "Card start date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Start_Date1)

    # click cancel
    def D2_Deposit_card_start_1_on_cancel(self, instance, value):
        pass

    # try also passing a value for variable to the on_save below
    def D2_Deposit_card_start_date_1_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.D2_Deposit_card_start_1_on_save,
                         on_cancel=self.D2_Deposit_card_start_1_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def D2_Deposit_transaction_1_on_save(self, instance, value, date_range):
        self.Deposit_Trans_Date_1 = value
        self.Deposit_date = value
        self.ids.D2_Deposit_transaction_Date_1_id.text = "Deposit date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Trans_Date_1)

    # click cancel
    def D2_Deposit_transaction_1_on_cancel(self, instance, value):
        pass

    # try also passing a value for variable to the on_save below
    def D2_Deposit_transaction_date_1_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.D2_Deposit_transaction_1_on_save,
                         on_cancel=self.D2_Deposit_transaction_1_on_cancel)
        date_dialog.open()

    # Get time
    def D2_Deposit_get_time_1(self, instance, time):
        self.Deposit_Trans_time_1 = time
        self.ids.D2_Deposit_transaction_time_1_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Trans_time_1)
    # Cancel

    def D2_Deposit_on_time_1_cancel(self, instance, time):
        pass

    def D2_show_Deposit_time_picker1(self):
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
        time_dialog.bind(on_cancel=self.D2_Deposit_on_time_1_cancel,
                         time=self.D2_Deposit_get_time_1)
        time_dialog.open()

    # **********************************************************************************
    #               Second Payment
    # **********************************************************************************
    def D2_dep_sal_option_choice2(self, value):
        self.Deposit_Payment_method2 = value

    def D2_Deposit_Debit_type2(self, value):
        self.Deposit_Debit_Type2 = value

    # D2 Card Expiry Date 1
    def D2_Deposit_card_Exp_2_on_save(self, instance, value, date_range):
        self.Deposit_Expiry_Date_2 = value
        self.ids.D2_Card_Expiry_2_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Expiry_Date_2)

    # click cancel
    def D2_Deposit_card_Exp_2_on_cancel(self, instance, value):
        pass

    # Deposit card expiry date
    def D2_Deposit_card_Exp_date_picker2(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.D2_Deposit_card_Exp_2_on_save,
                         on_cancel=self.D2_Deposit_card_Exp_2_on_cancel)
        date_dialog.open()

    # Card Start Date
    # click ok
    def D2_Deposit_card_start_2_on_save(self, instance, value, date_range):
        self.Deposit_Start_Date2 = value
        self.ids.D2_Card_Start_2_id.text = "Card start date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Start_Date2)

    # click cancel
    def D2_Deposit_card_start_2_on_cancel(self, instance, value):
        pass

    def D2_Deposit_card_start_date_2_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.D2_Deposit_card_start_2_on_save,
                         on_cancel=self.D2_Deposit_card_start_2_on_cancel)
        date_dialog.open()

    # Deposit/transaction  Date
    # click ok
    def D2_Deposit_transaction_2_on_save(self, instance, value, date_range):
        self.Deposit_Trans_Date_2 = value
        self.ids.D2_Deposit_transaction_Date_2_id.text = "Deposit date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Trans_Date_2)

    # click cancel
    def D2_Deposit_transaction_2_on_cancel(self, instance, value):
        pass

    # try also passing a value for variable to the on_save below
    def D2_Deposit_transaction_date_2_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.D2_Deposit_transaction_2_on_save,
                         on_cancel=self.D2_Deposit_transaction_2_on_cancel)
        date_dialog.open()

    # Get time
    def D2_Deposit_get_time_2(self, instance, time):
        self.Deposit_Trans_time_2 = time
        self.ids.D2_Deposit_transaction_time_2_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Deposit_Trans_time_2)
    # Cancel

    def D2_Deposit_on_time_2_cancel(self, instance, time):
        pass

    def D2_show_Deposit_time_picker2(self):
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
        time_dialog.bind(on_cancel=self.D2_Deposit_on_time_2_cancel,
                         time=self.D2_Deposit_get_time_2)
        time_dialog.open()

    # **********************************************************************************
    #               submit to database
    # **********************************************************************************
    def D2_Deposit_submit(self):
        # pass the input values into variables

        # First payment
        self.Deposit_Payment_method1 = self.ids.D2_payment_method_1_spin_id.text

        if self.ids.D2_transfer_ref_1_textf.text is None:
            self.Deposit_Transfer_Reference1 = ""
        else:
            self.Deposit_Transfer_Reference1 = self.ids.D2_transfer_ref_1_textf.text

        if self.ids.D2_card_nbr_1_textf == "":
            self.Deposit_Card_nbr1 = ""
        else:
            self.Deposit_Card_nbr1 = self.ids.D2_card_nbr_1_textf.text

        if self.ids.D2_Debit_type_1_spin_id.text is None:
            self.Deposit_Debit_Type1 = ""
        else:
            self.Deposit_Debit_Type1 = self.ids.D2_Debit_type_1_spin_id.text

        if self.ids.D2_Deposit_auth_1_textf == "":
            self.Deposit_Auth_code1 = ""
        else:
            self.Deposit_Auth_code1 = self.ids.D2_Deposit_auth_1_textf.text

        if self.ids.D2_Deposit_Amount_1_textf.text is None:
            self.Deposit_Amount1 = ""
        else:
            self.Deposit_Amount1 = self.ids.D2_Deposit_Amount_1_textf.text

        if self.ids.D2_Deposit_Receipt_nbr_1_textf == "":
            self.Deposit_Receipt_Nbr1 = ""
        else:
            self.Deposit_Receipt_Nbr1 = self.ids.D2_Deposit_Receipt_nbr_1_textf.text

        # ***************************************************************************

        # Second payment
        self.Deposit_Payment_method2 = self.ids.D2_payment_method_2_spin_id.text

        if self.ids.D2_transfer_ref_1_textf.text is None:
            self.Deposit_Transfer_Reference2 = ""
        else:
            self.Deposit_Transfer_Reference2 = self.ids.D2_transfer_ref_2_textf.text

        if self.ids.D2_card_nbr_2_textf.text is None:
            self.Deposit_Card_nbr2 = ""
        else:
            self.Deposit_Card_nbr2 = self.ids.D2_card_nbr_2_textf.text

        if self.ids.D2_Debit_type_2_spin_id.text is None:
            self.Deposit_Debit_Type2 = ""
        else:
            self.Deposit_Debit_Type2 = self.ids.D2_Debit_type_2_spin_id.text

        if self.ids.D2_Deposit_auth_2_textf.text is None:
            self.Deposit_Auth_code2 = ""
        else:
            self.Deposit_Auth_code2 = self.ids.D2_Deposit_auth_2_textf.text

        if self.ids.D2_Deposit_Amount_2_textf.text is None:
            self.Deposit_Amount2 = ""
        else:
            self.Deposit_Amount2 = self.ids.D2_Deposit_Amount_2_textf.text

        if self.ids.D2_Deposit_Receipt_nbr_2_textf.text is None:
            self.Deposit_Receipt_Nbr2 = ""
        else:
            self.Deposit_Receipt_Nbr2 = self.ids.D2_Deposit_Receipt_nbr_2_textf.text

        # Variables extracted from other screens
        v5_x = self.manager.get_screen('deposit_or_sale').ids.veh_select_spin_id.text.split(',')
        v5c_id = v5_x[0]

        Fname = self.manager.get_screen('customerscreen').ids.firstname_textf.text

        if self.manager.get_screen('customerscreen').ids.middlename_textf == "":
            Mname = ""
        else:
            Mname = self.manager.get_screen('customerscreen').ids.middlename_textf.text

        Lname = self.manager.get_screen('customerscreen').ids.lastname_textf.text

        if self.manager.get_screen('customerscreen').Customer_DOB == "":
            DOB = "null"
        else:
            DOB = self.manager.get_screen('customerscreen').Customer_DOB

        # age group must not be blank
        Age_Group = self.manager.get_screen('customerscreen').ids.agegroup_spnr.text
        Address1 = self.manager.get_screen('cust_address').ids.house_num_textf.text
        Address2 = self.manager.get_screen('cust_address').ids.street_textf.text
        Address3 = self.manager.get_screen('cust_address').ids.city_town_textf.text
        Address4 = self.manager.get_screen('cust_address').ids.county_textf.text
        Address5 = self.manager.get_screen('cust_address').ids.country_textf.text
        Address6 = self.manager.get_screen('cust_address').ids.postcode_textf.text
        email = self.manager.get_screen('cust_address').ids.email_textf.text
        Tel = self.manager.get_screen('cust_address').ids.tel_textf.text

        # SQL strings
        sql_string1 = "set @Split_pay ='{0}';".format(self.Split_payment.strip())
        sql_string2 = "set @Nbr_splits = {0};".format(self.Nbr_splits.strip())
        sql_string3 = "set @V5C_ID = {0};".format(v5c_id.strip())

        # First payment
        sql_string4 = "set @Payment_method1 ='{0}';".format(self.Deposit_Payment_method1.strip())
        sql_string5 = "set @Transfer_Reference1 = '{0}';".format(
            self.Deposit_Transfer_Reference1.strip())
        sql_string6 = "set @Card_Nbr1= {0};".format(self.Deposit_Card_nbr1.strip())
        sql_string7 = "set @Debit_Type1 ='{0}';".format(self.Deposit_Debit_Type1.strip())
        sql_string8 = "set @Exp_Date1 = '{0}';".format(self.Deposit_Expiry_Date_1)
        sql_string9 = "set @Start_Date1 ='{0}';".format(self.Deposit_Start_Date1)
        sql_string10 = "set @Trans_Date1 = '{0}';".format(self.Deposit_Trans_Date_1)
        sql_string11 = "set @Trans_time1 = '{0}';".format(self.Deposit_Trans_time_1)
        sql_string12 = "set @Auth_code1 = {0};".format(self.Deposit_Auth_code1.strip())
        sql_string13 = "set @Split_Amount1 = {0};".format(self.Deposit_Amount1.strip())
        sql_string14 = "set @Receipt_Nbr1 = {0};".format(self.Deposit_Receipt_Nbr1.strip())

        # Second payment
        sql_string15 = "set @Payment_method2 = '{0}';".format(self.Deposit_Payment_method2.strip())
        sql_string16 = "set @Transfer_Reference2 = '{0}';".format(
            self.Deposit_Transfer_Reference2.strip())
        sql_string17 = "set @Card_Nbr2 = {0};".format(self.Deposit_Card_nbr2.strip())
        sql_string18 = "set @Debit_Type2 ='{0}';".format(self.Deposit_Debit_Type2.strip())
        sql_string19 = "set @Exp_Date2 = '{0}';".format(self.Deposit_Expiry_Date_2)
        sql_string20 = "set @Start_Date2 ='{0}';".format(self.Deposit_Start_Date2)
        sql_string21 = "set @Trans_Date2 = '{0}';".format(self.Deposit_Trans_Date_2)
        sql_string22 = "set @Trans_time2 = '{0}';".format(self.Deposit_Trans_time_2)
        sql_string23 = "set @Auth_code2 = {0};".format(self.Deposit_Auth_code2.strip())
        sql_string24 = "set @Split_Amount2 = {0};".format(self.Deposit_Amount2.strip())
        sql_string25 = "set @Receipt_Nbr2 = {0};".format(self.Deposit_Receipt_Nbr2.strip())

        sql_string26 = "set @Deposit_Amount = @Split_Amount1 + @Split_Amount2;"

        # Customer details
        sql_string27 = 'Set @Fname= "{0}";'.format(Fname.strip())
        sql_string28 = 'Set @Mname= "{0}";'.format(Mname.strip())
        sql_string29 = 'Set @Lname= "{0}";'.format(Lname.strip())
        sql_string30 = "Set @DOB= '{0}';".format(DOB)
        sql_string31 = "set @Age_Group= '{0}';".format(Age_Group.strip())
        sql_string32 = "Set @Address1= '{0}';".format(Address1.strip())
        sql_string33 = 'Set @Address2= "{0}";'.format(Address2.strip())
        sql_string34 = "Set @Address3= '{0}';".format(Address3.strip())
        sql_string35 = "Set @Address4= '{0}';".format(Address4.strip())
        sql_string36 = "Set @Address5= '{0}';".format(Address5.strip())
        sql_string37 = "Set @Address6 = '{0}';".format(Address6.strip())
        sql_string38 = "Set @email = '{0}';".format(email.strip())
        sql_string39 = "Set @Tel = '{0}';".format(Tel.strip())
        sql_string40 = 'set @Sale_date= "";'
        sql_string41 = "set @Deposit_Date = '{0}';".format(self.Deposit_date)
        sql_string42 = "set @Staff_id = {0};".format(self.Staff_id.strip())
        sql_string43 = "call Customer_Insert_call();"

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
        print(sql_string30)
        print(sql_string31)
        print(sql_string32)
        print(sql_string33)
        print(sql_string34)
        print(sql_string35)
        print(sql_string36)
        print(sql_string37)
        print(sql_string38)
        print(sql_string39)
        print(sql_string40)
        print(sql_string41)
        print(sql_string42)

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
        mycursor.execute(sql_string31)
        mycursor.execute(sql_string32)
        mycursor.execute(sql_string33)
        mycursor.execute(sql_string34)
        mycursor.execute(sql_string35)
        mycursor.execute(sql_string36)
        mycursor.execute(sql_string37)
        mycursor.execute(sql_string38)
        mycursor.execute(sql_string39)
        mycursor.execute(sql_string40)
        mycursor.execute(sql_string41)
        mycursor.execute(sql_string42)
        mycursor.execute(sql_string43)
        mydb.commit()
        mydb.close()

        self.manager.current = "customerscreen"
