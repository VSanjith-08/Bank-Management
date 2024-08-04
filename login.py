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
        print("\n"+"-"*30)
        print("+++++",end="")
        print("\033[1;20;33m SIGN-IN SUCCESSFUL \033[0m",end="")
        print("+++++")
        print("-"*30)
        
    global final_uid
    final_uid = inp_uid

#Signup module
def signup():
    print("""
\nTHIS IS SIGN-UP PAGE
""")
    fname = input("FIRSTNAME : ").upper()
    lname = input("LASTNAME: ").upper()
    state = input("STATE CODE (Eg: tn,ka,kl,etc): ").lower()
    gender = input("GENDER: ").upper()
    dob = input("DATE OF BIRTH (yyyy-mm-dd) : ")
    mob = input("MOBILE NUMBER: ")
    # Checking is all the given characters in mobile number is a digit and of 10 digits
    a = 2
    while a != 0:
        def chk():
            print(f'\nERROR: INCORRECT MOBILE NUMBER\n\nYOU HAVE ONLY {a} MORE ATTEMPTS')
            global mo
            mo = input("RE-ENTER YOUR MOBILE NUMBER:\n>>> ")
                        
        if len(mob) == 10:
            for i in mob:
                if i.isalpha():
                    chk()
                    break
                else:
                    a = 1
                    break
        else:
            chk()
            mob = mo
        a-=1

        # If all the 3 chances are over for re-writing the mobile number
    if len(mob) == 10:
        for i in mob:
            if i.isalpha():
                quit()
            else:
                break
    else:
        quit()
        
    def passwd():
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
            print("\033[1;20;31mYOUR PASSWORD SHOULD HAVE ATLEAST ONE CAPITAL,SMALL,DIGIT AND NO SPACE.\n\033[0m")
            passwd()
        global c_passwd
        c_passwd = input("REPEAT PASSWORD: ")
        if n_passwd == c_passwd:
            pass
        else:
            print("\nERROR: PASSWORDS DOES NOT MATCH\n")
            passwd()

    passwd()
    def uid():
        formula = "select uid from login_details"
        mycursor.execute(formula)
        myresult = mycursor.fetchall()
        def gen_uiid():
            global gen_uid
            ct = len(fname+lname)
            global gen_uid
            if ct >= 7:
                nam = (fname+lname)[:7]
                gen_uid = (nam+str(random.randint(100,999))).lower()
            else:
                nam = fname+lname
                gen_uid = (nam+str(random.randint(100,999))).lower()
        gen_uiid()
        for i in myresult:
            if i[0] == gen_uid:
                gen_uiid()
    uid()
    print(f"\n##### YOU'RE NEWLY CREATED USER ID: {gen_uid} #####")
    print(f"\n##### PASSWORD: {c_passwd} #####\n")
    global user_info
    user_info=(fname,lname,state,mob,dob,c_passwd,gender,gen_uid)

    formula1 = "insert into login_details (firstname,lastname,state,mobileno,dob,passwd,gender,uid) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(formula1,user_info)
    mydb.commit()

    print("\n"+"-"*30)
    print("+++++",end="")
    print("\033[1;20;33m SIGN-UP SUCCESSFUL \033[0m",end="")
    print("+++++")
    print("-"*30)

    def login_continue():
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
    print("""
THIS IS SIGN-IN PAGE
""")
    
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
                print("\n### ####### ###\nYOU'RE GIVEN INPUTS ARE OVER\n\nTHANK YOU!\n")
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
                print("\n### ####### ###\nYOU'RE GIVEN INPUTS ARE OVER\n\nTHANK YOU!\n")
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
        print(" INCORRECT OPTION!\n TRY AGAIN!")            
        init_login()