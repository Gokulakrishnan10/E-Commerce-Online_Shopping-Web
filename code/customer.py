from datetime import date,timedelta
class Customer:

    def __init__(self,cursor,mydb):
        self.cursor=cursor
        self.mydb=mydb
    def customer_signup(self):
        print("_________________________SIGNUP..PAGE__________________________")
        name=input("Enter your Name ")
        cust_id=input("Enter customer id ")
        phone_no=input("Enter phone Number ")
        password=input("Set Password ")
        address=input("Enter your Address ")

        query="INSERT INTO customer(Name,Cust_id,Phone_no,Password,Address) VALUES( %s,%s,%s,%s,%s)"
        self.cursor.execute(query,(name,cust_id,phone_no,password,address))
        self.mydb.commit()
        self.customerhome(cust_id,address)
        
    def customer_signin(self):
        print("=======SIGNIN PAGE=======")
        name=input("Enter your name :")
        pwd=input("Enter your password :")
        query="select name,password from customer where name=%s and password=%s"
        self.cursor.execute(query,(name,pwd))
        val=self.cursor.fetchone()
        query="SELECT cust_id FROM customer WHERE name=%s and password=%s"
        self.cursor.execute(query,(name,pwd))
        cus=self.cursor.fetchone()
        cust_id=cus[0]

        query="SELECT address FROM customer WHERE name=%s and password=%s"
        self.cursor.execute(query,(name,pwd))
        addd=self.cursor.fetchone()
        address=addd[0]
        if(val==None):
            print("Wrong password")
            self.customer_signin()
        else:
            print("...........Success.........")
            self.customerhome(cust_id,address)

    def customerhome(self,cust_id,address):

        

        print("____________________________________")
        print("1.Search_item 2.Display_item 3.my_cart 4.Buyed_Products 5.Logout")
        n=input("Choose the opereation ")
        print(n)
        if(n=="1"):
            print("_________________Search_item___________________")
            itemname=input("Enter item Name: ")
            query="SELECT itemid,itemname,price,spec,quantity FROM item WHERE itemname=%s and itemname=%s"  
            self.cursor.execute(query,(itemname,itemname)) 
            itm=self.cursor.fetchone()
            itemid,itemname,price,spec,quantity=itm
            print('{} - {}- Rs.{} - {} '.format(itemid,itemname,price,spec))
            
            
            print('''
            1.Buy
            2.Add to cart
            3.Back
            ''')
            ch=int(input("Enter your choice:"))
            if(ch==1):
                print("Available Quantity:",quantity)
                self.customer_buy(itemid,cust_id,address)
            elif(ch==2):
                self.customer_add_to_cart(itemid,cust_id,address)
                self.customerhome(cust_id,address)
            elif(ch==3):
                self.customerhome(cust_id,address)
            else:
                print("Invalid entry")
                self.customerhome(cust_id,address)

        elif(n=="2"):
            print("_________________Display_item___________________") 

            query="select itemid,itemname,price from item"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()
            print("itemid   itemname     price  ")
            for item in lst:
                a,b,c=item
                print('{}   --{}         --Rs{}  '.format(a,b,c))
            i_id=input("Enter the itemID going to buy:")
            query="SELECT itemname,spec,quantity FROM item where itemid=%s and itemid=%s"
            self.cursor.execute(query,(i_id,i_id))
            lst2=self.cursor.fetchone()
            a,b,quantity=lst2
            print("------------------------------------")
            print("Product name:",a)
            print("Specification:",b)
            print("------------------------------------")
            print('''
            1.Buy
            2.Add to cart
            3.Back
            ''')
            
            ch=int(input("Enter your choice:"))
            if(ch==1):
                print("Available Quantity:",quantity)
                self.customer_buy(i_id,cust_id,address)
            elif(ch==2):
                self.customer_add_to_cart(i_id,cust_id,address)
            elif(ch==3):
                self.customerhome(cust_id,address)
            else:
                print("Invalid entry")
                self.customerhome(cust_id,address)
        elif(n=="3"):
            print("------------------------------")
            print("         CART ITEM            ")
            print("------------------------------")
            query1="SELECT itemid FROM cart WHERE cust_id=%s and cust_id=%s"
            self.cursor.execute(query1,(cust_id,cust_id))
            lst=self.cursor.fetchall()
            query2="SELECT itemid,itemname,price FROM item WHERE itemid=%s and itemid=%s"
            for i in lst:
                self.cursor.execute(query2,(i[0],i[0]))
                l=self.cursor.fetchone()
                itemid,name,price=l
                print('>{}    -{}  - Rs.{}'.format(itemid,name,price))
            
            print('''1.Buy
                     2.Remove from cart
                     3.Back''')
            n=int(input("Enter your choice"))
            if(n==1):
                itemid=input("Enter item id Going to buy: ")
                self.customer_buy(itemid,cust_id,address)
            elif(n==2):
                itemid=input("Enter item id Going to Remove: ")
                self.customer_remove_from_cart(itemid,cust_id,address)
            elif(n==3):
                self.customerhome(cust_id,address)



        elif(n=="4"):
            
            
            print("________________Buyed_Products_________________")
            print("===============================================")
            query1="select itemid,quantity,status,ordered_date,delivery_date from buyed_product where cust_id=%s and cust_id=%s"
            self.cursor.execute(query1,(cust_id,cust_id))
            lst1=self.cursor.fetchall()   
            
            for i in lst1:
                itemid,quantity,status,ordered_date,delivery_date=i
                self.customer_status(itemid,cust_id,address)
                query2="select itemname,price,spec from item where itemid=%s and itemid=%s"
                self.cursor.execute(query2,(itemid,itemid))
                lst2=self.cursor.fetchone()
                itemname,price,spec=lst2
                print(">{}   Rs{}   {}   {}".format(itemname,price*quantity,spec,status))  
            
            self.customerhome(cust_id,address) 


        else:
            print("Invalid entry")
            

    def customer_buy(self,itemid,cust_id,address):

        quantity=int(input("Enter the quantity you want::"))
        Delivery_Date=date.today()+timedelta(7)
        ordered_date=date.today()
        query1="INSERT INTO buyed_product(cust_id,itemid,quantity,address,ordered_date,Delivery_Date) VALUES(%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(query1,(cust_id,itemid,quantity,address,ordered_date,Delivery_Date))
        self.mydb.commit()

        query4="update buyed_product SET status='Not Delivered' where itemid=%s and cust_id=%s"
        self.cursor.execute(query4,(itemid,cust_id))
        self.mydb.commit()
        
        query2="UPDATE item SET quantity=quantity-%s WHERE itemid=%s"
        self.cursor.execute(query2,(quantity,itemid))
        self.mydb.commit()

        query3="SELECT itemname,price FROM item WHERE itemid=%s and itemid=%s"
        self.cursor.execute(query3,(itemid,itemid))
        lst=self.cursor.fetchone()
        itemname,price=lst
        print("Item name:",itemname)
        print("Total price:",quantity*price)
        print("Delivery date:",Delivery_Date)
        self.customerhome(cust_id,address)

    def customer_add_to_cart(self,itemid,cust_id,address):
        query="INSERT INTO cart(itemid,cust_id) VALUES(%s,%s)"
        self.cursor.execute(query,(itemid,cust_id))
        self.mydb.commit()
        print("Item added to the cart....")
        self.customerhome(cust_id,address)
    
    def customer_remove_from_cart(self,itemid,cust_id,address):
        query="DELETE FROM cart WHERE itemid=%s and cust_id=%s"
        self.cursor.execute(query,(itemid,cust_id))
        self.mydb.commit()
        print("Item Removed from the cart....")
        self.customerhome(cust_id,address)

    def customer_status(self,itemid,cust_id,address):
        query1="select Delivery_date,ordered_date from buyed_product where itemid=%s and cust_id=%s"
        self.cursor.execute(query1,(itemid,cust_id))
        lst1=self.cursor.fetchone()
        Delivery_date,Ordered_date=lst1
        today=date.today()+timedelta(7)

        if(Delivery_date==today):
            query2="update buyed_product SET status='Delivered' where itemid=%s and cust_id=%s"
            self.cursor.execute(query2,(itemid,cust_id))
            self.mydb.commit()
            

        elif(today>Delivery_date):
            query3="update buyed_product SET status='Delivered' where itemid=%s and cust_id=%s"
            self.cursor.execute(query3,(itemid,cust_id))
            self.mydb.commit()
            

        else:
            query4="update buyed_product SET status='Not Delivered' where itemid=%s and cust_id=%s"
            self.cursor.execute(query4,(itemid,cust_id))
            self.mydb.commit()
        
    
