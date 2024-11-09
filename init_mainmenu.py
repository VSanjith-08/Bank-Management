import os
terminal_width = os.get_terminal_size().columns

def mainmenu():
        print("\n"+"="*19)
        print("|::: MAIN MENU :::|")
        print("="*19)
        print('''
CHOOSE THE OPTION FROM THE FOLLOWING:
1 - TRANSFER MONEY
    (Via UPI,NET BANKING OR WALLET)
        
2 - ACCOUNT SERVICES
    (ACCOUNT STATEMENT, MINI STATEMENT, ACCOUNT BALENCE, Etc.)
              
3 - DEMOGRAPHICS
    (BAR PLOT AND LINE PLOT)
''')
        # Function to repeat the input if the user gives a wrong input
        inp_conf = int(input(">>> "))
        while inp_conf not in [1,2,3]:
            print("\nERROR: WRONG INPUT!\nTRYAGAIN!\n")
            inp_conf = int(input(">>> "))

        print("_"*terminal_width)
        if inp_conf == 1:
            print()
            import Transaction
            Transaction.init_transfermoney()
        if inp_conf == 2:
            print()
            import acc_services
            acc_services.init_accser()
        if inp_conf == 3:
            print()
            import matplotlib_mod as statista
            statista.init_statista()