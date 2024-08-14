import os
def title():
    def center_text(text, width):
        return text.center(width)
    terminal_width = os.get_terminal_size().columns
    design_before = center_text("=" * terminal_width, terminal_width)
    design_after = center_text("=" * terminal_width, terminal_width)
    w1 = "\033[1;20;33m     _           _       ____              _    \033[0m"
    w2 = "\033[1;20;33m     | |_   _ ___| |_    | __ )  __ _ _ __ | | __ \033[0m"
    w3 = "\033[1;20;33m _  | | | | / __| __|   |  _ \\ / _` | '_ \\| |/ /\033[0m"
    w4 = "\033[1;20;33m| |_| | |_| \\__ \\ |_    | |_) | (_| | | | |   < \033[0m"
    w5 = "\033[1;20;33m  \\___/ \\__,_|___/\\__|   |____/ \\__,_|_| |_|_|\\_\\\033[0m"
    print(design_before,end="")  
    print(center_text(w1, terminal_width))  
    print(center_text(w2, terminal_width)) 
    print(center_text(w3, terminal_width)) 
    print(center_text(w4, terminal_width)) 
    print(center_text(w5, terminal_width),'\n') 
    print(center_text("\033[1;20;33mAN ONLINE BANKING SERVICE\033[0m",terminal_width))
    print(design_after)
    
                                        
title()

import login
login.init_login()

# Funtion for money transaction _init_

def main_menu():
    print("\n"+"\033[1;20;34m=\033[0m"*19)
    print("\033[1;20;34m|::: MAIN MENU :::|\033[0m")
    print("\033[1;20;34m=\033[0m"*19)
    print('''
CHOOSE THE OPTION FROM THE FOLLOWING:
1 - TRANSFER MONEY
    (DEPOSIT, WITHDRAWL)
          
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
            import upi
            upi.init_transfermoney()

    else:
        print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m\n")
        inp_confi()

main_menu()