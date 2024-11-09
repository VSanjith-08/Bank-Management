import os
def title():
    def center_text(text, width):
        return text.center(width)
    terminal_width = os.get_terminal_size().columns
    design_before = center_text("=" * terminal_width, terminal_width)
    design_after = center_text("=" * terminal_width, terminal_width)
    w1 = "     _           _       ____              _    "
    w2 = "     | |_   _ ___| |_    | __ )  __ _ _ __ | | __ "
    w3 = " _  | | | | / __| __|   |  _ \\ / _` | '_ \\| |/ /"
    w4 = "| |_| | |_| \\__ \\ |_    | |_) | (_| | | | |   < "
    w5 = "  \\___/ \\__,_|___/\\__|   |____/ \\__,_|_| |_|_|\\_\\"
    print(design_before,end="")  
    print(center_text(w1, terminal_width))  
    print(center_text(w2, terminal_width)) 
    print(center_text(w3, terminal_width)) 
    print(center_text(w4, terminal_width)) 
    print(center_text(w5, terminal_width),'\n') 
    print(center_text("AN ONLINE BANKING SERVICE",terminal_width))
    print(design_after)
    
                                        
title()

import login
login.init_login()

# Funtion for money transaction _init_
if login.login:
    import init_mainmenu as _mainmenu_
    _mainmenu_.mainmenu()