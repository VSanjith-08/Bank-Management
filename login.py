# this is the login module
import numpy as np
import pandas as pd
import random
from datetime import datetime
import mysql.connector
import os

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)
mycursor = mydb.cursor()

login = False

def create_acc():
    print()
    print("="*32)
    print("|::: ACCOUNT CREATION PAGE :::|")
    print("="*32,"\n")
    # A new function to ignore the above print statement
    name = input("FULL NAME: ").upper()
    gender = input("GENDER: ").upper()
        
    def passwd():
        global n_passwd
        n_passwd = input("PASSWORD: ")
        caps,small,digit,space,spc = False,False,False,False,False
        for i in n_passwd:
            if i.isupper():
                caps = True
            if i.islower():
                small = True
            if i.isspace():
                space = True
            if i.isdigit():
                digit = True
            if [i.isdigit(),i.isalpha(),i.isspace()] == [False,False,False]:
                spc = True
        if [caps,small,digit,space,spc] != [True,True,True,False,True]:
            
            print("\nERROR: WRONG INPUT!")
            print("YOUR PASSWORD SHOULD HAVE ATLEAST ONE CAPITAL,SMALL,DIGIT,SPACE AND SPECIAL-CHARACTER.\n")
            passwd()
        else:
            repeat()
    def repeat():
        global c_passwd
        c_passwd = input("REPEAT PASSWORD: ")
        while n_passwd != c_passwd:
            print("\nERROR: PASSWORDS DOES NOT MATCH\n")
            passwd()
            break
    passwd()

    def uid():
        formula = "select uid from acc_details"
        mycursor.execute(formula)
        myresult = mycursor.fetchall()

        def gen_uiid():
            name_ws = ""
            for i in name:
                if i.isalpha():
                    name_ws += i

            global gn_uid
            ct = len(name_ws)
            if ct >= 7:
                nam = (name_ws)[:7]
                gn_uid = (nam+str(random.randint(100,999))).upper()
            else:
                gn_uid = (name_ws+str(random.randint(100,999))).upper()
        gen_uiid()
        for i in myresult:
            if i[0] == gn_uid:
                gen_uiid()
    uid()



    def create_acc2():
        if True:
            state = input("STATE CODE (Eg: tn,ka,kl,etc): ").lower()
            emai = input("MAIL-ID: ").lower()

            #Checking is the entered email is right or wrong
            chkforat = False
            for i in emai:
                if i == '@':
                    chkforat = True
                    break
            while chkforat == False:
                print("\n##### ERROR: INCORRECT EMAIL #####\n")
                emai = input("mailid: ")
                for i in emai:
                    if i == '@':
                        chkforat = True
                        break
            dob = input("DATE OF BIRTH (yyyy-mm-dd) : ")

            def upi_gen(email):
                email_index = email.index("@")
                email_l = email[:email_index]
                formula = "select upi_id from acc_details"
                mycursor.execute(formula)
                myresult = mycursor.fetchall()
                def gen_upii():
                    global gen_upi
                    gen_upi = email_l+str(random.randint(100,999))+"@okjstbnk"
                gen_upii()
                for i in myresult:
                    if i[0] == gen_upi:
                        gen_upii()
            upi_gen(emai)

            # Function to generate a new account number
            def accno_gen():
                formula = "select acc_no from acc_details"
                mycursor.execute(formula)
                myresult = mycursor.fetchall()
                def gen_acc_no():
                    global gen_accno
                    gen_accno = random.randint(1000000,9999999)
                gen_acc_no()
                for i in myresult:
                    if i[0] == gen_accno:
                        gen_acc_no()
            accno_gen()

            # Function to generate date of opening the date
            def date_gen():
                global gen_date
                gen_date=datetime.date(datetime.now())
            date_gen()

            # Function to generate IFSC code
            def ifsc_gen():
                formula = "select ifsc from acc_details"
                # dictionary of branches of our bank
                dict_state = {
                    "ap": pd.Series(["Visakhapatnam", "Vijayawada"]),
                    "ar": pd.Series(["Itanagar", "Tawang"]),
                    "as": pd.Series(["Guwahati", "Dibrugarh"]),
                    "br": pd.Series(["Patna", "Gaya"]),
                    "cg": pd.Series(["Raipur", "Bilaspur"]),
                    "ga": pd.Series(["Panaji", "Margao"]),
                    "gj": pd.Series(["Ahmedabad", "Surat"]),
                    "hr": pd.Series(["Gurugram", "Faridabad"]),
                    "hp": pd.Series(["Shimla", "Dharamshala"]),
                    "jh": pd.Series(["Ranchi", "Jamshedpur"]),
                    "ka": pd.Series(["Bengaluru", "Mysuru"]),
                    "kl": pd.Series(["Thiruvananthapuram", "Kochi"]),
                    "mp": pd.Series(["Bhopal", "Indore"]),
                    "mh": pd.Series(["Mumbai", "Pune"]),
                    "mn": pd.Series(["Imphal", "Churachandpur"]),
                    "ml": pd.Series(["Shillong", "Tura"]),
                    "mz": pd.Series(["Aizawl", "Lunglei"]),
                    "nl": pd.Series(["Kohima", "Dimapur"]),
                    "od": pd.Series(["Bhubaneswar", "Cuttack"]),
                    "pb": pd.Series(["Ludhiana", "Amritsar"]),
                    "rj": pd.Series(["Jaipur", "Udaipur"]),
                    "sk": pd.Series(["Gangtok", "Namchi"]),
                    "tn": pd.Series(["Chennai", "Coimbatore","Madurai","Tiruchirappalli"]),
                    "ts": pd.Series(["Hyderabad", "Warangal"]),
                    "tr": pd.Series(["Agartala", "Udaipur"]),
                    "up": pd.Series(["Lucknow", "Kanpur"]),
                    "uk": pd.Series(["Dehradun", "Haridwar"]),
                    "wb": pd.Series(["Kolkata", "Darjeeling"])
                }
                # Creating a dictionary of ifsc codes for each branch

                dict_branch = {
                    "Chennai": "JSTBNK01",
                    "Coimbatore": "JSTBNK02",
                    "Itanagar": "JSTBNK03",
                    "Tawang": "JSTBNK04",
                    "Guwahati": "JSTBNK05",
                    "Dibrugarh": "JSTBNK06",
                    "Patna": "JSTBNK07",
                    "Gaya": "JSTBNK08",
                    "Raipur": "JSTBNK09",
                    "Bilaspur": "JSTBNK10",
                    "Panaji": "JSTBNK11",
                    "Margao": "JSTBNK12",
                    "Ahmedabad": "JSTBNK13",
                    "Surat": "JSTBNK14",
                    "Gurugram": "JSTBNK15",
                    "Faridabad": "JSTBNK16",
                    "Shimla": "JSTBNK17",
                    "Dharamshala": "JSTBNK18",
                    "Ranchi": "JSTBNK19",
                    "Jamshedpur": "JSTBNK20",
                    "Bengaluru": "JSTBNK21",
                    "Mysuru": "JSTBNK22",
                    "Thiruvananthapuram": "JSTBNK23",
                    "Kochi": "JSTBNK24",
                    "Bhopal": "JSTBNK25",
                    "Indore": "JSTBNK26",
                    "Mumbai": "JSTBNK27",
                    "Pune": "JSTBNK28",
                    "Imphal": "JSTBNK29",
                    "Churachandpur": "JSTBNK30",
                    "Shillong": "JSTBNK31",
                    "Tura": "JSTBNK32",
                    "Aizawl": "JSTBNK33",
                    "Lunglei": "JSTBNK34",
                    "Kohima": "JSTBNK35",
                    "Dimapur": "JSTBNK36",
                    "Bhubaneswar": "JSTBNK37",
                    "Cuttack": "JSTBNK38",
                    "Ludhiana": "JSTBNK39",
                    "Amritsar": "JSTBNK40",
                    "Jaipur": "JSTBNK41",
                    "Udaipur": "JSTBNK42",
                    "Gangtok": "JSTBNK43",
                    "Namchi": "JSTBNK44",
                    "Visakhapatnam": "JSTBNK45",
                    "Vijayawada": "JSTBNK46",
                    "Hyderabad": "JSTBNK47",
                    "Warangal": "JSTBNK48",
                    "Agartala": "JSTBNK49",
                    "Udaipur": "JSTBNK50",
                    "Lucknow": "JSTBNK51",
                    "Kanpur": "JSTBNK52",
                    "Dehradun": "JSTBNK53",
                    "Haridwar": "JSTBNK54",
                    "Kolkata": "JSTBNK55",
                    "Darjeeling": "JSTBNK56",
                    "Madurai":"JSTBNK57",
                    "Tiruchirappalli":"JSTBNK58"
                }

                df_state = pd.DataFrame(dict_state,index=[0,1,2,3])

                access_state = np.array(df_state[state])

                print("\nCHOOSE YOUR BANK BRANCH NEARBY:\n")
                increment = 1
                for i in access_state:
                    if pd.notna(i)==False:
                        break
                    print(increment,end=" - ")
                    print(i.upper())
                    increment+=1
                print()
                bnk_branch = int(input(">>> "))
                
                global gen_ifsc
                gen_ifsc = dict_branch[access_state[bnk_branch-1]]

            ifsc_gen()

            acc_deta = (name,gen_upi,gen_accno,gen_ifsc,gen_date,gn_uid,state,dob,gender,c_passwd)
            acc_data = {"NAME":name,
                        'UPI ID':gen_upi,
                        'ACCOUNT NUMBER':gen_accno,
                        'IFSC CODE':gen_ifsc,
                        'ACCOUNT CREATED ON':gen_date
                        }
            global df_acc_data
            df_acc_data = pd.DataFrame([acc_data],index = [gn_uid])
            formula1 = "insert into acc_details (cu_name,upi_id,acc_no,ifsc,Date_of_opening,uid,state,dob,gender,passwd) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(formula1,acc_deta)
            mydb.commit()

            print("\n##### YOU'RE NEWLY GENERATED USER ID:#####",f"{gn_uid},#####")
            print("\n##### PASSWORD:",f"{c_passwd}"+" #####\n")
        print(df_acc_data,'\n')
        
        print("\n"+"-"*40)
        print("+++++",end="")
        print(" ACCOUNT CREATION SUCCESSFULL ",end="")
        print("+++++")
        print("-"*40)
        terminal_width = os.get_terminal_size().columns
        print("_"*terminal_width,"\n")

    create_acc2()
    signin()

def signin():
    
    print("\n"+"="*22)
    print("|::: SIGN-IN PAGE :::|")
    print("="*22,"\n")

    formula = f"select uid from acc_details"
    mycursor.execute(formula)
    retrived_uid = mycursor.fetchall()

    arr_retrived_uid = np.array([])
    for i in retrived_uid:
        arr_retrived_uid = np.concatenate((arr_retrived_uid,np.array([i[0]])))
    
    formula1 = f"select passwd from acc_details"
    mycursor.execute(formula1)
    retrived_passwd = mycursor.fetchall()
    
    arr_retrived_passwd = np.array([])
    for i in retrived_passwd:
        arr_retrived_passwd = np.concatenate((arr_retrived_passwd,np.array([i[0]])))
    global uid_pass
    uid_pass = False
    global passwd_pass
    passwd_pass = False
    global inp_uid
    inp_uid = input("UID: ")
    if inp_uid in arr_retrived_uid:
        uid_pass = True
    else:
        i = 2
        while uid_pass == False:
            if i != 0:
                print("\n### ERROR: INCORRECT UID ###")
                inp_uid = input(f"YOU HAVE {i} MORE CHANCE\n\nRE-ENTER UID: ")
                if inp_uid in arr_retrived_uid:
                    uid_pass = True
            else:
                print("\n### ####### ###\nYOU'RE GIVEN INPUTS ARE OVER\n\nTHANK YOU!\n")
                quit()
            i-=1

    print()
    global inp_passwd
    inp_passwd = input("PASSWORD: ")
    if inp_passwd in arr_retrived_passwd:
        passwd_pass = True
    else:
        i = 2
        while passwd_pass == False:
            if i != 0:
                print("\n### ERROR: INCORRECT PASSWORD ###")
                inp_passwd = input(f"YOU HAVE {i} MORE CHANCE\n\nRE-ENTER PASSWORD: ")
                if inp_passwd in arr_retrived_passwd:
                    passwd_pass = True
            else:
                print("\n### ####### ###\nYOU'RE GIVEN INPUTS ARE OVER\n\nTHANK YOU!\n")
                quit()
            i-=1
    print("\n"+"-"*34)
    print("+++++",end="")
    print(" SUCCESSFULLY SIGNED-IN ",end="")
    print("+++++")
    print("-"*34)
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    global login
    login = True

def admin():
    print("this is admin module")


#starting init
def init_login():
    print("""
CHOOSE THE OPTION FROM THE FOLLOWING:
1 - SIGN IN
2 - REGISTER
3 - ADMIN
          """)
    opt = int(input(">>> "))
    while opt in [1,2,3]:
        if opt == 2:
            create_acc()
            break
        elif opt == 1:
            signin()
            break
        elif opt == 3:
            admin()
            break
    else:
        print("\nERROR: WRONG INPUT!\nTRYAGAIN!")         
        init_login()
        