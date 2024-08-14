# this is the login module
import numpy as np
import pandas as pd
import random
import mysql.connector
import os

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)
mycursor = mydb.cursor()

def signin():
    
    print("\n"+"\033[1;20;92m=\033[0m"*30)
    print("\033[1;20;92m|::: THIS IS SIGN-IN PAGE :::|\033[0m")
    print("\033[1;20;92m=\033[0m"*30,"\n")

    formula = f"select uid from acc_details"
    mycursor.execute(formula)
    retrived_uid = mycursor.fetchall()

    arr_retrived_uid = np.array([])
    for i in retrived_uid:
        arr_retrived_uid = np.concatenate((arr_retrived_uid,np.array([i[0]])))
    
    formula1 = f"select passwd from acc_details"
    mycursor.execute(formula1)
    retrived_passwd = mycursor.fetchall()
    
    arr_retrived_passwd = np.array([])
    for i in retrived_passwd:
        arr_retrived_passwd = np.concatenate((arr_retrived_passwd,np.array([i[0]])))
    global uid_pass
    uid_pass = False
    global passwd_pass
    passwd_pass = False
    global inp_uid
    inp_uid = input("UID: ")
    if inp_uid in arr_retrived_uid:
        uid_pass = True
    else:
        i = 2
        while uid_pass == False:
            if i != 0:
                print("\033[1;20;31m\n### ERROR: INCORRECT UID ###\033[0m")
                inp_uid = input(f"YOU HAVE {i} MORE CHANCE\n\nRE-ENTER UID: ")
                if inp_uid in arr_retrived_uid:
                    uid_pass = True
            else:
                print("\033[1;20;33m\n### ####### ###\nYOU'RE GIVEN INPUTS ARE OVER\n\nTHANK YOU!\n\033[0m")
                quit()
            i-=1

    print()
    global inp_passwd
    inp_passwd = input("PASSWORD: ")
    if inp_passwd in arr_retrived_passwd:
        passwd_pass = True
    else:
        i = 2
        while passwd_pass == False:
            if i != 0:
                print("\033[1;20;31m\n### ERROR: INCORRECT PASSWORD ###\033[0m")
                inp_passwd = input(f"YOU HAVE {i} MORE CHANCE\n\nRE-ENTER PASSWORD: ")
                if inp_passwd in arr_retrived_passwd:
                    passwd_pass = True
            else:
                print("\033[1;20;33m\n### ####### ###\nYOU'RE GIVEN INPUTS ARE OVER\n\nTHANK YOU!\n\033[0m")
                quit()
            i-=1
    print("\n"+"-"*34)
    print("+++++",end="")
    print("\033[1;20;33m SUCCESSFULLY SIGNED-IN \033[0m",end="")
    print("+++++")
    print("-"*34)
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)

def admin():
    print("this is admin module")


#starting init
def init_login():
    print("""
CHOOSE THE OPTION FROM THE FOLLOWING:
1 - SIGN IN
2 - REGISTER
3 - ADMIN
          """)
    opt = int(input(">>> "))
    while opt in [1,2,3]:
        if opt == 2:
            import create_acc
            create_acc.create_acc()
            break
        elif opt == 1:
            signin()
            break
        elif opt == 3:
            admin()
            break
    else:
        print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m")         
        init_login()