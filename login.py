# this is the login module

import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Sanjay@2000",
    database = "Bank_Management"
)

mycursor = mydb.cursor()

formula1 = "import into login_details values()"
    


def signup():
  state = input("ENTER YOUR STATE : ")
  fname = input("ENTER YOUR FIRSTNAME  : ")
  lname = input("ENTER YOUR LASTNAME : ")
  dob = input("ENTER YOUR DATE OF BIRTH : ")
  mobile = input("ENTER YOUR MOBILE NUMBER : ")
  user_info=(state,fname,name,dob,mobile)
