# This is the main.py module
import pandas as pd
import numpy as np
import random
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)
mycursor = mydb.cursor()

def create_acc():
    print("""
THIS IS ACCOUNT CREATION PAGE TO PROCEED TYPE y/Y, OR TO SKIP TYPE n/N
""")
    def create_acc2():
        con = input(">>> ").lower()
        while con == 'y':
            name = input("NAME: ")
            state = input("STATE NAME: ")
            emai = input("MAIL-ID: ")
            dob = input("DATE OF BIRTH: ")
            mob = input("MOBILE NUMBER: ")
            a=3
            try:
                mob = int(mob)
            except:
                a-=1
            while a not in [-1,3]:
                if a==0:
                    create_acc()
                else:
                    try:
                        mob = int(mob)
                    except:
                        print(f'\nERROR: INCORRECT MOBILE NUMBER\n\nYOU HAVE ONLY {a} MORE ATTEMPTS')
                        mob = input("RE-ENTER YOUR MOBILE NUMBER:\n>>> ")
                    a-=1
            #function to generate a new upi id
            def upi_gen(email):
                email_index = email.index("@")
                email_l = email[:email_index]
                formula = "select upi_id from acc_statement"
                mycursor.execute(formula)
                myresult = mycursor.fetchall()
                def gen_upii():
                    global gen_upi
                    gen_upi = email_l+str(random.randint(100,999))+"@okjstbnk"
                gen_upii()
                for i in myresult:
                    if i[0] == gen_upi:
                        gen_upii()
            upi_gen(emai)
            print(gen_upi)

            global acc_deta
            acc_deta = (name,gen_upi,state,emai,dob,mob)
            break
        else:
            print("DO YOU WANT TO PROCEED y/Y - CONTINUE, OR n/N - TO REVERT")
            while con in ['y','n']:
                if con == 'y':
                    break
                elif con == 'n':
                    create_acc2()
            else:
                print("INCORRECT INPUT!")

    create_acc2()
create_acc()
'''
#Modules
import transaction
transaction.init_tm()
'''