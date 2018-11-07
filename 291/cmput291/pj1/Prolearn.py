import sqlite3
import time
import sys

conn = None
c = None
quit= False
aid= None
cid=None

def connect(path):
    global conn, c

    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(' PRAGMA forteign_keys=ON; ')
    conn.commit()
    return

def define_tables():
    global conn, c

    tablequery= '''
                drop table if exists deliveries;
drop table if exists olines;
drop table if exists orders;
drop table if exists customers;
drop table if exists carries;
drop table if exists products;
drop table if exists categories;
drop table if exists stores;
drop table if exists agents;

create table agents (
  aid           text,
  name          text,
  pwd       	text,
  primary key (aid));
create table stores (
  sid		int,
  name		text,
  phone		text,
  address	text,
  primary key (sid));
create table categories (
  cat           char(3),
  name          text,
  primary key (cat));
create table products (
  pid		char(6),
  name		text,
  unit		text,
  cat		char(3),
  primary key (pid),
  foreign key (cat) references categories);
create table carries (
  sid		int,
  pid		char(6),
  qty		int,
  uprice	real,
  primary key (sid,pid),	
  foreign key (sid) references stores,
  foreign key (pid) references products);
create table customers (
  cid		text,
  name		text,
  address	text,
  pwd		text,
  primary key (cid));
create table orders (
  oid		int,
  cid		text,
  odate		date,
  address	text,
  primary key (oid),
  foreign key (cid) references customers);
create table olines (
  oid		int,
  sid		int,
  pid		char(6),
  qty		int,
  uprice	real,
  primary key (oid,sid,pid),
  foreign key (oid) references orders,
  foreign key (sid) references stores,
  foreign key (pid) references products);
create table deliveries (
  trackingNo	int,
  oid		int,
  pickUpTime	date,
  dropOffTime	date,
  primary key (trackingNo,oid),
  foreign key (oid) references orders);

                '''

    c.executescript(tablequery)
    conn.commit()

    return
def insert_data():
    global conn, c
    insertq='''
            INSERT INTO agents VALUES ('a1','davood','adavood');
            INSERT INTO agents VALUES ('a2','john','ajohn');
            INSERT INTO agents VALUES ('a3','tony','atony');
         
            insert into stores values (10, 'Canadian Tire', '780-111-2222', 'Edmonton South Common');
insert into stores values (20, 'Walmart', '780-111-3333', 'Edmonton South Common');
insert into stores values (30, 'Loblaw City Market', '780-428-1945', 'Oliver Square');
insert into stores values (40, 'Shoppers Drug Mart', '780-426-7642', 'Edmonton City Centre');
insert into stores values (50, 'Shoppers Drug Mart', '780-474-8237', 'Kingsway Mall');
insert into stores values (60, 'Sears Department Store', '780-438-2098', 'Southgate Centre');
insert into stores values (70, 'Hudsons Bay', '780-435-9211', 'Southgate Centre');

insert into categories values ('dai', 'Dairy');
insert into categories values ('bak', 'Bakery');
insert into categories values ('pro', 'Produce');
insert into categories values ('ele', 'Electronics');
insert into categories values ('clo', 'Clothing and Apparel');
insert into categories values ('hom', 'Home Appliances');

insert into products values ('p10','4L milk 1%','ea', 'dai');
insert into products values ('p20','dozen large egg','ea', 'dai');
insert into products values ('p30','cheddar cheese (270g)','ea', 'dai');
insert into products values ('p40','white sliced bread','ea', 'bak');
insert into products values ('p50','dozen donuts','ea', 'bak');
insert into products values ('p60','red delicious apple','lb', 'pro');
insert into products values ('p70','gala apple','lb', 'pro');
insert into products values ('p80','baby carrots (454g)','ea', 'pro');
insert into products values ('p90','broccoli','lb', 'pro');
insert into products values ('p100','headphones','ea', 'ele');
insert into products values ('p110','8gb sdhc Card','ea', 'ele');
insert into products values ('p120','aaa batteries (8-pk)','ea', 'ele');
insert into products values ('p130','led hd tv, 32-in','ea', 'ele');
insert into products values ('p140','v-neck sweater','ea', 'clo');
insert into products values ('p150','cotton hoodie','ea', 'clo');
insert into products values ('p160','coffee maker','ea', 'hom');
insert into products values ('p170','toaster','ea', 'hom');
insert into products values ('p180','food mixer','ea', 'hom');

insert into carries values (10, 'p110', 75, 13.99);
insert into carries values (10, 'p120', 50, 12.99);
insert into carries values (10, 'p130', 20, 249.99);
insert into carries values (10, 'p160', 35, 24.99);
insert into carries values (10, 'p170', 40, 19.99);
insert into carries values (20, 'p10', 100, 4.70);
insert into carries values (20, 'p20', 80, 2.60);
insert into carries values (20, 'p30', 60, 3.79);
insert into carries values (20, 'p40', 120, 2.20);
insert into carries values (20, 'p50', 40, 4.00);
insert into carries values (20, 'p60', 100, 0.79);
insert into carries values (20, 'p70', 90, 1.15);
insert into carries values (20, 'p90', 0, 1.79);
insert into carries values (20, 'p100', 20, 11.79);
insert into carries values (30, 'p10', 90, 4.60);
insert into carries values (30, 'p30', 0, 3.75);
insert into carries values (30, 'p40', 100, 2.10);
insert into carries values (30, 'p50', 35, 5.99);
insert into carries values (30, 'p60', 98, 1.05);
insert into carries values (30, 'p70', 68, 1.25);
insert into carries values (30, 'p80', 40, 1.99);
insert into carries values (30, 'p90', 70, 1.79);
insert into carries values (30, 'p160', 30, 24.99);
insert into carries values (40, 'p10', 90, 4.75);
insert into carries values (40, 'p20', 70, 2.40);
insert into carries values (40, 'p30', 40, 3.89);
insert into carries values (40, 'p40', 89, 1.99);
insert into carries values (40, 'p60', 100, 0.79);
insert into carries values (40, 'p120', 35, 12.99);
insert into carries values (50, 'p10', 80, 4.75);
insert into carries values (50, 'p20', 80, 2.40);
insert into carries values (50, 'p30', 38, 3.89);
insert into carries values (50, 'p40', 84, 1.99);
insert into carries values (50, 'p120', 4, 12.99);
insert into carries values (60, 'p110', 50, 14.39);
insert into carries values (60, 'p120', 75, 13.99);
insert into carries values (60, 'p170', 50, 19.99);
insert into carries values (60, 'p100', 20, 13.49);
insert into carries values (70, 'p140', 32, 22.99);
insert into carries values (70, 'p150', 28, 54.99);
insert into carries values (70, 'p100', 9, 17.59);

insert into customers values ('c10', 'Jack Abraham', 'CS Dept, University of Alberta','cjack');
insert into customers values ('c20', 'Joe Samson', '9632-107 Ave','cjoe');
insert into customers values ('c30', 'John Connor', '111-222 Ave','cjohn');
insert into customers values ('c40', 'Sam Tritzen', '9702-162 St NW','csam');
insert into customers values ('c50', 'Bryanna Petrovic', '391 Richfield Rd','cbry');
insert into customers values ('c60', 'John Doe', '11 Knottwood Rd','cjohn');
insert into customers values ('c70', 'Jane Donald', '8012-122 St SW','cjane');
insert into customers values ('c80', 'Erin Branch', '54 Elanore Dr','cerin');

insert into orders values (100, 'c10', datetime('now', '-3 hours'), 'Athabasca Hall, University of Alberta');
insert into orders values (110, 'c40', datetime('now', '-3 hours'), '9702-162 St NW');
insert into orders values (120, 'c20', datetime('now', '-4 hours'), '9632-107 Ave');
insert into orders values (130, 'c60', datetime('now', '-5 hours'), '31 Jackson Ave');
insert into orders values (140, 'c40', datetime('now', '-8 hours'), '9702-162 St NW');
insert into orders values (150, 'c40', datetime('now', '-2 days'), '9702-162 St NW');
insert into orders values (160, 'c50', datetime('now', '-3 days'), '391 Richfield Rd');
insert into orders values (170, 'c10', datetime('now', '-4 days'), 'Athabasca Hall, University of Alberta');
insert into orders values (180, 'c20', datetime('now', '-4 days'), '9632-107 Ave');
insert into orders values (190, 'c50', datetime('now', '-5 days'), '391 Richfield Rd');
insert into orders values (200, 'c70', datetime('now', '-5 days'), '90 Jonah Ave');
insert into orders values (210, 'c70', datetime('now', '-5 days'), '8012-122 St SW');
insert into orders values (220, 'c80', datetime('now', '-6 days'), '54 Elanore Dr');
insert into orders values (230, 'c30', datetime('now', '-8 days'), '111-222 Ave');

insert into olines values (100, 20, 'p20', 1, 2.8);
insert into olines values (110, 30, 'p70', 1, 1.25);
insert into olines values (110, 30, 'p80', 2, 1.99);
insert into olines values (120, 20, 'p10', 1, 4.7);
insert into olines values (120, 40, 'p20', 1, 2.4);
insert into olines values (120, 40, 'p30', 1, 3.89);
insert into olines values (130, 70, 'p150', 1, 54.99);
insert into olines values (140, 40, 'p60', 2, 0.79);
insert into olines values (140, 30, 'p90', 2, 1.79);
insert into olines values (150, 60, 'p110', 1, 14.39);
insert into olines values (160, 20, 'p70', 1, 1.15);
insert into olines values (160, 30, 'p80', 1, 1.99);
insert into olines values (170, 20, 'p100', 2, 11.79);
insert into olines values (180, 40, 'p60', 1, 1.05);
insert into olines values (180, 40, 'p120', 1, 12.99);
insert into olines values (180, 40, 'p40', 1, 1.99);
insert into olines values (190, 10, 'p50', 1, 4);
insert into olines values (190, 10, 'p10', 1, 4.7);
insert into olines values (200, 10, 'p130', 1, 249.99);
insert into olines values (210, 10, 'p120', 1, 12.99);
insert into olines values (220, 30, 'p110', 1, 4.6);
insert into olines values (230, 20, 'p50', 2, 4);

insert into deliveries values (1000,100,datetime(), null);
insert into deliveries values (1001,110,datetime('now', '-3 hours'), datetime('now'));
insert into deliveries values (1002,120,datetime('now','-4 hours'), datetime('now'));
insert into deliveries values (1003,130,datetime(), null);
insert into deliveries values (1004,140,datetime('now', '-5 hours'), datetime('now', '-4 hours'));
insert into deliveries values (1005,150,datetime('now', '-1 day'), null);
insert into deliveries values (1006,160,datetime('now', '-1 day'), null);
insert into deliveries values (1007,170,datetime(), datetime('now', '-3 hours'));
insert into deliveries values (1008,180,datetime(), null);
insert into deliveries values (1009,190,datetime(), datetime('now'));
insert into deliveries values (1010,200,datetime(), null);
insert into deliveries values (1011,210,datetime('now', '-2 days'), datetime('now', '-1 day'));
insert into deliveries values (1012,220,datetime('now', '-2 days'), null);
insert into deliveries values (1013,230,datetime('now', '-8 days'), null);
'''
    c.executescript(insertq)
    conn.commit()
    return
def cdatabase(path):
    global conn, c
    connect(path)
    define_tables()
    insert_data()
    return
def is_custom(cid):
    c.execute('SELECT cid FROM customers WHERE cid=?;',(cid,))
    if c.fetchone() != None:
        return True
    else:
        return False
def correct_pwd(cid,pwd):
    c.execute('SELECT pwd FROM customers WHERE cid=? AND pwd=?',(cid,pwd))
    if c.fetchone() != None:
        return True
    else:
        return False
def ifquit():
    global conn,c,quit
    if quit==True:
        print("Exiting....")
        time.sleep(1)
        conn.close()
        print("Exitted!")
        sys.exit()
    else:
        return False
def login():
    global conn, c,quit,aid,cid
    cora=input("Enter 'c' to login as a customer or enter 'a' as an agent. ")
    if cora=="c":
        cid=input("Please enter your cid: ")
        if cid=="quit!":
            quit=True
            ifquit()
        if is_custom(cid):
            pwd=input("Please enter your password: ")
            if pwd=="quit!":
                quit=True
                ifquit()
            if correct_pwd(cid,pwd):
                return True
            else:
                print("WRONG PASSWORD!!!,  Try again !!!")
                return False
        else:
            print("WRONG CID !!!,  Try again")
            return False
            
    elif cora=="a":
        aid=input("Please enter your aid: ")
        if aid=="quit!":
            quit=True
            ifquit()
        if is_custom(aid):
            pwd=input("Please enter your password: ")
            if pwd=="quit!":
                quit=True
                ifquit()            
            if correct_pwd(aid,pwd):
                return True
            else:
                print("WRONG PASSWORD!!!,  Try again !!!")
                return False
        else:
            print("WRONG CID !!!,  Try again")
            return False
    elif cora=="quit!":
        quit=True
        ifquit()
    else:
        print("Wrong commanda, Try again")
        return False

def customer_func(cid):
    global conn, c,quit
    cmd = input("What do you want to do? ENTER||SEARCH to search for a product||PLACE o place an order||LIST to see all your orders")
    #leave(cmd)
    if cmd == "SEARCH":
        #search orders
        pass
    elif cmd == "PLACE":
        c.execute("SELECT name FROM products")
        productlist=c.fetchall()
        for product in productlist:
            print(product[0])
        #print all products
        finished=False
        cart=[]
        pinfo=[]
        sinfo=[]
        qtyinfo=[]
        while not finished:
            wantedproduct=input("Enter the product you want to order:")
            if wantedproduct=="quit!":
                quit=True
                ifquit()
            wantqty=input("How many/much do you want? ")
            if wantqty=="quit!":
                quit=True
                ifquit()                
            c.execute('SELECT s.name,c.qty FROM stores s,carries c,products p WHERE s.sid=c.sid AND p.name=? AND p.pid=c.pid AND c.qty>=?',(wantedproduct,wantqty))
            storelist=c.fetchall()
            for row in range(0,len(storelist)):
                print("store ",storelist[row][0]," has ",storelist[row][1]," in stock")
            pstore=input("Which store do you want purches from? :")
            if pstore=="quit!":
                quit=True
                ifquit()             
            c.execute("SELECT p.name, p.pid FROM products p, carries c WHERE name = :nam AND p.pid==c.pid AND c.qty>= :qtii",{"nam":wantedproduct,"qtii":wantqty})
            orderp=c.fetchone()
            if orderp==None:
                print("Product", wantedproduct ,"NOT in stock at",pstore,"(or store name had a spelling mistake)Please try again! ")
            else:
                cart.append(orderp[0])
                pid=orderp[1]
                pinfo.append(pid)
                c.execute('SELECT sid FROM stores WHERE name=?',(pstore,))
                sid=c.fetchone()[0]
                sinfo.append(sid)
                qtyinfo.append(wantqty)
                c.execute('UPDATE carries SET qty=qty-? WHERE sid=? AND pid=?',(wantqty,sid,pid))
                print("added to cart!")
                goodtogo=input("Continue Shopping?(Y/N)?")
                if wantqty=="quit!":
                    quit=True
                    ifquit()                 
                if goodtogo=="N":
                    finished=True

            #place the order
       # c.execute('SELECT uprice FROM carries WHERE pid=? AND sid=?',(pid,sid))
       # uprice=c.fetchone()[0]
        c.execute('SELECT MAX(oid) FROM orders;')
        disoid=c.fetchone()
        disoid=int(disoid[0])+1
        current_date = time.strftime("%Y-%m-%d %H:%M:%S")
        c.execute('SELECT address FROM customers WHERE cid=?',(cid,))
        address=c.fetchone()[0]
        c.execute('INSERT INTO orders VALUES (?,?,?,?)',(disoid,cid,current_date,address))
        conn.commit()
        c.execute('SELECT oid FROM orders WHERE oid=?',(disoid,))
        print("Your order id is :",c.fetchone()[0])
        for item in range(0,len(cart)):
            pid=pinfo[item]
            sid=sinfo[item]
            wantqty=qtyinfo[item]
            c.execute('SELECT uprice FROM carries WHERE pid=? AND sid=?',(pid,sid))
            uprice=c.fetchone()[0]            
            c.execute('INSERT INTO olines VALUES(?,?,?,?,?)',(disoid,sid,pid,wantqty,uprice))
        conn.commit()

            
            
            
        
    elif cmd == "LIST":
        order_to_show=None
        c.execute('SELECT ol.oid,o.odate,ol.qty,ol.uprice*ol.qty FROM orders o, olines ol WHERE o.cid=? AND o.oid=ol.oid ORDER BY o.odate DESC',(cid,))
        order_to_show=c.fetchall()
        i=0
        contin="Y"
        while contin=="Y" and i < len(order_to_show):
            for row in range (i,i+5):
                if row < len(order_to_show):
                    print(order_to_show[row])
                else:
                    break
            i=i+5
            if i>=len(order_to_show):
                break                
            contin=contin=input("Show more? (Y/N) :")
            if contin=="quit!":
                quit=True
                ifquit()

path='./pjdata.db'
#cdatabase(path)
connect(path)
def agent_func():
    cmd = input("What do you want to do? ENTER||SETUP to set up a delivery||UPDATE to update a delivery||ADD ti add stock to a store")
    #leave(cmd)
    if cmd == "SETUP":
        #setupleave(cmd)
        pass
    elif cmd == "UPDATE":
        #update
        pass
    elif cmd == "ADD":
        addpid=input("Enter the product you want to add: ")
        addsid=input("Enter the store you want to add the product to")
        addnum=int(input("How many do you want to add?"))
        c.execute('UPDATE carries SET qty= qty+? WHERE pid=? AND sid=?',(addnum,addpid,addsid))
        print("qyt updated!")
        conn.commit()
        chanprice=input("Do you want to change the price? (Y/N): ")
        if chanprice!="N":
            chanprice=float(input("What is the new price?: "))
            chanprice="%.2f" %chanprice
            c.execute('UPDATE carries SET uprice=? WHERE pid=? AND sid=?',(chanprice,addpid,addsid))
            c.execute('SELECT uprice FROM carries WHERE pid=? AND sid=?',(addpid,addsid))
            print(c.fetchone()[0])
            conn.commit()
        elif chanprice="quit!":
            quit=True
            quit()
        else:
            print("Wrong Message")
while login()==False:
    login()
agent_func()

#while not quit:
    #customer_func(cid)
#c.execute("SELECT * FROM stores;")
#chart=c.fetchall()
#for each in chart:
   # print(each)
