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


class Deposit_in_one_Screen(Screen):
    """
    Variables dictionary:
        1: Payment_method
        2: Debit_type
        3: Expiry_date
        4: Start_date
        5: Deposit_date
        6: Deposit_time
        7:
    """

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def __init__(self, **kwargs):
        super(Deposit_in_one_Screen, self).__init__(**kwargs)
        self.Split_payment = "No"
        self.Payment_method = ""
        self.Transfer_Reference = ""
        self.Card_nbr = 0
        self.Debit_type = ""
        self.Expiry_date = "null"
        self.Start_date = "null"
        self.Trans_Date = ""
        self.Trans_time = ""
        self.Auth_code = 0
        self.Amount = ""
        self.Receipt_Nbr = 0
        self.Deposit_date = ""
        self.Staff_id = 1

    # Checks on the values being passed
    # Payment method
    def dep_sal_option_choice(self, value):
        self.Payment_method = value

    # Debit type
    def Deposit_Debit_type(self, value):
        self.Debit_type = value

    # Card Expiry Date
    def Deposit_card_Exp_on_save(self, instance, value, date_range):
        Deposit_in_1_Expiry_Date = value
        self.Expiry_date = "{0}".format(value)
        self.ids.Card_Expiry_id.text = "Card Expiry date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            Deposit_in_1_Expiry_Date)

    # click cancel
    def Deposit_card_Exp_on_cancel(self, instance, value):
        pass

    def Deposit_card_Exp_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Deposit_card_Exp_on_save,
                         on_cancel=self.Deposit_card_Exp_on_cancel)
        date_dialog.open()

    # Card Start Date
    def Deposit_card_start_on_save(self, instance, value, date_range):
        Deposit_in_1_Start_Date = value
        self.Start_date = "{0}".format(value)
        self.ids.Card_Start_id.text = "Card start date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            Deposit_in_1_Start_Date)

    # click cancel
    def Deposit_card_start_on_cancel(self, instance, value):
        pass

    def Deposit_card_start_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Deposit_card_start_on_save,
                         on_cancel=self.Deposit_card_start_on_cancel)
        date_dialog.open()

    # Deposit Date
    def Deposit_transaction_on_save(self, instance, value, date_range):
        Deposit_in_1_Trans_Date = value
        self.Trans_Date = "{0}".format(value)
        self.Deposit_date = "{0}".format(value)
        self.ids.Deposit_transaction_Date_id.text = "Deposit date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            Deposit_in_1_Trans_Date)

    # click cancel
    def Deposit_transaction_on_cancel(self, instance, value):
        pass

    def Deposit_transaction_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Deposit_transaction_on_save,
                         on_cancel=self.Deposit_transaction_on_cancel)
        date_dialog.open()

    # Get time
    def Deposit_get_time(self, instance, time):
        Deposit_in_1_Trans_time = time
        self.Trans_time = "{0}".format(time)
        self.ids.Deposit_transaction_time_id.text = "Deposit Time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            Deposit_in_1_Trans_time)

    # Cancel
    def Deposit_on_time_cancel(self, instance, time):
        pass

    def show_Deposit_time_picker(self):
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
        time_dialog.bind(on_cancel=self.Deposit_on_time_cancel, time=self.Deposit_get_time)
        time_dialog.open()

    # submit to database
    def Deposit_in_1_submit(self):

        # Programme flows for variables to ensure that blank values are handled correctly
        # in preparation for database insert
        v5_x = self.manager.get_screen('deposit_or_sale').ids.veh_select_spin_id.text.split(',')
        v5c_id = v5_x[0]

        Fname = self.manager.get_screen('customerscreen').ids.firstname_textf.text
        if self.manager.get_screen('customerscreen').ids.middlename_textf == "":
            Mname = ""
        else:
            Mname = self.manager.get_screen('customerscreen').ids.middlename_textf.text

        Lname = self.manager.get_screen('customerscreen').ids.lastname_textf.text

        if self.manager.get_screen('customerscreen').Customer_DOB == "":
            DOB = ""
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

        if self.ids.deposit_in_one_transfer_ref_textf.text is None:
            self.Transfer_Reference = ""
        else:
            self.Transfer_Reference = self.ids.deposit_in_one_transfer_ref_textf.text

        if self.ids.deposit_in_1_card_nbr_textf.text is None:
            self.Card_nbr = 0
        else:
            self.Card_nbr = self.ids.deposit_in_1_card_nbr_textf.text

        if self.ids.Deposit_in_1_Debit_type_spin_id.text is None:
            self.Debit_type = ""

        if self.ids.Deposit_in_1_auth_textf.text is None:
            self.Auth_code = 0
        else:
            self.Auth_code = self.ids.Deposit_in_1_auth_textf.text

        if self.ids.Deposit_in_1_Amount_textf.text is None:
            self.Amount = ""
        else:
            self.Amount = self.ids.Deposit_in_1_Amount_textf.text

        if self.ids.Deposit_in_1_Receipt_nbr_textf.text is None:
            self.Receipt_Nbr = 0
        else:
            self.Receipt_Nbr = self.ids.Deposit_in_1_Receipt_nbr_textf.text

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
        sql_string13 = "set @Deposit_Amount = {0};".format(self.Amount.strip())
        sql_string14 = "set @Receipt_Nbr = {0};".format(self.Receipt_Nbr.strip())
        sql_string15 = 'Set @Fname= "{0}";'.format(Fname.strip())
        sql_string16 = 'Set @Mname= "{0}";'.format(Mname.strip())
        sql_string17 = 'Set @Lname= "{0}";'.format(Lname.strip())
        sql_string18 = "Set @DOB= '{0}';".format(DOB)
        sql_string19 = "set @Age_Group= '{0}';".format(Age_Group.strip())
        sql_string20 = "Set @Address1= '{0}';".format(Address1.strip())
        sql_string21 = 'Set @Address2= "{0}";'.format(Address2.strip())
        sql_string22 = "Set @Address3= '{0}';".format(Address3.strip())
        sql_string23 = "Set @Address4= '{0}';".format(Address4.strip())
        sql_string24 = "Set @Address5= '{0}';".format(Address5.strip())
        sql_string25 = "Set @Address6 = '{0}';".format(Address6.strip())
        sql_string26 = "Set @email = '{0}';".format(email.strip())
        sql_string27 = "Set @Tel = '{0}';".format(Tel.strip())
        sql_string28 = 'set @Sale_date= "";'
        sql_string29 = "set @Deposit_Date = '{0}';".format(self.Deposit_date)
        sql_string30 = "set @Staff_id = {0};".format(self.Staff_id.strip())
        sql_string31 = "call Customer_Insert_call();"

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
        mydb.commit()
        mydb.close()

        self.manager.current = "customerscreen"
