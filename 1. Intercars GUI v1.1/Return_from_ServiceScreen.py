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


class Return_from_ServiceScreen(Screen):

    def __init__(self, **kwargs):
        super(Return_from_ServiceScreen, self).__init__(**kwargs)
        self.V5C_id = ""
        self.Carwash_id = ""
        self.Elect_mech_id = ""
        self.Mech_Grg_id = ""
        self.MOT_Grg_id = ""
        self.Serv_type = ""
        self.Serv_date = ""
        self.Entity_Name = ""
        self.Return_date = ""
        self.Quality_check_val = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # Retrieving the vehicles that received a specific type of service
    def Service_type_return(self, value):
        self.Serv_type = value

        if self.Serv_type == "":
            serv_type_list = [("Select Service", "Service date")]
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_serv_date_select_spin_id.values = Serv_type_send_list

        elif self.Serv_type == "Carwash":

            # Pull the current inhouse vehicles for service
            sql_str = """ select a.V5C_id,
                		b.Model,
                		b.Reg_numb
                		from icp.Op_service a left join
                			 icp.V5C b
                			 on a.V5C_id = b.V5C_id
                			 where a.Serv_return_date is null and a.Serv_type = "Carwash"; """

            mydata = pd.read_sql_query(sql_str, mydb)

            # converting the pandas dataframe into a numpy array
            num_data = mydata.to_numpy()

            # Reshaping the data
            Ar_shape = num_data.reshape(num_data.shape)
            # Converting to a list
            Array_tup = list(map(tuple, Ar_shape))

            Vehicle_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup]
            self.ids.Vehicle_return_select_spin_id.values = Vehicle_return_list

        elif self.Serv_type == "Electrical":

            # Pull the current inhouse vehicles for service
            sql_str1 = """ select a.V5C_id,
                		b.Model,
                		b.Reg_numb
                		from icp.Op_service a left join
                			 icp.V5C b
                			 on a.V5C_id = b.V5C_id
                			 where a.Serv_return_date is null and a.Serv_type = "Electrical"; """

            mydata1 = pd.read_sql_query(sql_str1, mydb)

            # converting the pandas dataframe into a numpy array
            num_data1 = mydata1.to_numpy()

            # Reshaping the data
            Ar_shape1 = num_data1.reshape(num_data1.shape)
            # Converting to a list
            Array_tup1 = list(map(tuple, Ar_shape1))

            Vehicle_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup1]
            self.ids.Vehicle_return_select_spin_id.values = Vehicle_return_list

        elif self.Serv_type == "Mechanic":

            # Pull the current inhouse vehicles for service
            sql_str2 = """ select a.V5C_id,
                		b.Model,
                		b.Reg_numb
                		from icp.Op_service a left join
                			 icp.V5C b
                			 on a.V5C_id = b.V5C_id
                			 where a.Serv_return_date is null and a.Serv_type = "Mechanic"; """

            mydata2 = pd.read_sql_query(sql_str2, mydb)

            # converting the pandas dataframe into a numpy array
            num_data2 = mydata2.to_numpy()

            # Reshaping the data
            Ar_shape2 = num_data2.reshape(num_data2.shape)
            # Converting to a list
            Array_tup2 = list(map(tuple, Ar_shape2))

            Vehicle_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup2]
            self.ids.Vehicle_return_select_spin_id.values = Vehicle_return_list

        elif self.Serv_type == "MOT":

            # Pull the current inhouse vehicles for service
            sql_str3 = """ select a.V5C_id,
                		b.Model,
                		b.Reg_numb
                		from icp.Op_service a left join
                			 icp.V5C b
                			 on a.V5C_id = b.V5C_id
                			 where a.Serv_return_date is null and a.Serv_type = "MOT"; """

            mydata3 = pd.read_sql_query(sql_str3, mydb)

            # converting the pandas dataframe into a numpy array
            num_data3 = mydata3.to_numpy()

            # Reshaping the data
            Ar_shape3 = num_data3.reshape(num_data3.shape)
            # Converting to a list
            Array_tup3 = list(map(tuple, Ar_shape3))

            Vehicle_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup3]
            self.ids.Vehicle_return_select_spin_id.values = Vehicle_return_list

        else:
            print("Service type error")

    # **************************************************************************************************************
    # Extract the V5C_id this will be used to narrow down the service you sent the vehicle on
    # Here the code retrieves the Entity_Name and the serv_date
    def selected_vehicle_return(self, value):
        x = value.split(',')
        self.V5C_id = x[0]

        if self.Serv_type == "Carwash":
            sql_entity_serv_datex1 = """select a.Carwash_id,
                                        b.Entity_Name,
                                		a.serv_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.Carwash_id = b.Carwash_id
                                			 where a.Carwash_id is not null and a.Serv_type = "Carwash" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax1 = pd.read_sql_query(sql_entity_serv_datex1, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax1 = mydatax1.to_numpy()

            # Reshaping the data
            Ar_shapex1 = num_datax1.reshape(num_datax1.shape)
            # Converting to a list
            Array_tupx1 = list(map(tuple, Ar_shapex1))

            Serv_type_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tupx1]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Serv_type_return_list

        elif self.Serv_type == "Electrical":
            sql_entity_serv_datex2 = """select a.Elect_mech_id,
                                        b.Entity_Name,
                                		a.serv_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.Elect_mech_id = b.Elect_mech_id
                                			 where a.Elect_mech_id is not null and a.Serv_type = "Electrical" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax2 = pd.read_sql_query(sql_entity_serv_datex2, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax2 = mydatax2.to_numpy()

            # Reshaping the data
            Ar_shapex2 = num_datax2.reshape(num_datax2.shape)
            # Converting to a list
            Array_tupx2 = list(map(tuple, Ar_shapex2))

            Serv_type_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tupx2]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Serv_type_return_list

        elif self.Serv_type == "Mechanic":
            sql_entity_serv_datex3 = """select a.Mech_Grg_id,
                                        b.Entity_Name,
                                		a.serv_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.Mech_Grg_id = b.Mech_Grg_id
                                			 where a.Mech_Grg_id is not null and a.Serv_type = "Mechanic" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax3 = pd.read_sql_query(sql_entity_serv_datex3, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax3 = mydatax3.to_numpy()

            # Reshaping the data
            Ar_shapex3 = num_datax3.reshape(num_datax3.shape)
            # Converting to a list
            Array_tupx3 = list(map(tuple, Ar_shapex3))

            Serv_type_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tupx3]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Serv_type_return_list

        elif self.Serv_type == "MOT":
            sql_entity_serv_datex4 = """select a.MOT_Grg_id,
                                        b.Entity_Name,
                                		a.serv_date
                                		from icp.Op_service a left join
                                			 icp.Entity b
                                			 on a.MOT_Grg_id = b.MOT_Grg_id
                                			 where a.MOT_Grg_id is not null and a.Serv_type = "MOT" and a.V5C_id = {0}; """.format(self.V5C_id)

            mydatax4 = pd.read_sql_query(sql_entity_serv_datex4, mydb)

            # converting the pandas dataframe into a numpy array
            num_datax4 = mydatax4.to_numpy()

            # Reshaping the data
            Ar_shapex4 = num_datax4.reshape(num_datax4.shape)
            # Converting to a list
            Array_tupx4 = list(map(tuple, Ar_shapex4))

            Serv_type_return_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tupx4]

            # assigning the values for Entity_serv_date_select_spin_id
            self.ids.Entity_serv_date_select_spin_id.values = Serv_type_return_list

    # ****************************************************************************************************************
    # Narrowing down the actual vehicle and service on the date
    # here the date and service company is selected
    def selected_serv_type_return(self, value):
        x = value.split(',')

        if self.Serv_type == "Carwash":
            self.Carwash_id = x[0]
            self.Serv_date = x[2]

        elif self.Serv_type == "Electrical":
            self.Elect_mech_id = x[0]
            self.Serv_date = x[2]

        elif self.Serv_type == "Mechanic":
            self.Mech_Grg_id = x[0]
            self.Serv_date = x[2]

        elif self.Serv_type == "MOT":
            self.MOT_Grg_id = x[0]
            self.Serv_date = x[2]

    # Return date
    def Return_date_on_save(self, instance, value, date_range):
        self.Return_date = value
        self.ids.Return_date_lbl.text = "Return date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Return_date)

    # click cancel
    def Return_date_on_cancel(self, instance, value):
        pass

    def Return_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Return_date_on_save, on_cancel=self.Return_date_on_cancel)
        date_dialog.open()

    # Extract the quality check flag
    def Quality_check(self, value):
        self.Quality_check_val = value

    # Submit to database: Update icp.Op_Service
    def Submit_return_from_service(self):

        sql_string1 = "set @V5C_id = {0};".format(self.V5C_id.strip())
        sql_string2 = "set @Serv_date = '{0}';".format(self.Serv_date)
        sql_string3 = "set @Serv_return_date = '{0}';".format(self.Return_date)
        sql_string4 = "set @Service_quality_check_done = '{0}';".format(
            self.Quality_check_val.strip())
        sql_string5 = "set @Service_quality_description = '{0}';".format(
            self.ids.Quality_description_textf.text.strip())

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

        sql_string10 = "call Return_from_service_call();"

        print(sql_string1)
        print(sql_string2)
        print(sql_string3)
        print(sql_string4)
        print(sql_string5)
        print(sql_string6)
        print(sql_string7)
        print(sql_string8)
        print(sql_string9)

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

        mydb.commit()
        mydb.close()

        self.manager.current = "op_service_screen"
