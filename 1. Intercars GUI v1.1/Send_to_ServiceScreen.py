from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
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


class Send_to_ServiceScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.V5C_id = ""
        self.Vehicle_of_interest = ""
        self.Reg_numb = ""
        self.Serv_date = ""
        self.Serv_type = ""
        self.Entity_Name = ""
        self.Carwash_id = ""
        self.Elect_mech_id = ""
        self.Mech_Grg_id = ""
        self.MOT_Grg_id = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    sql_str = """ select a.V5C_id,
                    a.Model,
                    a.Reg_numb
                    from icp.V5C a
                    left join icp.Sale b
                    on a.V5C_id = b.V5C_id
                    where b.V5C_id is null; """

    mydata = pd.read_sql_query(sql_str, mydb)

    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    # Converting to a list
    Array_tup = list(map(tuple, Ar_shape))

    Vehicle_send_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup]

    def selected_vehicle_send(self, value):
        x = value.split(',')
        self.V5C_id = x[0]
        self.Vehicle_of_interest = x[1]
        self.Reg_numb = x[2]

    # Service date
    def serv_date_on_save(self, instance, value, date_range):
        self.Serv_date = value
        self.ids.serv_date_lbl.text = "Service date:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Serv_date)

    # click cancel
    def serv_date_on_cancel(self, instance, value):
        pass

    def serv_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.serv_date_on_save, on_cancel=self.serv_date_on_cancel)
        date_dialog.open()

    def Service_type_send(self, value):
        self.Serv_type = value

        if self.Serv_type == "":
            l = [("0", "Select Service")]
            serv_type_list = l
            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in serv_type_list]
            self.ids.Entity_list_select_spin_id.values = Serv_type_send_list

        elif self.Serv_type == "Carwash":
            Sql_carwash = """ select a.Carwash_id,
                        		b.Entity_Name
                        		from icp.Carwash a left join
                        			 icp.Entity b
                        			 on a.Carwash_id = b.Carwash_id
                        			 where b.Carwash_id is not null; """

            mydata1 = pd.read_sql_query(Sql_carwash, mydb)

            # converting the pandas dataframe into a numpy array
            num_data1 = mydata1.to_numpy()

            # Reshaping the data
            Ar_shape1 = num_data1.reshape(num_data1.shape)

            # Converting to a list
            Array_tup1 = list(map(tuple, Ar_shape1))

            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in Array_tup1]

            self.ids.Entity_list_select_spin_id.values = Serv_type_send_list

        elif self.Serv_type == "Electrical":

            Sql_Electrical = """ select a.Elect_mech_id,
                            		b.Entity_Name
                            		from icp.Electrical a left join
                            			 icp.Entity b
                            			 on a.Elect_mech_id = b.Elect_mech_id
                            			 where b.Elect_mech_id is not null; """

            mydata2 = pd.read_sql_query(Sql_Electrical, mydb)

            # converting the pandas dataframe into a numpy array
            num_data2 = mydata2.to_numpy()

            # Reshaping the data
            Ar_shape2 = num_data2.reshape(num_data2.shape)

            # Converting to a list
            Array_tup2 = list(map(tuple, Ar_shape2))

            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in Array_tup2]

            self.ids.Entity_list_select_spin_id.values = Serv_type_send_list

        elif self.Serv_type == "Mechanic":
            Sql_Mechanic = """ select a.Mech_Grg_id,
                        		b.Entity_Name
                        		from icp.Mechanic a left join
                        			 icp.Entity b
                        			 on a.Mech_Grg_id = b.Mech_Grg_id
                        			 where b.Mech_Grg_id is not null; """

            mydata3 = pd.read_sql_query(Sql_Mechanic, mydb)

            # converting the pandas dataframe into a numpy array
            num_data3 = mydata3.to_numpy()

            # Reshaping the data
            Ar_shape3 = num_data3.reshape(num_data3.shape)

            # Converting to a list
            Array_tup3 = list(map(tuple, Ar_shape3))

            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in Array_tup3]

            self.ids.Entity_list_select_spin_id.values = Serv_type_send_list

        elif self.Serv_type == "MOT":
            Sql_MOT = """ select a.MOT_Grg_id,
                        		b.Entity_Name
                        		from icp.MOT_Garage a left join
                        			 icp.Entity b
                        			 on a.MOT_Grg_id = b.MOT_Grg_id
                        			 where b.MOT_Grg_id is not null;"""

            mydata4 = pd.read_sql_query(Sql_MOT, mydb)

            # converting the pandas dataframe into a numpy array
            num_data4 = mydata4.to_numpy()

            # Reshaping the data
            Ar_shape4 = num_data4.reshape(num_data4.shape)

            # Converting to a list
            Array_tup4 = list(map(tuple, Ar_shape4))

            Serv_type_send_list = ["{0}, {1}".format(x[0], x[1]) for x in Array_tup4]

            self.ids.Entity_list_select_spin_id.values = Serv_type_send_list

        else:
            print("Service type Error!")

    def selected_serv_type_send(self, value):
        x = value.split(',')

        if self.Serv_type == "Carwash":
            self.Carwash_id = x[0]
            self.Entity_Name = "{0}".format(x[1])

        elif self.Serv_type == "Electrical":
            self.Elect_mech_id = x[0]
            self.Entity_Name = "{0}".format(x[1])

        elif self.Serv_type == "Mechanic":
            self.Mech_Grg_id = x[0]
            self.Entity_Name = "{0}".format(x[1])

        elif self.Serv_type == "MOT":
            self.MOT_Grg_id = x[0]
            self.Entity_Name = "{0}".format(x[1])

        else:
            print("Error!")

    # Submit to database
    def Submit_send_to_service(self):

        sql_string1 = "set @V5C_id = {0};".format(self.V5C_id.strip())
        sql_string2 = "set @serv_date = '{0}';".format(self.Serv_date)
        sql_string3 = "set @serv_type = '{0}';".format(self.Serv_type.strip())
        sql_string4 = "set @Description = '{0}';".format(
            self.ids.Serv_Description_textf.text.strip())

        if self.Carwash_id == "":
            sql_string5 = 'set @Carwash_id = "{0}";'.format(self.Carwash_id.strip())
        else:
            sql_string5 = "set @Carwash_id = {0};".format(self.Carwash_id.strip())

        if self.Elect_mech_id == "":
            sql_string6 = 'set @Elect_mech_id = "{0}";'.format(self.Elect_mech_id.strip())
        else:
            sql_string6 = "set @Elect_mech_id = {0};".format(self.Elect_mech_id.strip())

        if self.Mech_Grg_id == "":
            sql_string7 = 'set @Mech_Grg_id = "{0}";'.format(self.Mech_Grg_id.strip())
        else:
            sql_string7 = "set @Mech_Grg_id = {0};".format(self.Mech_Grg_id.strip())

        if self.MOT_Grg_id == "":
            sql_string8 = 'set @MOT_Grg_id = "{0}";'.format(self.MOT_Grg_id.strip())
        else:
            sql_string8 = "set @MOT_Grg_id = {0};".format(self.MOT_Grg_id.strip())

        sql_string9 = "call Op_new_serv_call();"

        print(sql_string1)
        print(sql_string2)
        print(sql_string3)
        print(sql_string4)
        print(sql_string5)
        print(sql_string6)
        print(sql_string7)
        print(sql_string8)

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

        mydb.commit()
        mydb.close()

        self.manager.current = "op_service_screen"

        # Reset the values
        self.Carwash_id = ""
        self.Elect_mech_id = ""
        self.Mech_Grg_id = ""
        self.MOT_Grg_id = ""
