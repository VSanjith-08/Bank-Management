import os

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
        def inp_confi():
            global inp_conf
            inp_conf = int(input(">>> "))
        inp_confi()
        
        if inp_conf in [1,2,3]:
            if inp_conf == 1:
                print()
                print("_"*os.get_terminal_size().columns)
                import Transaction
                Transaction.init_transfermoney()
            if inp_conf == 2:
                 print()
                 print("_"*os.get_terminal_size().columns)
                 import acc_services
                 acc_services.init_accser()
            if inp_conf == 3:
                print()
                print("_"*os.get_terminal_size().columns)
                import matplotlib_mod as statista
                statista.init_statista()
        else:
            print("\nERROR: WRONG INPUT!\nTRYAGAIN!\n")
            inp_confi()
terminal_width = os.get_terminal_size().columns
print("_"*terminal_width)