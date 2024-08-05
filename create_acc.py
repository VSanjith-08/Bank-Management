# This is the main.py module
import pandas as pd
import numpy as np
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


def create_acc():
    print("\033[1;20;96m=\033[0m"*40)
    print("\033[1;20;96m|::: THIS IS ACCOUNT CREATION PAGE :::|\033[0m")
    print("\033[1;20;96m=\033[0m"*40,"\n")
    # A new function to ignore the above print statement
    def create_acc2():
        import login
        formula3 = f"select firstname,lastname,gender from login_details where uid = '{login.final_uid}'"
        mycursor.execute(formula3)
        myresult1 = mycursor.fetchall()
        if True:
            name = str((myresult1[0][0]+" "+myresult1[0][1]))
            state = input("STATE CODE (Eg: tn,ka,kl,etc): ").lower()
            emai = input("MAIL-ID: ").lower()

            #Checking is the entered email is right or wrong
            chkforat = False
            for i in emai:
                if i == '@':
                    chkforat = True
                    break
            while chkforat == False:
                print("\033[1;20;31m\n##### ERROR: INCORRECT EMAIL #####\n\033[0m")
                emai = input("mailid: ")
                for i in emai:
                    if i == '@':
                        chkforat = True
                        break
            dob = input("DATE OF BIRTH (yyyy-mm-dd) : ")
            mob = input("MOBILE NUMBER: ")
            # Checking is all the given characters in mobile number is a digit and of 10 digits
            a = 2
            while a != 0:
                def chk():
                    print("\033[1;20;31m\nERROR: INCORRECT MOBILE NUMBER\033[0m")
                    print("\033[1;20;31m\nYOU HAVE ONLY\033[0m",f'\033[1;20;33m{a}\033[0m','\033[1;20;31mMORE ATTEMPTS\033[0m')
                    global mo
                    mo = input("RE-ENTER YOUR MOBILE NUMBER:\n>>> ")
                                
                if len(mob) == 10:
                    for i in mob:
                        if i.isalpha():
                            chk()
                            break
                        else:
                            a = 1
                            break
                else:
                    chk()
                    mob = mo
                a-=1

            # If all the 3 chances are over for re-writing the mobile number
            if len(mob) == 10:
                for i in mob:
                    if i.isalpha():
                        quit()
                    else:
                        break
            else:
                quit()
                
            gender = str(myresult1[0][2])
            # If all the 3 chances are over for re-writing the mobile number
            if len(mob) == 10:
                for i in mob:
                    if i.isalpha():
                        create_acc()
                        break
                    else:
                        break
            else:
                create_acc()

            # Function to generate a new upi id
            def upi_gen(email):
                email_index = email.index("@")
                email_l = email[:email_index]
                formula = "select upi_id from acc_statement"
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
                formula = "select acc_no from acc_statement"
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
                formula = "select ifsc from acc_statement"
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

            import login                         
            global acc_deta
            acc_deta = (name,gen_upi,gen_accno,gen_ifsc,mob,gen_date,login.final_uid,state,dob,gender)
            acc_data = {"NAME":name,
                        'UPI ID':gen_upi,
                        'ACCOUNT NUMBER':gen_accno,
                        'IFSC CODE':gen_ifsc,
                        'ACCOUNT CREATED ON':gen_date
                        }
            global df_acc_data
            df_acc_data = pd.DataFrame([acc_data],index = [login.final_uid])
            formula1 = "insert into acc_statement (cu_name,upi_id,acc_no,ifsc,mobile_no,Date_of_opening,uid,state,dob,gender) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(formula1,acc_deta)
            mydb.commit()
        print(df_acc_data,'\n')

        print("\n"+"-"*39)
        print("+++++",end="")
        print("\033[1;20;33m ACCOUNT CREATION SUCCESSFUL \033[0m",end="")
        print("+++++")
        print("-"*39)

    create_acc2()

def init_create_acc():
    import login
    ui = login.final_uid
    formula2 = f"select uid from acc_statement where uid = '{ui}'"
    mycursor.execute(formula2)
    retrived_uid  = mycursor.fetchall()
    if login.lstatus:
        if len(retrived_uid)!=0:
            if ui not in retrived_uid[0]:
                global acc_created
                def confirmation():
                    inp_confirmation = input("TO PROCEED BY CREATING AN ACCOUNT (FULL ACCESS) PRESS- y/Y"+"\n"+" "*30+"(OR)"+"\n"+"TO PROCEED BY WITHOUT AN ACCOUNT (LIMITED ACCESS) PRESS- n/N"+"\n\n"+">>> ").lower()
                    print()
                    if inp_confirmation == "y":
                        create_acc()
                        acc_created = True
                    elif inp_confirmation == "n":
                        acc_created = False
                    else:
                        print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m")
                        confirmation()
                confirmation()
            else:
                pass
        elif len(retrived_uid)==0:
            global acc_created
            def confirmation():
                inp_confirmation = input("TO PROCEED BY CREATING AN ACCOUNT (FULL ACCESS) PRESS- y/Y"+"\n"+" "*30+"(OR)"+"\n"+"TO PROCEED BY WITHOUT AN ACCOUNT (LIMITED ACCESS) PRESS- n/N"+"\n\n"+">>> ").lower()
                print()
                if inp_confirmation == "y":
                    create_acc()
                    acc_created = True
                elif inp_confirmation == "n":
                    acc_created = False
                else:
                    print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m")
                    confirmation()
            confirmation()