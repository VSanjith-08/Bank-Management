import pandas as pd
import numpy as np
import os
from datetime import datetime
import mysql.connector

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
    print("bar plot")

def line_plot():
    print("line plot")


def init_statista():
    print("\n"+"="*22)
    print("|::: DEMOGRAPHICS :::|")
    print("="*22)
    print("""
CHOOSE THE TYPE OF ACCOUNT SERVICE
          
1 - BAR PLOT
          
2 - LINE PLOT

3 - MAIN MENU
""")
    # Function to repeat the input if the user gives a wrong input
    inp_mode = int(input(">>> "))
    def imp_mod():
        global inp_mode
        inp_mode = int(input(">>> "))
    if inp_mode in [1,2,3]:
        if inp_mode == 1:
            bar_plot()
        elif inp_mode == 2:
            line_plot()
        elif inp_mode == 3:
            import init_mainmenu
            terminal_width = os.get_terminal_size().columns
            print("_"*terminal_width)
            print()
            init_mainmenu.mainmenu()
    else:
        print("INCORRECT OPTION\nRE-ENTER THE CORRECT OPTION")
        imp_mod()
        