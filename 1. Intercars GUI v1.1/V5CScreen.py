from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker

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


class V5CScreen(Screen):
    def __init__(self, **kwargs):
        super(V5CScreen, self).__init__(**kwargs)
        self.First_Reg = ""
        self.First_Reg_uk = ""
        self.Logbook_issued_date = ""
        self.Owner1_Acq_date = ""
        self.Owner2_Acq_date = ""
        self.Owner3_Acq_date = ""
        self.Owner4_Acq_date = ""
        self.Prev_regnum = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # First registration date
    def First_Reg_on_save(self, instance, value, date_range):
        self.First_Reg = value
        self.ids.First_reg_lbl.text = "First registration:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.First_Reg)

    # click cancel
    def First_Reg_on_cancel(self, instance, value):
        pass

    def First_Reg_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1970,
            max_year=2050,)
        date_dialog.bind(on_save=self.First_Reg_on_save, on_cancel=self.First_Reg_on_cancel)
        date_dialog.open()

    # First registration UK date
    def First_Reg_uk_on_save(self, instance, value, date_range):

        self.First_Reg_uk = value
        self.ids.First_reg_uk_lbl.text = "First registration UK:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.First_Reg_uk)

    # click cancel
    def First_Reg_uk_on_cancel(self, instance, value):
        pass

    def First_Reg_uk_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1970,
            max_year=2050,)
        date_dialog.bind(on_save=self.First_Reg_uk_on_save, on_cancel=self.First_Reg_uk_on_cancel)
        date_dialog.open()

    # Logbook issue date
    def Logbook_issued_date_on_save(self, instance, value, date_range):
        self.Logbook_issued_date = value
        self.ids.Logbook_Issued_date_lbl.text = "Logbook issued date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Logbook_issued_date)

    # click cancel
    def Logbook_issued_date_on_cancel(self, instance, value):
        pass

    def Logbook_issued_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1970,
            max_year=2050,)
        date_dialog.bind(on_save=self.Logbook_issued_date_on_save,
                         on_cancel=self.Logbook_issued_date_on_cancel)
        date_dialog.open()

    # Owner 1 Acquisition date
    def Owner1_Acq_date_on_save(self, instance, value, date_range):
        self.Owner1_Acq_date = value
        self.ids.Owner1_Acq_date_lbl.text = "Owner1 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Owner1_Acq_date)

    # click cancel
    def Owner1_Acq_date_on_cancel(self, instance, value):
        pass

    def Owner1_Acq_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1970,
            max_year=2050,)
        date_dialog.bind(on_save=self.Owner1_Acq_date_on_save,
                         on_cancel=self.Owner1_Acq_date_on_cancel)
        date_dialog.open()

    # Owner 2 Acquisition date
    def Owner2_Acq_date_on_save(self, instance, value, date_range):
        self.Owner2_Acq_date = value
        self.ids.Owner2_Acq_date_lbl.text = "Owner2 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Owner2_Acq_date)

    # click cancel
    def Owner2_Acq_date_on_cancel(self, instance, value):
        pass

    def Owner2_Acq_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1970,
            max_year=2050,)
        date_dialog.bind(on_save=self.Owner2_Acq_date_on_save,
                         on_cancel=self.Owner2_Acq_date_on_cancel)
        date_dialog.open()

    # Owner 3 Acquisition date
    def Owner3_Acq_date_on_save(self, instance, value, date_range):
        self.Owner3_Acq_date = value
        self.ids.Owner3_Acq_date_lbl.text = "Owner3 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Owner3_Acq_date)

    # click cancel
    def Owner3_Acq_date_on_cancel(self, instance, value):
        pass

    def Owner3_Acq_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1970,
            max_year=2050,)
        date_dialog.bind(on_save=self.Owner3_Acq_date_on_save,
                         on_cancel=self.Owner3_Acq_date_on_cancel)
        date_dialog.open()

    # Owner 4 Acquisition date
    def Owner4_Acq_date_on_save(self, instance, value, date_range):
        self.Owner4_Acq_date = value
        self.ids.Owner4_Acq_date_lbl.text = "Owner4 Acq date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Owner4_Acq_date)

    # click cancel
    def Owner4_Acq_date_on_cancel(self, instance, value):
        pass

    def Owner4_Acq_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=1970,
            max_year=2050,)
        date_dialog.bind(on_save=self.Owner4_Acq_date_on_save,
                         on_cancel=self.Owner4_Acq_date_on_cancel)
        date_dialog.open()

    # Submit to database
    def Submit_V5C(self):

        if self.ids.Prev_regnum_textf.text is None:
            self.Prev_regnum = ""
        else:
            self.Prev_regnum = self.ids.Prev_regnum_textf.text

        if self.ids.Owner2_Name_textf.text is None:
            Prev_owner2_Name = ""
        else:
            Prev_owner2_Name = self.ids.Owner2_Name_textf.text

        if self.ids.Owner2_Address_textf.text is None:
            Prev_Owner2_Address = ""
        else:
            Prev_Owner2_Address = self.ids.Owner2_Address_textf.text

        if self.ids.Owner3_Name_textf.text is None:
            Prev_owner3_Name = ""
        else:
            Prev_owner3_Name = self.ids.Owner3_Name_textf.text

        if self.ids.Owner3_Address_textf.text is None:
            Prev_Owner3_Address = ""
        else:
            Prev_Owner3_Address = self.ids.Owner3_Address_textf.text

        if self.ids.Owner4_Name_textf.text is None:
            Prev_owner4_Name = ""
        else:
            Prev_owner4_Name = self.ids.Owner4_Name_textf.text

        if self.ids.Owner4_Address_textf.text is None:
            Prev_Owner4_Address = ""
        else:
            Prev_Owner4_Address = self.ids.Owner4_Address_textf.text

        sql_string1 = "set @Regnum = '{0}';".format(self.ids.Regnum_textf.text.strip().upper())
        sql_string2 = "set @Prev_regnum = '{0}';".format(self.Prev_regnum.strip().upper())
        sql_string3 = "set @Document_Reference = {0};".format(
            self.ids.Document_Reference_textf.text.strip())
        sql_string4 = "set @First_reg = '{0}';".format(self.First_Reg)
        sql_string5 = "set @first_reg_uk = '{0}';".format(self.First_Reg_uk)
        sql_string6 = "set @Make = '{0}';".format(self.ids.Make_textf.text.strip().upper())
        sql_string7 = "set @Model = '{0}';".format(self.ids.Model_textf.text.strip().upper())
        sql_string8 = "set @Bodytype ='{0}';".format(self.ids.Bodytype_textf.text.strip())
        sql_string9 = "set @TaxClass = '{0}';".format(self.ids.TaxClass_textf.text.strip())
        sql_string10 = "set @FuelType = '{0}';".format(self.ids.FuelType_textf.text.strip())
        sql_string11 = "set @number_Seats = {0};".format(self.ids.number_Seats_textf.text.strip())
        sql_string12 = "set @Vehicle_Category = '{0}';".format(
            self.ids.Vehicle_Category_textf.text.strip())
        sql_string13 = "set @Colour = '{0}';".format(self.ids.Colour_textf.text.strip().upper())
        sql_string14 = "set @Logbook_Issued_date = '{0}';".format(self.Logbook_issued_date)
        sql_string15 = "set @Cylinder_capacity = '{0}';".format(
            self.ids.Cylinder_capacity_textf.text.strip())
        sql_string16 = "set @nbr_Prev_Owners = {0};".format(
            self.ids.nbr_Prev_Owners_textf.text.strip())
        sql_string17 = "set @Prev_owner1_Name = '{0}';".format(
            self.ids.Owner1_Name_textf.text.strip())
        sql_string18 = "set @Prev_Owner1_Address = '{0}';".format(
            self.ids.Owner1_Address_textf.text.strip())
        sql_string19 = "set @prev_Owner1_Acq_date = '{0}';".format(self.Owner1_Acq_date)
        sql_string20 = "set @Prev_owner2_Name = '{0}';".format(Prev_owner2_Name.strip())
        sql_string21 = "set @Prev_Owner2_Address = '{0}';".format(Prev_Owner2_Address.strip())
        sql_string22 = "set @prev_Owner2_Acq_date = '{0}';".format(self.Owner2_Acq_date)
        sql_string23 = "set @Prev_owner3_Name = '{0}';".format(Prev_owner3_Name.strip())
        sql_string24 = "set @Prev_Owner3_Address = '{0}';".format(Prev_Owner3_Address.strip())
        sql_string25 = "set @prev_Owner3_Acq_date = '{0}';".format(self.Owner3_Acq_date)
        sql_string26 = "set @Prev_owner4_Name = '{0}';".format(Prev_owner4_Name.strip())
        sql_string27 = "set @Prev_Owner4_Address = '{0}';".format(Prev_Owner4_Address.strip())
        sql_string28 = "set @prev_Owner4_Acq_date = '{0}';".format(self.Owner4_Acq_date)
        sql_string29 = "call icp_V5C_Call();"

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

        mydb.commit()
        mydb.close()

        self.manager.current = "vehiclescreen"
