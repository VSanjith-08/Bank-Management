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

# Status of the login
def l_status():
    global lstatus
    lstatus = False
    if uid_pass:
        if passwd_pass:
            lstatus = True
    if lstatus:
        print("\n"+"-"*34)
        print("+++++",end="")
        print("\033[1;20;33m SUCCESSFULLY SIGNED-IN \033[0m",end="")
        print("+++++")
        print("-"*34)
        terminal_width = os.get_terminal_size().columns
        print("_"*terminal_width,"\n")
        
    global final_uid
    final_uid = inp_uid

#Signup module
def signup():
    print("\n"+"\033[1;20;33m=\033[0m"*30)
    print("\033[1;20;33m|::: THIS IS SIGN-UP PAGE :::|\033[0m")
    print("\033[1;20;33m=\033[0m"*30,"\n")
    fname = input("FIRSTNAME : ").upper()
    lname = input("LASTNAME: ").upper()
    gender = input("GENDER: ").upper()
        
    def passwd():
        global n_passwd
        n_passwd = input("PASSWORD: ")
        caps,small,digit,space,spc = False,False,False,False,False
        for i in n_passwd:
            if i.isupper():
                caps = True
            if i.islower():
                small = True
            if i.isspace():
                space = True
            if i.isdigit():
                digit = True
            if [i.isdigit(),i.isalpha(),i.isspace()] == [False,False,False]:
                spc = True
        if [caps,small,digit,space,spc] != [True,True,True,False,True]:
            
            print("\033[1;20;31m\nERROR: WRONG INPUT!\033[0m")
            print("\033[1;20;31mYOUR PASSWORD SHOULD HAVE ATLEAST ONE CAPITAL,SMALL,DIGIT,SPACE AND SPECIAL-CHARACTER.\n\033[0m")
            passwd()
        else:
            repeat()
    def repeat():
        global c_passwd
        c_passwd = input("REPEAT PASSWORD: ")
        while n_passwd != c_passwd:
            print("\033[1;20;31m\nERROR: PASSWORDS DOES NOT MATCH\n\033[0m")
            passwd()
            break
    passwd()

    def uid():
        formula = "select uid from login_details"
        mycursor.execute(formula)
        myresult = mycursor.fetchall()
        def generation_uid():
            global inp_uid
            inp_uid = input("USER ID: ")
            cont = True
            for i in myresult:
                if i[0] == inp_uid:
                    cont = False
            if cont == False:

                def gen_uiid():
                    global gn_uid
                    ct = len(fname+lname)
                    global gn_uid
                    if ct >= 7:
                        nam = (fname+lname)[:7]
                        gn_uid = (nam+str(random.randint(100,999))).lower()
                    else:
                        nam = fname+lname
                        gn_uid = (nam+str(random.randint(100,999))).lower()
                gen_uiid()
                for i in myresult:
                    if i[0] == gn_uid:
                        gen_uiid()

                print("\033[1;20;31m\nERROR: USER ID ALREADY IN USE, TRY AGAIN\033[0m")
                print("SUGGESTED USER IDS:  ",end="")
                for i in range(3):
                    gen_uiid()
                    print(gn_uid,end=" ")
                print("\n")
                generation_uid()
        generation_uid()
        
    uid()
    print("\033[1;20;34m\n##### YOU'RE NEWLY CREATED USER ID:#####\033[0m",f"\033[1;20;33m{inp_uid}\033[0m,\033[1;20;34m#####\033[0m")
    print("\033[1;20;34m\n##### PASSWORD:\033[0m",f"\033[1;20;33m{c_passwd}\033[0m"+"\033[1;20;34m #####\n\033[0m")
    global user_info
    user_info=(fname,lname,c_passwd,gender,inp_uid)

    formula1 = "insert into login_details (firstname,lastname,passwd,gender,uid) values (%s,%s,%s,%s,%s)"
    mycursor.execute(formula1,user_info)
    mydb.commit()

    print("\n"+"-"*30)
    print("+++++",end="")
    print("\033[1;20;33m SIGN-UP SUCCESSFUL \033[0m",end="")
    print("+++++")
    print("-"*30)
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width,"\n")

    def login_continue():
        print("\n"+"\033[1;20;92m=\033[0m"*30)
        print("\033[1;20;92m|::: THIS IS SIGN-IN PAGE :::|\033[0m")
        print("\033[1;20;92m=\033[0m"*30,"\n")

        log_continue = input("\nDO YOU WANT TO CONTINUE y/Y, TO ABORT n/N: ").lower()
        if log_continue in ['y','n']:
            if log_continue == 'y':
                signin()
                l_status()
            elif log_continue == 'n':
                quit()
        else:
            print('\nWRONG INPUT!')
            login_continue()
    login_continue()

    

def signin():
    formula = f"select uid from login_details"
    mycursor.execute(formula)
    retrived_uid = mycursor.fetchall()

    arr_retrived_uid = np.array([])
    for i in retrived_uid:
        arr_retrived_uid = np.concatenate((arr_retrived_uid,np.array([i[0]])))
    
    formula1 = f"select passwd from login_details"
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

def admin():
    print("this is admin module")

#starting init
def init_login():
    print("""
CHOOSE THE OPTION FROM THE FOLLOWING:
1 - SIGN IN
2 - SIGN UP
3 - ADMIN
          """)
    opt = int(input(">>> "))
    while opt in [1,2,3]:
        if opt == 2:
            signup()
            break
        elif opt == 1:
            signin()
            l_status()
            break
        elif opt == 3:
            admin()
            break
    else:
        print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m")         
        init_login()