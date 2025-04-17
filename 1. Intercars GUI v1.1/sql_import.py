import mysql.connector

import os
DB_USER_1 = os.environ['DB_USER_1']
DB_PASSWORD_1 = os.environ['DB_PASSWORD_1']

def db_connection(self):
    cnn = mysql.connector.connect(
        host="localhost",
        user=DB_USER_1,
        password=DB_PASSWORD_1,
        database="icp",
        auth_plugin='mysql_native_password'
    )

    return cnn
