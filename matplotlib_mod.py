import pandas as pd
import numpy as np
import os
from datetime import datetime
import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)
mycursor = mydb.cursor()

import login
formula = f"select * from acc_details"
mycursor.execute(formula)
myresult = mycursor.fetchall()

df_acc_details = pd.DataFrame(myresult)
df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)
df_transaction = pd.read_csv("Database//transaction.csv",index_col = 0)

def bar_plot():
    gender = df_acc_details["Gender"]
    bar = plt.plot(kind='bar',x='gender',title='gender comparison')
    print(bar)

def line_plot():
    print('line plot')


def init_statista():
    print("\n"+"="*22)
    print("|::: DEMOGRAPHICS :::|")
    print("="*22)
    print("""
CHOOSE THE TYPE OF DEMOGRAPHICS.
          
1 - BAR PLOT
          
2 - LINE PLOT

3 - MAIN MENU
""")
    # command to repeat the input if the user gives a wrong input

    inp_mode = int(input(">>> "))
    while inp_mode not in [1,2,3]:
        print("INCORRECT OPTION\nRE-ENTER THE CORRECT OPTION")
        inp_mode = int(input(">>> "))

    if inp_mode == 1:
        bar_plot()
    elif inp_mode == 2:
        line_plot()
    elif inp_mode == 3:
        import init_mainmenu
        print()
        init_mainmenu.mainmenu()
