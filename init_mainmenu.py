import os

def mainmenu():
        print("\n"+"\033[1;20;34m=\033[0m"*19)
        print("\033[1;20;34m|::: MAIN MENU :::|\033[0m")
        print("\033[1;20;34m=\033[0m"*19)
        print('''
CHOOSE THE OPTION FROM THE FOLLOWING:
1 - TRANSFER MONEY
    (Via UPI,NET BANKING OR WALLET)
        
2 - ACCOUNT SERVICES
    (ACCOUNT STATEMENT, MINI STATEMENT, ACCOUNT BALENCE, Etc.)
''')
        # Function to repeat the input if the user gives a wrong input
        def inp_confi():
            global inp_conf
            inp_conf = int(input(">>> "))
        inp_confi()
        
        if inp_conf in [1,2]:
            if inp_conf == 1:
                print("_"*os.get_terminal_size().columns)
                import Transaction
                Transaction.init_transfermoney()
        else:
            print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m\n")
            inp_confi()