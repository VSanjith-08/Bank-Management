# This is the Transaction module

import pandas as pd
import numpy as np
import random
from datetime import datetime
import mysql.connector

print("""
SELECT THE OPTIONS TO THEIR CORRESPONDING NUMBERS:
1 - TRANSFER MONEY
2 - DEPOSIT
3 - WITHDRAW
      """)

# 3 major functions for init

def trans_mon():
    print("""
CHOOSE YOUR TRANSACTION METHODS:
1 - UPI
2 - NET BANKING
3 - CREDIT/DEBIT CARDS
4 - MOBILE WALLETS
          """)
    init_trans()

# 4 functions under transfer money

def upi():
    print("Transaction methods 1")
def net_banking():
    print("Transaction methods 2")
def cards_tran():
    print("Transaction methods 3")
def mob_wallet():
    print("Transaction methods 4")

# init for transfer of money

def init_trans():
    opt = int(input(">>> "))
    while opt in [1,2,3,4]:
        if opt == 1:
            upi()
            break
        elif opt == 2:
            net_banking()
            break
        elif opt == 3:
            cards_tran()
            break
        elif opt == 4:
            mob_wallet()
            break
    else:
        print(" INCORRECT OPTION!\n TRY AGAIN")            
        init()

def deposit():
    print("hello world2")
def withdraw():
    print("hello world2")


# Starting init
def init():
    opt = int(input(">>> "))
    while opt in [1,2,3]:
        if opt == 1:
            trans_mon()
            break
        elif opt == 2:
            deposit()
            break
        elif opt == 3:
            withdraw()
            break
    else:
        print(" INCORRECT OPTION!\n TRY AGAIN")            
        init()

init()