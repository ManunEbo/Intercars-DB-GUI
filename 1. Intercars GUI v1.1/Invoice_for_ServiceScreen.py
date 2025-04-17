from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker
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


class Invoice_for_ServiceScreen(Screen):

    def __init__(self, **kwargs):
        super(Invoice_for_ServiceScreen, self).__init__(**kwargs)
        self.V5C_id = ""
        self.Carwash_id = ""
        self.Elect_mech_id = ""
        self.Mech_Grg_id = ""
        self.MOT_Grg_id = ""
        self.Serv_type = ""
        self.Serv_date = ""
        self.Invoice_date = ""
        self.Serv_return_date = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def Service_type_invoice(self, value):
        self.Serv_type = value

        # retrieving carwash services that have no invoices
        if self.Serv_type == "Carwash":

            # Pull the current inhouse vehicles for service
            sql_str = """ select a.V5C_id,
                        		b.Model,
                        		b.Reg_numb
                        		from icp.Op_service a left join
                        			icp.V5C b
                        			on a.V5C_id = b.V5C_id
                        			where a.Serv_return_date is not null and a.Serv_type = "Carwash" and a.Carwash_id is not null and a.Serv_Invoice_Date is null
                        			order by a.V5C_id; """

            mydata = pd.read_sql_query(sql_str, mydb)

            # converting the pandas dataframe into a numpy array
            num_data = mydata.to_numpy()

            # Reshaping the data
            Ar_shape = num_data.reshape(num_data.shape)
            # Converting to a list
            Array_tup = list(map(tuple, Ar_shape))

            Vehicle_invoice_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup]
            self.ids.Vehicle_invoice_select_spin_id.values = Vehicle_invoice_list

        # retrieving Electrical services that have no invoices
        elif self.Serv_type == "Electrical":

            sql_str1 = """ select a.V5C_id,
                        		b.Model,
                        		b.Reg_numb
                        		from icp.Op_service a left join
                        			icp.V5C b
                        			on a.V5C_id = b.V5C_id
                        			where a.Serv_return_date is not null and a.Serv_type = "Electrical" and a.Elect_mech_id is not null and a.Serv_Invoice_Date is null
                        			order by a.V5C_id; """

            mydata1 = pd.read_sql_query(sql_str1, mydb)

            # converting the pandas dataframe into a numpy array
            num_data1 = mydata1.to_numpy()

            # Reshaping the data
            Ar_shape1 = num_data1.reshape(num_data1.shape)
            # Converting to a list
            Array_tup1 = list(map(tuple, Ar_shape1))

            Vehicle_invoice_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup1]
            self.ids.Vehicle_invoice_select_spin_id.values = Vehicle_invoice_list

        # retrieving Mechanic services that have no invoices
        elif self.Serv_type == "Mechanic":

            sql_str2 = """ select a.V5C_id,
                    		b.Model,
                    		b.Reg_numb
                    		from icp.Op_service a left join
                    			icp.V5C b
                    			on a.V5C_id = b.V5C_id
                    			where a.Serv_return_date is not null and a.Serv_type = "Mechanic" and a.Mech_Grg_id is not null and a.Serv_Invoice_Date is null
                    			order by a.V5C_id; """

            mydata2 = pd.read_sql_query(sql_str2, mydb)

            # converting the pandas dataframe into a numpy array
            num_data2 = mydata2.to_numpy()

            # Reshaping the data
            Ar_shape2 = num_data2.reshape(num_data2.shape)
            # Converting to a list
            Array_tup2 = list(map(tuple, Ar_shape2))

            Vehicle_invoice_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup2]
            self.ids.Vehicle_invoice_select_spin_id.values = Vehicle_invoice_list

        # retrieving MOT services that have no invoices
        elif self.Serv_type == "MOT":

            sql_str3 = """ select a.V5C_id,
                    		b.Model,
                    		b.Reg_numb
                    		from icp.Op_service a left join
                    			icp.V5C b
                    			on a.V5C_id = b.V5C_id
                    			where a.Serv_return_date is not null and a.Serv_type = "MOT" and MOT_Grg_id is not null and a.Serv_Invoice_Date is null
                    			order by a.V5C_id; """

            mydata3 = pd.read_sql_query(sql_str3, mydb)

            # converting the pandas dataframe into a numpy array
            num_data3 = mydata3.to_numpy()

            # Reshaping the data
            Ar_shape3 = num_data3.reshape(num_data3.shape)
            # Converting to a list
            Array_tup3 = list(map(tuple, Ar_shape3))

            Vehicle_invoice_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup3]
            self.ids.Vehicle_invoice_select_spin_id.values = Vehicle_invoice_list

        else:
            print("Service type error!")

    # **************************************************************************************************************
    # Extract the V5C_id this will be used to narrow down the service you sent the vehicle on
    # Here the code retrieves the Entity_Name and the serv_date
    def selected_vehicle_invoice(self, value):
        x = value.split(',')
        self.V5C_id = x[0]

        if self.Serv_type == "Carwash":
            sql_entity_serv_datex1 = """select a.Carwash_id,
                                        b.Entity_Name,
                                		a.serv_date,
                                        a.Serv_return_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.Carwash_id = b.Carwash_id
                                			 where a.Serv_return_date is not null and a.Carwash_id is not null and a.Serv_type = "Carwash" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax1 = pd.read_sql_query(sql_entity_serv_datex1, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax1 = mydatax1.to_numpy()

            # Reshaping the data
            Ar_shapex1 = num_datax1.reshape(num_datax1.shape)
            # Converting to a list
            Array_tupx1 = list(map(tuple, Ar_shapex1))

            Entity_serv_date_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tupx1]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Entity_serv_date_list

        elif self.Serv_type == "Electrical":
            sql_entity_serv_datex2 = """select a.Elect_mech_id,
                                        b.Entity_Name,
                                		a.serv_date,
                                        a.Serv_return_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.Elect_mech_id = b.Elect_mech_id
                                			 where a.Serv_return_date is not null and a.Elect_mech_id is not null and a.Serv_type = "Electrical" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax2 = pd.read_sql_query(sql_entity_serv_datex2, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax2 = mydatax2.to_numpy()

            # Reshaping the data
            Ar_shapex2 = num_datax2.reshape(num_datax2.shape)
            # Converting to a list
            Array_tupx2 = list(map(tuple, Ar_shapex2))

            Entity_serv_date_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tupx2]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Entity_serv_date_list

        elif self.Serv_type == "Mechanic":
            sql_entity_serv_datex3 = """select a.Mech_Grg_id,
                                        b.Entity_Name,
                                		a.serv_date,
                                        a.Serv_return_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.Mech_Grg_id = b.Mech_Grg_id
                                			 where a.Serv_return_date is not null and a.Mech_Grg_id is not null and a.Serv_type = "Mechanic" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax3 = pd.read_sql_query(sql_entity_serv_datex3, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax3 = mydatax3.to_numpy()

            # Reshaping the data
            Ar_shapex3 = num_datax3.reshape(num_datax3.shape)
            # Converting to a list
            Array_tupx3 = list(map(tuple, Ar_shapex3))

            Entity_serv_date_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tupx3]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Entity_serv_date_list

        elif self.Serv_type == "MOT":
            sql_entity_serv_datex4 = """select a.MOT_Grg_id,
                                        b.Entity_Name,
                                		a.serv_date,
                                        a.Serv_return_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.MOT_Grg_id = b.MOT_Grg_id
                                			 where a.Serv_return_date is not null and a.MOT_Grg_id is not null and a.Serv_type = "MOT" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax4 = pd.read_sql_query(sql_entity_serv_datex4, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax4 = mydatax4.to_numpy()

            # Reshaping the data
            Ar_shapex4 = num_datax4.reshape(num_datax4.shape)
            # Converting to a list
            Array_tupx4 = list(map(tuple, Ar_shapex4))

            Entity_serv_date_list = ["{0}, {1}, {2}, {3}".format(
                x[0], x[1], x[2], x[3]) for x in Array_tupx4]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Entity_serv_date_list

    def select_Entity_serv_date_invoice(self, value):
        x = value.split(',')

        if self.Serv_type == "Carwash":
            self.Carwash_id = x[0]
            self.Serv_date = x[2]
            self.Serv_return_date = x[3]

        elif self.Serv_type == "Electrical":
            self.Elect_mech_id = x[0]
            self.Serv_date = x[2]
            self.Serv_return_date = x[3]

        elif self.Serv_type == "Mechanic":
            self.Mech_Grg_id = x[0]
            self.Serv_date = x[2]
            self.Serv_return_date = x[3]

        elif self.Serv_type == "MOT":
            self.MOT_Grg_id = x[0]
            self.Serv_date = x[2]
            self.Serv_return_date = x[3]

        else:
            print("Say what???")

    # Invoice date
    def Invoice_date_on_save(self, instance, value, date_range):
        self.Invoice_date = value
        self.ids.Invoice_date_lbl.text = "Return date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Invoice_date)

    # click cancel
    def Invoice_date_on_cancel(self, instance, value):
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
        date_dialog.bind(on_save=self.Invoice_date_on_save, on_cancel=self.Invoice_date_on_cancel)
        date_dialog.open()

    # Update icp.Op_Service
    def Submit_invoice_for_service(self):

        sql_string1 = "set @V5C_id = {0};".format(self.V5C_id.strip())
        sql_string2 = "set @Serv_date = '{0}';".format(self.Serv_date)
        sql_string3 = "set @Serv_return_date = '{0}';".format(self.Serv_return_date)
        sql_string4 = "set @Serv_Invoice_nbr = '{0}';".format(
            self.ids.Invoice_nbr_textf.text.strip())
        sql_string5 = "set @Serv_Invoice_Date = '{0}';".format(self.Invoice_date)

        if self.Carwash_id == "":
            sql_string6 = 'set @Carwash_id = "{0}";'.format(self.Carwash_id.strip())
        else:
            sql_string6 = "set @Carwash_id = {0};".format(self.Carwash_id.strip())

        if self.Elect_mech_id == "":
            sql_string7 = 'set @Elect_mech_id = "{0}";'.format(self.Elect_mech_id.strip())
        else:
            sql_string7 = "set @Elect_mech_id = {0};".format(self.Elect_mech_id.strip())

        if self.Mech_Grg_id == "":
            sql_string8 = 'set @Mech_Grg_id = "{0}";'.format(self.Mech_Grg_id.strip())
        else:
            sql_string8 = "set @Mech_Grg_id = {0};".format(self.Mech_Grg_id.strip())

        if self.MOT_Grg_id == "":
            sql_string9 = 'set @MOT_Grg_id = "{0}";'.format(self.MOT_Grg_id.strip())
        else:
            sql_string9 = "set @MOT_Grg_id = {0};".format(self.MOT_Grg_id.strip())

        sql_string10 = "set @Description = '{0}';".format(self.ids.Description_textf.text.strip())
        sql_string11 = "set @Price = {0};".format(self.ids.Price_textf.text.strip())
        sql_string12 = "call Invoice_Update_call();"

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

        mydb.commit()

        mydb.close()
        self.manager.current = "op_service_screen"
