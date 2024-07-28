# This is the Transaction module

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
# 3 major functions for init [1-Transfer Money,2-Deposit,3-Withdraw]
print("""
SELECT THE OPTIONS TO THEIR CORRESPONDING NUMBERS:
1 - TRANSFER MONEY
2 - DEPOSIT
3 - WITHDRAW
      """)

# [1] Transfer money
def trans_mon():
    print("""
CHOOSE YOUR TRANSACTION METHODS:
1 - UPI
2 - NET BANKING
3 - CREDIT/DEBIT CARDS
4 - MOBILE WALLETS
          """)
    init_trans()

# 4 functions under transfer money {1-UPI,2-NET BANKING,3-CREDIT/DEBIT CARDS,4-MOBILE WALLETS}
# [1]{1} function of upi
def upi():
    upi_id_mob = input(">>> ENTER YOUR UPI ID/MOBILE: ")
    for i in upi_id_mob:
        if i.isdigit():
            int_bool = True
        else:
            int_bool = False
            break
    if int_bool:
        upi_id_mob = int(upi_id_mob)
    
    
# [1]{2} function of net banking
def net_banking():
    print("Transaction methods 2")
# [1]{3} function of cards transaction
def cards_tran():
    print("Transaction methods 3")
# [1]{4} functions of wallet
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
        init_tm()
### xxx ###

def deposit():
    print("hello world2")
def withdraw():
    print("hello world2")


# Starting init
def init_tm():
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
        print(" INCORRECT OPTION!\n TRY AGAIN!")            
        init_tm()

init_tm()