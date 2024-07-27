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

def trans_mon():
    print("hello world1")
def deposit():
    print("hello world2")
def withdraw():
    print("hello world2")


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