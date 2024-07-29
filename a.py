import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)
mycursor = mydb.cursor()
#Add values into table
'''
mycursor.execute(formula,values)
'''
# Selecting and getting data
mycursor.execute("Select * from login_details")

myresult = mycursor.fetchall()
print(type(myresult))
