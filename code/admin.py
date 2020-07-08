from datetime import date,timedelta
class Admin:
    def __init__(self,cursor,mydb):
        self.cursor=cursor
        self.mydb=mydb
    
    def admin_product(self):
        print("____________________________________")
        print("__________ITEMS IN SHOP_____________")
        print("____________________________________")
        query="SELECT itemid,itemname,quantity,price FROM item"
        self.cursor.execute(query)
        lst=self.cursor.fetchall()   
        for item in lst:
            a,b,c,d=item
            print('+{} - {} - {}  -{}'.format(a,b,c,d))
        n=int(input('''choose the operation
        
                1.Add product
                2.Remove product
                3.back
                  '''))
        if(n==1):
            itemid=input("Enter item_id : ")
            itemname=input("Enter item_name : ")
            quantity=input("Enter no.of.quantity : ")
            price=input("Enter price : ")
            spec=input("Enter specification : ")
            query="INSERT INTO item(itemid, itemname, quantity, price, spec) VALUES (%s,%s,%s,%s,%s)"
            self.cursor.execute(query,(itemid,itemname,quantity,price,spec))
            self.mydb.commit()
            print("Added successfully........")
            self.adminhome()
        elif(n==2):
            itemid=input("Enter Remove item_id : ")
            query=("DELETE FROM item WHERE itemid=%s and itemid=%s")
            self.cursor.execute(query,(itemid,itemid))
            self.mydb.commit()
            print("Removed successfully......")
            self.adminhome()
        
        elif(n==3):
            self.adminhome()
        else:
            print("Invalid Entry")


    def admin_quantity(self):
        print('''
            1.Add quantity
            2.Remove quantity
            3.Back
            ''')
        ch=int(input("Enter your choice:"))
        if(ch==1):
            query="SELECT itemid,itemname,quantity FROM item"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()   
            for item in lst:
                a,b,c=item
                print('>{} - {} - {}'.format(a,b,c))

            itemid=input("Enter the item ID:")
            q="SELECT itemname FROM product WHERE itemid=%s and itemid=%s"
            self.cursor.execute(q,(itemid,itemid))
            i=self.cursor.fetchone()
            prod_name=i[0]
            choice=input('sure this ({}) product [yes/no]? '.format(prod_name))
            if(choice=='yes' or choice=='y'):
                aq=input("Enter the number of quantity:")
                query="UPDATE item SET quantity=quantity+%s WHERE itemid=%s"
                self.cursor.execute(query,(aq,itemid))
                self.mydb.commit()
                print(aq+" item added successfully")
                self.adminhome()
            elif(choice=='no' or choice=='n'):
                self.admin_quantity()

        elif(ch==2):
            query="SELECT item_id,item_name,quantity FROM product"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()   
            for item in lst:
                a,b,c=item
                print('+{} - {} - {}'.format(a,b,c))
            itemid=input("Enter the item ID:")
            q="SELECT itemname FROM product WHERE itemid=%s and itemid=%s"
            self.cursor.execute(q,(itemid,itemid))
            i=self.cursor.fetchone()
            prod_name=i[0]
            choice=input('sure this ({}) product [yes/no]? '.format(prod_name))
            if(choice=='yes' or choice=='y'):
                rq=input("Enter the number of quantity:")
                query="UPDATE item SET quantity=quantity-%s WHERE itemid=%s"
                self.cursor.execute(query,(rq,itemid))
                self.mydb.commit()
                print(rq+" item removed successfully")
                self.adminhome()
            elif(choice=='no' or choice=='n'):
                self.admin_quantity()
        elif(ch==3):
            self.adminhome()
        else:
            print("Invalid entry")
            self.adminhome()


    def admin_view(self):
        query="SELECT itemid,itemname,quantity FROM item"
        self.cursor.execute(query)
        lst=self.cursor.fetchall()   
        for item in lst:
            a,b,c=item
            print('+{} - {} - {}'.format(a,b,c))
        self.adminhome()

    def admin_view_custdata(self):
        query1="SELECT cust_id,name FROM customer"
        self.cursor.execute(query1)
        lst1=self.cursor.fetchall()
        for i in lst1:
            id,name=i
            print(">{} - {}".format(id,name))
        cust_id=input("Enter the customerID:")
        query2="SELECT name,phone_no,address FROM customer WHERE cust_id=%s and cust_id=%s"
        self.cursor.execute(query2,(cust_id,cust_id))
        lst2=self.cursor.fetchone()
        name,phone_no,address=lst2
        print("Name:",name)
        print("Phone Number:",phone_no)
        print("Address:",address)
        query3="SELECT itemid,quantity,Delivery_date FROM buyed_product WHERE cust_id=%s and cust_id=%s"
        self.cursor.execute(query3,(cust_id,cust_id))
        lst3=self.cursor.fetchall()
        for i in lst3:
            itemid,quantity,Delivery_date=i
            query4='SELECT itemname,price FROM item WHERE itemid=%s and itemid=%s'
            self.cursor.execute(query4,(itemid,itemid))
            lst4=self.cursor.fetchone()
            itemname,price=lst4
            print('Item Name:',itemname)
            print("quantity:",quantity)
            print("Total price:",quantity*price)
        
        
            


    def admin_signin(self):
        print("=======SIGNIN PAGE=======")
        name=input("Enter your name :")
        pwd=input("Enter your password :")
        query="select name,password from admin where name=%s and password=%s"
        self.cursor.execute(query,(name,pwd))
        val=self.cursor.fetchone()
        if(val==None):
            print("Wrong password")
        else:
            print("...........Success.........")
            self.adminhome()

    def adminhome(self):
        print("_____________Admin_____________")
        print('''
             1.make changes in product
             2.make changes in quantity
             3.View Products
             4.View Customer Data
             5.Logout

            ''' )
        choice=int(input("Enter your choice:"))
        if(choice==1):
            self.admin_product()
            self.adminhome()
        elif(choice==2):
            self.admin_quantity()
            self.adminhome()
        elif(choice==3):
            self.admin_view()
            self.adminhome()
        elif(choice==4):
            self.admin_view_custdata()
            self.adminhome()
        else:
            print("Invalid entry")
        
