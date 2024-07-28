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
    state = input("ENTER YOUR STATE : ")
    fname = input("ENTER YOUR FIRSTNAME  : ")
    lname = input("ENTER YOUR LASTNAME : ")
    dob = input("ENTER YOUR DATE OF BIRTH (yyyy/mm/dd) : ")
    mobile = input("ENTER YOUR MOBILE NUMBER : ")
    global user_info
    user_info=(fname,lname,state,mobile,dob)
    
signup()

formula1 = "insert into login_details (firstname,lastname,state,mobileno,dob) values (%s,%s,%s,%s,%s)"
mycursor.execute(formula1,("V","Sanjith","tn",'9446324247',"2007-08-31"))
mydb.commit()