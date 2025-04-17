from kivy.uix.screenmanager import Screen, ScreenManager
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


class Deposit_or_SaleScreen(Screen):

    def __init__(self, **kwargs):
        super(Deposit_or_SaleScreen, self).__init__(**kwargs)
        self.V5c_id = ""
        self.Vehicle_reg = ""

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

    custom_list = Array_tup
    vehicle_list = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in custom_list]

    def selected_vehicle(self, value):
        x = value.split(',')

        self.Vehicle_reg = x[2]
        self.V5c_id = x[0]

    def Deposit_sale_option(self, value):
        pass

    def payment_method_selection(self, value):
        pass

    def Dep_Sal_options(self):
        if self.ids.Dep_Sal_spin_id.text == "Deposit" and self.ids.payment_option_spin_id.text == "One Payment":
            self.manager.current = 'Deposit_in_one'

        elif self.ids.Dep_Sal_spin_id.text == "Deposit" and self.ids.payment_option_spin_id.text == "Two Payments":
            self.manager.current = 'Deposit_in_two'

        elif self.ids.Dep_Sal_spin_id.text == "Deposit" and self.ids.payment_option_spin_id.text == "Three Payments":
            self.manager.current = 'Deposit_in_three'

        elif self.ids.Dep_Sal_spin_id.text == "Sale only" and self.ids.payment_option_spin_id.text == "One Payment":
            self.manager.current = 'Sale_in_one'

        elif self.ids.Dep_Sal_spin_id.text == "Sale only" and self.ids.payment_option_spin_id.text == "Two Payments":
            self.manager.current = 'Sale_in_two'

        elif self.ids.Dep_Sal_spin_id.text == "Sale only" and self.ids.payment_option_spin_id.text == "Three Payments":
            self.manager.current = 'Sale_in_three'

        elif self.ids.Dep_Sal_spin_id.text == "Sale after Deposit" and self.ids.payment_option_spin_id.text == "One Payment":
            self.manager.current = 'Sale_with_deposit_1'

        elif self.ids.Dep_Sal_spin_id.text == "Sale after Deposit" and self.ids.payment_option_spin_id.text == "Two Payments":
            self.manager.current = 'Sale_with_deposit_2'

        elif self.ids.Dep_Sal_spin_id.text == "Sale after Deposit" and self.ids.payment_option_spin_id.text == "Three Payments":
            self.manager.current = 'Sale_with_deposit_3'

    mydb.close()
