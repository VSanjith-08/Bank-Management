# this is the login module

import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)
mycursor = mydb.cursor()

def signup():
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
    global user_info
    user_info=(fname,lname,state,mobile,dob,c_passwd,gender)
    
signup()

formula1 = "insert into login_details (firstname,lastname,state,mobileno,dob,passwd,gender) values (%s,%s,%s,%s,%s,%s,%s)"
mycursor.execute(formula1,user_info)
mydb.commit()