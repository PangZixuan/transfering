import sqlite3
import time
import datetime
import sys

conn = None
c = None
quit= False
aid= None
cid=None
cart=[]
qtyinfo=[]
storeinfo=[]
pidinfo=[]
sidinfo=[]

def connect(path):
    global conn, c

    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(' PRAGMA forteign_keys=ON; ')
    conn.commit()
    return

def is_valid_id(cora,cid):
    if cora=="c":
        c.execute('SELECT cid FROM customers WHERE cid=?;',(cid,))
    if cora=="a":
        c.execute('SELECT aid FROM agents WHERE aid=?;',(aid,))
    if c.fetchone() != None:
        return True
    else:
        return False
    
    
def correct_pwd(cora,cid,pwd):
    if cora=="c":
        c.execute('SELECT pwd FROM customers WHERE cid=? AND pwd=?',(cid,pwd))
    if cora=="a":
        c.execute('SELECT pwd FROM agents WHERE aid=? AND pwd=?',(aid,pwd))
    if c.fetchone() != None:
        return True
    else:
        return False
    
def takeSecond(elem):
    return elem[1]

def printFive(order,x,y):
    for i in range(x,y):
        #find id, name, unit, category
        oneProduct = []
        p_name = order[i][0]
        c.execute("SELECT p1.pid, p1.name, p1.unit, c1.name FROM products p1, categories c1 WHERE p1.name = ? AND p1.cat = c1.cat;",(p_name,))
        inuc = c.fetchone()
        for j in range(len(inuc)):
            oneProduct.append(inuc[j])
        
        #find number of stores that carry it
        c.execute ("SELECT count(*) FROM carries c, products p WHERE p.name = ? AND p.pid = c.pid;", (p_name,))
        count = c.fetchone()
        oneProduct.append(count[0])
        
        #find number of stores that have it in stock
        c.execute ("SELECT count(*) FROM carries c, products p WHERE c.pid = p.pid AND p.name = ?AND c.qty>0;", (p_name,))
        count = c.fetchone()
        oneProduct.append(count[0])
        
        #find minimum price tag among the stores that carry it
        c.execute ("SELECT min(c.uprice) FROM carries c, products p WHERE p.name = ? AND p.pid = c.pid;", (p_name,))
        minPrice = c.fetchone()
        oneProduct.append(minPrice[0])
        
        #find minimum price tag among the stores that have it in stock
        c.execute ("SELECT min(c.uprice) FROM carries c, products p WHERE c.pid = p.pid AND p.name = ?AND c.qty>0;", (p_name,))
        minPrice = c.fetchone()
        oneProduct.append(minPrice[0])
        
        #find the number of orders within the past 7 days
        #c.execute ("SELECT count(*) FROM olines ol, orders or, products p WHERE p.name = ? AND p.pid = ol.pid AND ol.oid = or.oid AND or.odate >= datetime('now','-7');", (p_name,))
        #orDate = c.fetchone()
        #oneProduct.append(orDate[0])
        
        print(oneProduct)    

def productDetail(prodName):
    global conn,c,cid,cart,qtyinfo,storeinfo
    #id,name,unit,category
    c.execute("SELECT p1.pid, p1.name, p1.unit, c1.name FROM products p1, categories c1 WHERE p1.name = ? AND p1.cat = c1.cat;",(prodName,))
    inuc = c.fetchone()
    if inuc != None:
        print("Product ID is: "+inuc[0])
        print("Product Name is: "+inuc[1])
        print("Product unit is: "+inuc[2])
        print("Product cateogrty name is: "+inuc[3])
        #current_date = time.strftime("%Y-%m-%d %H:%M:%S")
        weekago=datetime.datetime.now() - datetime.timedelta(days=8)
        c.execute("SELECT o.oid FROM orders o,olines ol  WHERE o.oid=ol.oid AND ol.pid=? AND o.odate>?",(inuc[0],weekago))
        weekorders=c.fetchall()
        print("numbers of order : ",len(weekorders))
    
    #check all stores that have this item in stock
        c.execute("SELECT s.name, c.uprice, c.qty FROM carries c, stores s, products p WHERE c.sid = s.sid AND c.pid = p.pid AND p.name = ? AND c.qty>0 ORDER BY c.uprice;",(prodName,))
        storec = c.fetchall()
        if storec != []:
            print("Here are all the stores that have this product in stock as well as their price tags for this item.")
            for i in range(len(storec)):
                print("Store ",storec[i][0]," has ",storec[i][2]," instock at a price of",storec[i][1])
        else :
            print("Sorry this item is out of stock everywhere!")
    
    #check all stores that carry this item
        c.execute("SELECT s.name, c.uprice FROM carries c, stores s, products p WHERE c.sid = s.sid AND c.pid = p.pid AND p.name = ? AND c.qty=0 ORDER BY c.uprice;",(prodName,))
        storeS = c.fetchall()
        if storeS != []:
            print("Here are the store that carry this item but don't have them in stock as well as their price tags for this item.")
            for i in range(len(storeS)):
                print(storeS[0])
                
        putin = input("Do you want to add the item to your basket?(Y/N)")
        handle_error(putin)
        #if cart.lower() == 'n':
           # customer_func(cid)
        if putin.lower() == 'y':
            pstore=input("Which store do you want to purches from? :")
            handle_error(pstore)
            qty=int(input("How many do you want to add to your cart? "))
            handle_error(qty)
            cart.append(prodName)
            qtyinfo.append(qty)
            storeinfo.append(pstore)
            print("Product: ",prodName,"at Store ",pstore," Added to cart!")
            c.execute("SELECT p.pid FROM products p WHERE name = ?",(prodName,))
            pid=c.fetchone()[0]
            pidinfo.append(pid)
            c.execute('SELECT c.sid FROM carries c,stores s WHERE c.sid=s.sid AND name=?',(pstore,))
            sid=c.fetchone()[0]
            sidinfo.append(sid)
            c.execute('UPDATE carries SET qty= qty-? WHERE sid=? AND pid=?',(qty,sid,pid))
    else:
        print("wrong product name!")
def handle_error(whatever):
    global conn,c,quit
    if whatever=="quit!":
        quit==True
        cart=[]
        qtyinfo=[]
        storeinfo=[]
        pidinfo=[]
        sidinfo=[]        
        print("Exiting....")
        time.sleep(1)
        conn.close()
        print("Exitted!")
        sys.exit(0)
    elif whatever=="logout!":
        cart=[]
        qtyinfo=[]
        storeinfo=[]
        pidinfo=[]
        sidinfo=[]       
        main()
        
def registy():
    global conn,c
    valid=False
    name=input("Enter your name: ")
    while not valid :
        newid=input("Please enter a cid :")
        c.execute('SELECT cid FROM customers WHERE cid=?',(newid,))
        exist=c.fetchone()
        if exist == None:
            pwd=input("Please enter a password: ")
            address=input("To register as a customer, we need your address.  Enter your address: ")
            valid=True
            c.execute('INSERT INTO customers VALUES (?,?,?,?)',(newid,name,address,pwd))
            conn.commit()
            print("Successfully registered! Please LOGIN now.")
        else:
            print("Entered id exists, try another one!")



############################################################################################################################
    #handle customer functions            
def customer_func(cid):
    global conn, c,quit,cart,qtyinfo
    cmd = input("What do you want to do?\n ENTER||SEARCH to search for a product||PLACE o place an order||LIST to see all your orders :")
    ##########################################################################
    #SEARCH entered
    if cmd == "SEARCH":
        objektz=None
        while objektz == None:
            objektz = input ("What are you searching for?")
            handle_error(objektz)
        objektz=objektz.split(' ')
        order = []
        for i in range(len(objektz)):
            obj = objektz[i]
            obj = "%"+obj+"%"
            c.execute("SELECT * FROM products WHERE products.name LIKE ?",(obj.lower(),))
            obj = c.fetchall()
            if len(obj)>0:
                for x in range(len(obj)):
                    if len(order) == 0:
                        newItem = [obj[x][1],1]
                        order.append(newItem)
                    else:
                        exists = 0
                        for j in range(len(order)):
                            if obj[x][1] == order[j][0]:
                                order[j][1]+=1
                                exists = 1
                                break
                        if exists != 1:
                            obj[x][1]!=order[j][0]
                            newItem = [obj[x][1],1]
                            order.append(newItem)
        order.sort(reverse = True, key = takeSecond)
        if len(order)<=5:
            printFive(order,0,len(order))
            pressN = input ("Type in specific item name for details. (case and space sensitive)")
            handle_error(pressN)
        elif len(order)>5:
            printFive(order,0,5)
            pressN = input("Type N to go to next page ||Type in specific item for details. (case and space sensitive) ")
            handle_error(pressN)
            inc1 = 0
            inc2 = 5
            incMul =0
            while pressN.lower() == 'n':
                incMul+=1
                if inc2+5*incMul <= len(order):
                    printFive(order,inc1+5*incMul,inc2+5*incMul)
                    pressN = input("Type N to go to next page ||Type in specific item for details. (case  and space sensitive) ")
                    handle_error(pressN)
                elif inc2+5*incMul > len(order):
                    printFive(order, inc1+5*incMul, len(order))
                    pressN = input("End of list, type in sepcific itme for details. (case and space sensitive)")
                    handle_error(pressN)
                    break
        productDetail(pressN)
        #search orders
     
    ####################################################
    #PLACE entered 
    elif cmd == "PLACE":
        if len(cart)==0:
            print("Nothing to place, you have nothing in your cart!")
        else:
            print("you have ",len(cart),"items in your cart.")
            seecart=input("Do you want to see what is(are) in it? (Y/N):")
            if seecart=="Y":
                print(cart)
            
            #c.execute("SELECT name FROM products")
           # productlist=c.fetchall()
            #for product in productlist:
               # print(product[0])
            #print all products
            finished=False
           # cart=[]
            #pidinfo=[]
            #sidinfo=[]
            #qtyinfo=[]
            while not finished:
                finished=True
                placeready=input("Do you want to place the order for all your products in cart?(Y/N): ")
                if placeready=="Y":
                    for item in cart:
                        index=cart.index(item)
                        wantqty=qtyinfo[index]
                        sid=sidinfo[index]
                        pid=pidinfo[index]
                        c.execute('SELECT s.name, c.qty FROM stores s,carries c,products p WHERE s.sid=c.sid AND c.sid=? AND p.pid=c.pid AND c.pid=? AND c.qty<0',(sid,pid))
                        storelist=c.fetchone()
                        if storelist!=None:
                            finished=False
                            pstore=storelist[0]
                            print(item," IS OUT OFF STOCK IN STORE ",pstore)
                            ifchange=input("Make change on its quantities? (Y/N) || Or Enter DELETE to delete item from your cart: ")
                            if ifchange=="Y":
                                stockqty=(storelist[1]+wantqty)
                                print("Your store ",pstore," has ",stockqty," in stock.")
                                print("You have ",wantqty," in your cart.")
                                qtyinfo[index]=int(input('Enter the quantity you want change it to: '))
                                while qtyinfo[index] > stockqty:
                                    print("Still too many(much),Try lower!")
                                    qtyinfo[index]=int(input('Enter the quantity you want change it to: '))
                                diff=wantqty-qtyinfo[index]
                                c.execute('UPDATE carries SET qty= qty+? WHERE sid=? AND pid=?',(diff,sid,pid))                            
                            elif ifchange=="DELETE" or qtyinfo[index]==0:
                                cart.remove(item)
                                qtyinfo.pop(index)
                                sidinfo.pop(index)
                                pidinfo.pop(index)
                                storeinfo.pop(index)
                                c.execute('UPDATE carries SET qty= qty+? WHERE sid=? AND pid=?',(qtyinfo[index],sid,pid))  
                                print("item Deleted!")
                            elif ifchange=="N":
                                print("order will not be placed")
                                break
                        else:
                            print(item," instock, and ready to be placed")
                elif placeready=="N":
                    finished=False
                    break
                else:
                    handle_error(placeready)
            if finished:
                c.execute('SELECT MAX(oid) FROM orders;')
                disoid=c.fetchone()
                disoid=int(disoid[0])+1
                current_date = time.strftime("%Y-%m-%d %H:%M:%S")
                c.execute('SELECT address FROM customers WHERE cid=?',(cid,))
                address=c.fetchone()[0]
                c.execute('INSERT INTO orders VALUES (?,?,?,?)',(disoid,cid,current_date,address))
                conn.commit()   
                print("your oder id is: ",disoid)
                for item in range(0,len(cart)):
                    pid=pidinfo[item]
                    sid=sidinfo[item]
                    wantqty=qtyinfo[item]
                    c.execute('SELECT uprice FROM carries WHERE pid=? AND sid=?',(pid,sid))
                    uprice=c.fetchone()[0]            
                    c.execute('INSERT INTO olines VALUES(?,?,?,?,?)',(disoid,sid,pid,wantqty,uprice))
                conn.commit()    
                print("All your orders have been placed!!   Your oid is: ",disoid)
                #wantedproduct=input("Enter the product you want to order:")
                #handle_error(wantedproduct)
                #wantqty=input("How many/much do you want? ")
                #handle_error(wantqty)  
                #c.execute('SELECT s.name,c.qty FROM stores s,carries c,products p WHERE s.sid=c.sid AND p.name=? AND p.pid=c.pid AND c.qty>=?',(wantedproduct,wantqty))
                #storelist=c.fetchall()
                #if storelist==[]:
                    #print("OUT OFF STOCK IN ALL STORES! ")
                    #continue
               # else:
                    #for row in range(0,len(storelist)):
                      #  print("store ",storelist[row][0]," has ",storelist[row][1]," in stock")
                   # pstore=input("Which store do you want purches from? :")
                    #handle_error(pstore)            
                #c.execute("SELECT p.name, p.pid FROM products p, carries c WHERE name = :nam AND p.pid==c.pid AND c.qty>= :qtii",{"nam":wantedproduct,"qtii":wantqty})
                #orderp=c.fetchone()
                #if orderp==None:
                 #   print("Product", wantedproduct ,"NOT enough in stock at ",pstore,"(or store name had a spelling mistake)Please try again! ")
               # else:
                  #  cart.append(orderp[0])
                 #   pid=orderp[1]
                  #  pidinfo.append(pid)
                  #  c.execute('SELECT sid FROM stores WHERE name=?',(pstore,))
                  #  sid=c.fetchone()[0]
                   # sidinfo.append(sid)
                    #qtyinfo.append(wantqty)
                    #c.execute('UPDATE carries SET qty=qty-? WHERE sid=? AND pid=?',(wantqty,sid,pid))
                    #print("added to cart!")
                    #goodtogo=input("Continue Shopping?(Y/N)?")
                    #handle_error(goodtogo)               
                    #if goodtogo=="N":
                    #    finished=True
    
                #place the order
           # c.execute('SELECT uprice FROM carries WHERE pid=? AND sid=?',(pid,sid))
           # uprice=c.fetchone()[0]
            
            
  #########################################          
            
    #LIST entered 
    elif cmd == "LIST":
        c.execute('SELECT * FROM orders WHERE cid=?',(cid,))
        ifempty=c.fetchone()
        if ifempty==None:
            print("No order has been found")
        else:
            order_to_show=None
            c.execute('SELECT ol.oid,o.odate,ol.qty,ol.uprice*ol.qty FROM orders o, olines ol WHERE o.cid=? AND o.oid=ol.oid ORDER BY o.odate DESC',(cid,))
            order_to_show=c.fetchall()
            pricelist=[]
            for row in range(0,len(order_to_show)):
                price=order_to_show[row][3]
                price=round(price,2)
                pricelist.append(price)
            i=0
            contin="Y"
            while contin=="Y" and i < len(order_to_show):
                for row in range (i,i+5):
                    if row < (len(order_to_show)):
                        print("oid: ",order_to_show[row][0]," oder date: ",order_to_show[row][1]," quantity and total price: ",order_to_show[row][2],pricelist[row])
                    else:
                        break
                i=i+5
                if i>=len(order_to_show):
                    break                
                contin=input("Show more? (Y/N) :")
                handle_error(contin)
            showinfo=input("Enter an oid to learn more: Or enter 'N' to go back to main manue: ")
            if showinfo != "N":
                handle_error(showinfo)
                showinfo=int(showinfo)
                print(showinfo)
                c.execute('SELECT * FROM deliveries WHERE oid=?',(showinfo,))
                dprinter=c.fetchone()
                c.execute('SELECT address FROM orders WHERE oid=?',(showinfo,))
                adprinter=c.fetchone()[0]
                c.execute('SELECT s.sid, s.name, p.pid, p.name,ol.qty,ol.uprice,p.unit FROM stores s,products p, olines ol WHERE ol.oid=? AND ol.sid=s.sid AND ol.pid=p.pid',(showinfo,))
                iprinter=c.fetchall()
                print("Order id:",showinfo," will be delivered to ",adprinter)
                if dprinter==None:
                    print("Diliver Not set up" )
                else:
                    print("Delivery information: Tracking NO:",dprinter[0]," And pick up time:",dprinter[2]," And drop off time:",dprinter[3])
                print("Order info Below:")
                for row in range(0,len(iprinter)):
                    print("Store info:",iprinter[row][0],iprinter[row][1]," Product info: ",iprinter[row][2],iprinter[row][3]," qty: ",iprinter[row][4]," unit&price: ",iprinter[row][6],iprinter[row][5])
                
    else:
        handle_error(cmd)
        print("WRONG Commanda Given !!")

##########################################################################################################################################
#handld agent functions

def agent_func(aid):
    global conn, c
    cmd = input("What do you want to do?\n ENTER||SETUP to set up a delivery||UPDATE to update a delivery||ADD ti add stock to a store: ")
    #handle_error(cmd)
    if cmd == "SETUP":
        #setuphandle_error(cmd)
        tknum=None
        c.execute('SELECT MAX(trackingNo) FROM deliveries')
        tknum=c.fetchone()[0]+1
        print("New trackingNo generated :",tknum)
        finish="Y"
        oid_list=[]
        while finish=="Y":
            order=input("Enter an oid to add the order to the diliver. :")
            handle_error(order)
            oid_list.append(order)
            finish=input("Want to add another oid to the same diliver?(Y/N) \n Remember thet your oid entered has to be from one same customer\n since I'm not told to handle this erorr and I'm lazy:")
            handle_error(finish)
        print(len(oid_list)," orders have been added to diliver.  TrackingNo : ",tknum)
        settime=input("Set Up a Pick up time? (Y/N) :")
        handle_error(settime)
        dilidate=None
        if settime=="Y":
            piktime=input("Enter the pick up time as format of yyyy-mm-dd. : ")
            handle_error(piktime)
            year,month,day=map(int,piktime.split('-'))
            dilidate=datetime.date(year,month,day)
            #print(dilidate)
        for orders in oid_list:
            oid=orders
            c.execute('INSERT INTO deliveries VALUES (?,?,?,?)',(tknum,oid,dilidate,None))
            conn.commit()
            
       
    elif cmd == "UPDATE":
        #update
        tknum=input("Enter a tracking number: ")
        c.execute('SELECT d.trackingNo, d.oid,d.pickUpTime,d.dropOffTime FROM deliveries d Where d.trackingNo=?',(tknum,))
        dinfo=c.fetchall()
        piktime=dinfo[0][2]
        drptime=dinfo[0][3]
        oid_list=[]
        for row in range(0,len(dinfo)):
            oid=dinfo[row][1]
            oid_list.append(oid)
        print("Tracking number: ",tknum,"has ",len(oid_list)," orders with pick up time: ",piktime," and drop off time: ",drptime,".")
        print("Order ids are:")
        for item in oid_list:
            print(item)
        todo=input("What to do with it? Enter|'UPDATE' to edit pick up time or drop off time |'DELETE' to delete a delivery")
        if todo=="UPDATE":
            picktime=input("Enter new PICK UP date in the format of yyyy-mm-dd OR enter 'N' to keep the old pick up time: ")
            handle_error(picktime)
            if picktime!="N":
                year,month,day=map(int,picktime.split('-'))
                piktime=datetime.date(year,month,day)
                print("pick up time updated")
                c.execute('UPDATE deliveries SET pickUpTime=? WHERE trackingNo=? ',(piktime,tknum))
                conn.commit()
            droptime=input("Enter new DROP OFF date in the format of yyyy-mm-dd OR enter 'N' to keep the old pick up time: ")
            handle_error(droptime)
            if droptime!="N":
                year,month,day=map(int,droptime.split('-'))
                drptime=datetime.date(year,month,day)
                print("pick up time updated")
                c.execute('UPDATE deliveries SET dropOffTime=? WHERE trackingNo=? ',(drptime,tknum))
                conn.commit()
        elif todo=="DELETE":
            done=False
            while not done:
                order=int(input('Enter the oid of the order you want to remove from the delivery: '))
                handle_error(order)
                c.execute('DELETE FROM deliveries WHERE oid=? AND trackingNo=?',(order,tknum))
                conn.commit()
                print("order# ",order," has been deleted from delivery")
                more=input("DELETE another order? (Y/N): ")
                if more=="N":
                    done=True
        else:
            handle_error(todo)
            print("WRONG commanda given!!")
            
   
    elif cmd == "ADD":
        addpid=input("Enter the product id of the product you want to add: ")
        handle_error(addpid)
        addsid=input("Enter the store id of the store you want to add the product to")
        handle_error(addsid)
        addnum=int(input("How many do you want to add?"))
        handle_error(addnum)
        c.execute('UPDATE carries SET qty= qty+? WHERE pid=? AND sid=?',(addnum,addpid,addsid))
        print("qyt updated!")
        conn.commit()
        chanprice=input("Do you want to change the price? (Y/N): ")
        handle_error(chanprice)
        if chanprice!="N":
            chanprice=float(input("What is the new price?: "))
            handle_error(chanprice)
            chanprice=round(chanprice,2)
            c.execute('UPDATE carries SET uprice=? WHERE pid=? AND sid=?',(chanprice,addpid,addsid))
            c.execute('SELECT uprice FROM carries WHERE pid=? AND sid=?',(addpid,addsid))
            print(c.fetchone()[0])
            conn.commit()
    else:
        handle_error(cmd)
        print("WRONG commanda given!!")
         
def login():
    global conn, c,aid,cid
    cora=input("Enter 'c' to login as a customer or enter 'a' as an agent. New member? Enter 'r' to registe. :")
    if cora=="c":#handling for customer login
        cid=input("Please enter your cid: ")
        handle_error(cid)
        if is_valid_id(cora,cid):
            pwd=input("Please enter your password: ")
            handle_error(pwd)
            if correct_pwd(cora,cid,pwd):
                print("Loged in! welcome")
                while True:
                    customer_func(cid)                
                return True
            else:
                print("WRONG PASSWORD!!!,  Try again !!!")
                return False
        else:
            print("WRONG CID !!!,  Try again")
            return False
            
    elif cora=="a":#handling for agent login
        aid=input("Please enter your aid: ")
        handle_error(aid)
        if is_valid_id(cora,aid):
            pwd=input("Please enter your password: ")
            handle_error(pwd)          
            if correct_pwd(cora,aid,pwd):
                print("Loged in! welcome")
                while True:
                    agent_func(aid)                
                return True
            else:
                print("WRONG PASSWORD!!!,  Try again !!!")
                return False
        else:
            print("WRONG AID !!!,  Try again")
            return False
    elif cora=="r":#handling for registry
        registy()
        return False
        
    else:
        handle_error(cora)
        print("Wrong commanda, Try again")
        return False



#cdatabase(path)
def main():
   # conn = sqlite3.connect(sys.argv[1])
    #path='./pjdata.db'
    connect(sys.argv[1])
    #connect(path)
    print("#######################################################")
    print("Enter 'quit!' to quit at any time. Or Enter 'logout!' to logout")
    while login()==False:
        login()
#while not quit and aid==None:
    #customer_func(cid)
#while not quit and cid==None:
    #agent_func(aid)
#c.execute("SELECT * FROM stores;")
#chart=c.fetchall()
#for each in chart:
   # print(each)
main()
