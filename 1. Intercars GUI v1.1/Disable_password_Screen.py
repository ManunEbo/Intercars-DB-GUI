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


class Disable_password_Screen(Screen):
    def __init__(self, **kwargs):
        super(Disable_password_Screen, self).__init__(**kwargs)
        self.Staff_id = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    sql_str = """ select b.Staff_id,a.Fname,a.Lname from icp.Names a left join icp.Staff b on a.Staff_id = b.Staff_id where a.Staff_id is Not null; """

    mydata = pd.read_sql_query(sql_str, mydb)

    # converting the pandas dataframe into a numpy array
    num_data = mydata.to_numpy()

    # Reshaping the data
    Ar_shape = num_data.reshape(num_data.shape)
    # Converting to a list
    Array_tup = list(map(tuple, Ar_shape))

    staff_list_disable = ["{0}, {1}, {2}".format(x[0], x[1], x[2]) for x in Array_tup]

    def selected_staff_disable(self, value):
        x = value.split(',')
        self.Staff_id = x[0]

    def Disable_password(self):
        sql_string1 = "set @random_bytes = RANDOM_BYTES(16);"
        sql_string2 = "set @Staff_id = {0};".format(self.Staff_id.strip())
        sql_string3 = "update icp.Staff set Passwd = @random_bytes , iv = @random_bytes where Staff_id = @Staff_id;"

        print(sql_string1)
        print(sql_string2)
        print(sql_string3)

        mycursor = mydb.cursor()
        mycursor.execute(sql_string1)
        mycursor.execute(sql_string2)
        mycursor.execute(sql_string3)

        mydb.commit()
        mydb.close()

        self.manager.current = "staff_screen"
