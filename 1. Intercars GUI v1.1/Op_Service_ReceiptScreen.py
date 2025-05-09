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


class Op_Service_ReceiptScreen(Screen):

    def __init__(self, **kwargs):
        super(Op_Service_ReceiptScreen, self).__init__(**kwargs)
        self.Op_service_id = ""
        self.Serv_type = ""
        self.Serv_Invoice_Date = ""
        self.Serv_Invoice_nbr = ""
        self.Price = ""
        self.VAT_Flag = ""
        self.Split_payment = ""
        self.Trans_Date = ""
        self.Trans_time = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def Service_type_Receip(self, value):
        self.Serv_type = value

        if self.Serv_type == "Carwash":

            # Pull the current inhouse vehicles for service
            sql_str = """ select a.Op_service_id,
                    		a.Serv_Invoice_Date,
                    		a.Serv_Invoice_nbr,
                            a.Price
                                from icp.Op_service a left join
                                icp.Op_service_Receipt b
                                on a.Op_service_id = b.Op_service_id
                                left join
                                icp.Op_bank_transfer c
                                on a.Op_service_id = c.Op_service_id
                                    where a.Serv_type = "Carwash" and b.Op_service_id is null and  c.Op_service_id is null and a.Serv_Invoice_Date is not null
                                    order by a.Op_service_id; """

            mydata = pd.read_sql_query(sql_str, mydb)

            # converting the pandas dataframe into a numpy array
            num_data = mydata.to_numpy()

            # Reshaping the data
            Ar_shape = num_data.reshape(num_data.shape)
            # Converting to a list
            Array_tup = list(map(tuple, Ar_shape))

            Serv_type_Receipt_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tup]

            self.ids.Service_invoice_select_spin_id.values = Serv_type_Receipt_list

        elif self.Serv_type == "Electrical":

            sql_str1 = """ select a.Op_service_id,
                    		a.Serv_Invoice_Date,
                    		a.Serv_Invoice_nbr,
                            a.Price
                                from icp.Op_service a left join
                                icp.Op_service_Receipt b
                                on a.Op_service_id = b.Op_service_id
                                left join
                                icp.Op_bank_transfer c
                                on a.Op_service_id = c.Op_service_id
                                    where a.Serv_type = "Electrical" and b.Op_service_id is null and  c.Op_service_id is null and a.Serv_Invoice_Date is not null
                                    order by a.Op_service_id; """

            mydata1 = pd.read_sql_query(sql_str1, mydb)

            # converting the pandas dataframe into a numpy array
            num_data1 = mydata1.to_numpy()

            # Reshaping the data
            Ar_shape1 = num_data1.reshape(num_data1.shape)
            # Converting to a list
            Array_tup1 = list(map(tuple, Ar_shape1))

            Serv_type_Receipt_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tup1]

            self.ids.Service_invoice_select_spin_id.values = Serv_type_Receipt_list

        elif self.Serv_type == "Mechanic":

            sql_str2 = """ select a.Op_service_id,
                    		a.Serv_Invoice_Date,
                    		a.Serv_Invoice_nbr,
                            a.Price
                                from icp.Op_service a left join
                                icp.Op_service_Receipt b
                                on a.Op_service_id = b.Op_service_id
                                left join
                                icp.Op_bank_transfer c
                                on a.Op_service_id = c.Op_service_id
                                    where a.Serv_type = "Mechanic" and b.Op_service_id is null and  c.Op_service_id is null and a.Serv_Invoice_Date is not null
                                    order by a.Op_service_id; """

            mydata2 = pd.read_sql_query(sql_str2, mydb)

            # converting the pandas dataframe into a numpy array
            num_data2 = mydata2.to_numpy()

            # Reshaping the data
            Ar_shape2 = num_data2.reshape(num_data2.shape)
            # Converting to a list
            Array_tup2 = list(map(tuple, Ar_shape2))

            Serv_type_Receipt_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tup2]

            self.ids.Service_invoice_select_spin_id.values = Serv_type_Receipt_list

        elif self.Serv_type == "MOT":

            sql_str3 = """select a.Op_service_id,
                    		a.Serv_Invoice_Date,
                    		a.Serv_Invoice_nbr,
                            a.Price
                                from icp.Op_service a left join
                                icp.Op_service_Receipt b
                                on a.Op_service_id = b.Op_service_id
                                left join
                                icp.Op_bank_transfer c
                                on a.Op_service_id = c.Op_service_id
                                    where a.Serv_type = "MOT" and b.Op_service_id is null and  c.Op_service_id is null and a.Serv_Invoice_Date is not null
                                    order by a.Op_service_id; """

            mydata3 = pd.read_sql_query(sql_str3, mydb)

            # converting the pandas dataframe into a numpy array
            num_data3 = mydata3.to_numpy()

            # Reshaping the data
            Ar_shape3 = num_data3.reshape(num_data3.shape)
            # Converting to a list
            Array_tup3 = list(map(tuple, Ar_shape3))

            Serv_type_Receipt_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tup3]
            self.ids.Service_invoice_select_spin_id.values = Serv_type_Receipt_list

        else:
            print("Error: Unknown service type!")

    def Serv_Receipt_invoice(self, value):
        x = value.split(',')

        self.Op_service_id = x[0]
        self.Serv_Invoice_Date = x[1]
        self.Serv_Invoice_nbr = x[2]
        self.Price = x[3]

        # Setting the values for splitpayment
        Split_payment1 = [(0, "N"), (1, "Y")]
        Split_payment_list = ["{0}, {1}".format(x[0], x[1]) for x in Split_payment1]
        self.ids.Split_payment_select_spin_id.values = Split_payment_list

    # creating the splitpayment flag
    def Split_payment_call(self, value):
        x = value.split(',')
        self.Split_payment = x[0]

    # Transaction date
    def Transaction_date_on_save(self, instance, value, date_range):
        self.Trans_Date = value
        self.ids.Transaction_date_lbl.text = "Transaction date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_Date)

    # click cancel
    def Transaction_date_on_cancel(self, instance, value):
        pass

    def Transaction_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Transaction_date_on_save,
                         on_cancel=self.Transaction_date_on_cancel)
        date_dialog.open()

    # Get time
    def trans_get_time(self, instance, time):
        self.Trans_time = time
        self.ids.Transaction_time_id.text = "Transaction time:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Trans_time)

    # Cancel
    def trans_on_time_cancel(self, instance, time):
        pass

    def show_Transaction_time_picker(self):
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
        time_dialog.bind(on_cancel=self.trans_on_time_cancel, time=self.trans_get_time)
        time_dialog.open()

    # Extracting the VAT flag
    def VAT_Receip(self, value):
        self.VAT_Flag = value

    # Update icp.Op_Service
    def Submit_service_Receipt(self):

        sql_string1 = "set @Op_service_id = {0};".format(self.Op_service_id.strip())
        sql_string2 = "set @Split_payment = '{0}';".format(self.Split_payment.strip())
        sql_string3 = "set @Trans_Date = '{0}';".format(self.Trans_Date)
        sql_string4 = "set @Trans_time = '{0}';".format(self.Trans_time)
        sql_string5 = "set @Auth_code = {0};".format(self.ids.Auth_code_textf.text.strip())
        sql_string6 = "set @Receipt_nbr = {0};".format(self.ids.Receipt_nbr_textf.text.strip())
        sql_string7 = "set @Amount = {0};".format(self.ids.Amount_textf.text.strip())
        sql_string8 = "set @VAT_Flag = '{0}';".format(self.VAT_Flag.strip())

        if self.VAT_Flag == "Y":
            sql_string9 = "set @VAT_rate = 0.2;"
            sql_string10 = "set @VAT = {0};".format(float(float(self.ids.Amount_textf.text) -
                                                          (float(self.ids.Amount_textf.text)/1.2)))
            sql_string11 = "set @Net = {0};".format(float(self.ids.Amount_textf.text)/1.2)

        sql_string12 = "call Op_service_receipt_call();"

        print(sql_string1)
        print(sql_string2)
        print(sql_string3)
        print(sql_string4)
        print(sql_string5)
        print(sql_string6)
        print(sql_string7)
        print(sql_string8)

        if self.VAT_Flag == "Y":
            print(sql_string9)
            print(sql_string10)
            print(sql_string11)

        mycursor = mydb.cursor()
        mycursor.execute(sql_string1)
        mycursor.execute(sql_string2)
        mycursor.execute(sql_string3)
        mycursor.execute(sql_string4)
        mycursor.execute(sql_string5)
        mycursor.execute(sql_string6)
        mycursor.execute(sql_string7)
        mycursor.execute(sql_string8)

        if self.VAT_Flag == "Y":
            mycursor.execute(sql_string9)
            mycursor.execute(sql_string10)
            mycursor.execute(sql_string11)

        mycursor.execute(sql_string12)
        mydb.commit()
        mydb.close()

        self.manager.current = "operation_screen"
