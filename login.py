# this is the login module

import pandas as pd
import random
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)
mycursor = mydb.cursor()

def signup():
    print("""
\nTHIS IS SIGN UP PAGE
""")
    fname = input("FIRSTNAME : ").upper()
    lname = input("LASTNAME: ").upper()
    state = input("STATE CODE (Eg: tn,ka,kl,etc): ").lower()
    gender = input("GENDER: ").upper()
    dob = input("DATE OF BIRTH (yyyy-mm-dd) : ")
    def mob_le():
        global mobile
        mobile = input("MOBILE NUMBER : ")
        a=0
        for i in mobile:
            if i.isdigit()==False:
                print("\nERROR: RE-ENTER YOU'RE MOBILE NUMBER\n")
                mob_le()
            a+=1
        if a!=10:
            print("\nERROR: RE-ENTER YOU'RE MOBILE NUMBER\n")
            mob_le()
    mob_le()
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
            print("\nWRONG INPUT!\nYOUR PASSWORD SHOULD HAVE ATLEAST ONE CAPITAL,SMALL,DIGIT AND NO SPACE.\n")
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
    user_info=(fname,lname,state,mobile,dob,c_passwd,gender,gen_uid)
    def login_continue():
        log_continue = input("\nDO YOU WANT TO CONTINUE y/Y, TO ABORT n/N: ").lower()
        if log_continue in ['y','n']:
            if log_continue == 'y':
                signin()
            elif log_continue == 'n':
                quit()
        else:
            print('\nWRONG INPUT!')
            login_continue()
    login_continue()

    formula1 = "insert into login_details (firstname,lastname,state,mobileno,dob,passwd,gender,uid) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(formula1,user_info)
    mydb.commit()

def signin():
    print("signin")
def admin():
    print("admin")

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
            break
        elif opt == 3:
            admin()
            break
    else:
        print(" INCORRECT OPTION!\n TRY AGAIN!")            
        init_login()
init_login()