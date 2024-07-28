# This is the main.py module
import pandas as pd
import numpy as np
import random
from datetime import datetime
import mysql.connector


def create_acc():
    print("""
THIS IS ACCOUNT CREATION PAGE TO PROCEED TYPE y/Y, OR TO SKIP TYPE n/N
""")
    def create_acc2():
        con = input(">>> ").lower()
        while con == 'y':
            f_name = input("ENTER YOUR FIRST NAME:\n>>> ")
            l_name = input("ENTER YOUR LAST NAME:\n>>> ")
            state = input("ENTER YOUR STATE NAME:\n>>> ")
            email = input("ENTER YOUR MAIL-ID:\n>>> ")
            dob = input("ENTER YOUR DATE OF BIRTH:\n>>> ")
            mob = input("ENTER YOUR MOBILE NUMBER:\n>>> ")
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

            global acc_deta
            acc_deta = (f_name,l_name,state,email,dob,mob)
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

#Modules
import transaction
transaction.init_tm()