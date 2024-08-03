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
    print(design_after)

title()

import login
login.init_login()

import create_acc
create_acc.init_create_acc()