import mysql.connector
from admin import *
from customer import *
from datetime import date,timedelta 
mydb=mysql.connector.connect( 
    host='localhost',
    user='root',    
    password='',
    database='OnlineShopping'
)

cursor=mydb.cursor(buffered=True)

while True:
    print("**********WELCOME***********")
    print("____________________________________")
    who=input("Admin/or/Customer")
    if(who=="Admin" or who=="a"):
        ad=Admin(cursor,mydb)
        ad.admin_signin()
    
    elif(who=="Customer" or who=="c"):
    
        cus=Customer(cursor,mydb)
        sign=input("signin..or..Signup")
        if(sign=="signin"):
            cus.customer_signin()
        elif(sign=="signup"):
            cus.customer_signup()
        else:
            print("Invalid Entry")
    else:
        print("_______Invalid_______")