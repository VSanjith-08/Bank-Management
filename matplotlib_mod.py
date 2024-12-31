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
    database = "bank_management"
)
mycursor = mydb.cursor()

import login
formula = f"select * from acc_details"
mycursor.execute(formula)
myresult = mycursor.fetchall()

mycursor = mydb.cursor()
formula = f"select * from acc_details"
mycursor.execute(formula)
myresult = mycursor.fetchall()

f2 = f"show columns from acc_details"
mycursor.execute(f2)
myresult2 = mycursor.fetchall()
lst = []
for i in myresult2:
    lst+=[i[0]]
df_login = pd.DataFrame(myresult,columns = lst)

df_acc_details = pd.DataFrame(myresult)
df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)
df_transaction = pd.read_csv("Database//transaction.csv",index_col = 0)

import login
upi_passwd = login.inp_passwd
u_id = login.inp_uid

user_name = df_login["cu_name"][df_login.uid == u_id].tolist()[0]

def bar_plot():
    mycursor = mydb.cursor()
    formula = f"select * from acc_details"
    mycursor.execute(formula)
    myresult = mycursor.fetchall()

    f2 = f"show columns from acc_details"
    mycursor.execute(f2)
    myresult2 = mycursor.fetchall()
    lst = []
    for i in myresult2:
        lst+=[i[0]]
    df_login = pd.DataFrame(myresult,columns = lst)
    gender = df_login['gender'].to_list()

    a = 0
    b = 0
    for i in gender:
        if i == "M":
            a+=1
        if i == "F":
            b+=1

    dict_gen = {
        "GENDER":['MALE','FEMALE'],
        'NUMBER':[a,b]
    }
    gender_ratio = pd.DataFrame(dict_gen)

    gender_ratio.plot(kind = "bar",x = "GENDER",title = "GENDER RATIO")
    plt.ylabel("NUMBER OF PEOPLE")
    plt.show()

def line_plot():
    import login
    upi_passwd = login.inp_passwd
    u_id = login.inp_uid

    mycursor = mydb.cursor()
    formula = f"select * from acc_details"
    mycursor.execute(formula)
    myresult = mycursor.fetchall()

    f2 = f"show columns from acc_details"
    mycursor.execute(f2)
    myresult2 = mycursor.fetchall()
    lst = []
    for i in myresult2:
        lst+=[i[0]]

    df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)
    df_transaction = pd.read_csv("Database//transaction.csv",index_col = 0)
    df_login = pd.DataFrame(myresult,columns = lst)
    df_wallet = df_wallet.rename({'balance':'balance2'},axis = 'columns')

    a = df_transaction["timestamp"].tolist()
    new_datestamp = []
    for i in a:
        new_datestamp+=[i[0:7]]
    df_transaction["timestamp"] = new_datestamp

    a = df_wallet["timestamp"].tolist()
    new_datestamp = []
    for i in a:
        new_datestamp+=[i[0:7]]
    df_wallet["timestamp"] = new_datestamp

    user = user_name
    df_baltime = df_transaction[df_transaction.uid == user].loc[:,['balance','timestamp']]
    index_baltime = 0
    for i in range(df_baltime.shape[0]):
        index_baltime +=1
    df_baltime.index = list(range(index_baltime))

    df_baltime2 = df_wallet[df_wallet.uid == user].loc[:,['balance2','timestamp']]
    index_baltime2 = 0
    for i in range(df_baltime2.shape[0]):
        index_baltime2 +=1
    df_baltime2.index = list(range(index_baltime2))

    a = df_baltime['timestamp'].to_list()
    no = 0
    j = []
    index = []
    for i in a:
        no+=1
        if i not in j:
            j+=[i]
            index+=[no-1]

    a = df_baltime2['timestamp'].to_list()
    no = 0
    j = []
    index2 = []
    for i in a:
        no+=1
        if i not in j:
            j+=[i]
            index2+=[no-1]

    df_baltime3 = df_baltime.loc[index]._append(df_baltime2.loc[index2],sort = True)

    df_baltime3.index = list(range(list(df_baltime3.shape)[0]))

    def line_plot1():
        df_baltime.loc[index].plot(kind='line',color = ['red'])
        plt.xticks(df_baltime.loc[index].index,df_baltime.loc[index].timestamp)
        plt.title(f"{user.upper()} : BANK BALANCE FOR EACH FINANCIAL MONTH")
        plt.xlabel("MONTH")
        plt.ylabel("BANK BALANCE")
        plt.show()

    def line_plot2():
        df_baltime.loc[index].plot(kind='line',color = ['red'])
        plt.plot(df_baltime3['timestamp'],df_baltime3['balance2'])
        plt.xticks(df_baltime.loc[index].index,df_baltime.loc[index].timestamp)
        plt.title(f"{user.upper()} : BANK BALANCE AND WALLET BALANCE FOR EACH FINANCIAL MONTH")
        plt.xlabel("MONTH")
        plt.ylabel("BANK BALANCE")
        plt.show()
    print("""
CHOOSE THE TYPE OF LINE PLOT.
        
1 - BANK BALANCE FOR EACH FINANCIAL MONTH
        
2 - BANK BALANCE AND WALLET BALANCE FOR EACH FINANCIAL MONTH
""")
    inp_mode = int(input(">>> "))
    while inp_mode not in [1,2,3]:
        print("INCORRECT OPTION\nRE-ENTER THE CORRECT OPTION")
        inp_mode = int(input(">>> "))

    if inp_mode == 1:
        line_plot1()
    elif inp_mode == 2:
        line_plot2()

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
