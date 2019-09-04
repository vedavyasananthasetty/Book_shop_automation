'''
Created on Sep 27, 2018

@author: lenovo
'''
import sqlite3
con = sqlite3.connect("mydb4.db")
print("database connected")
print()
cur = con.cursor()
cur.execute("create table if not exists customer5(cid int,ctype varchar(20),cname varchar(20),address varchar(200),primary key(cid))")
cur.execute("CREATE TABLE if not exists salesrecord5(nocp int,sprice int,sid int)")
cur.execute("CREATE TABLE if not exists sales5(balance int,invoiceno int,amount_paid int,cid int,sid int,primary key(sid))")
cur.execute(" CREATE TABLE if not exists books5(bname varchar(20),publisher varchar(20),location varchar(100),nocp int,price int,author varchar(20))")
cur.execute("CREATE TABLE if not exists usr5(uid int,phno int,address varchar(200),primary key(uid))")
cur.execute("CREATE TABLE if not exists supplier5(address varchar(200),phno int,sname varchar(20),suid int,primary key(suid))")
cur.execute("CREATE TABLE if not exists purchase5 (pamount int,pnote varchar(20),balance int,paid int,pid int,suid int)")
cur.execute(" CREATE TABLE if not exists precord5 (nocp int,price int,pid int)")


n=int(input("BOOKSHOP AUTOMATION SYSTEM DATABASE BY GROUP 2: no. of customers please:"))
try:
    
    for i in range(1, n+1):
        cid = input("enter cid :" + str(i) + ":")
        ctype = input("type:" + str(i) + ":")
        cname = input("enter name :" + str(i) + ":")
        address = input("enter address :" + str(i) + ":")
        cur.execute("insert INTO customer5 (cid,ctype,cname,address) values(?,?,?,?)", (cid,ctype,cname,address))
    con.commit()

    print('customers:')
    print('CUSTOMERS TABLE')
    print()
    cur.execute("select * from customer5")
    for row in cur.fetchall():
        print(row)
    print()
    
    
    for i in range(1, n+1):
        nocp = input("enter copies :" + str(i) + ":")
        sprice = input("price:" + str(i) + ":")
        sid = input("enter sid :" + str(i) + ":")
        cur.execute("insert INTO salesrecord5(nocp,sprice,sid) values(?,?,?)", (nocp,sprice,sid))
    con.commit()

    print('sales record:')
    print('SALES RECORD TABLE')
    print()
    cur.execute("select * from salesrecord5")
    for row in cur.fetchall():
        print(row)
    print()
     
    
    
    for i in range(1, n+1):
        balance = input('enter balance: ' + str(i) + ':')
        invoiceno = input('enter invoice no.:' + str(i) + ':')
        amount_paid= input('enter paid amount :' + str(i) + ':')
        cid= input('enter cids :' + str(i) + ':')
        sid= input('enter sids:' + str(i) + ':')
        
    
        cur.execute("insert into sales5(balance,invoiceno,amount_paid,cid,sid) values(?,?,?,?,?)", (balance,invoiceno,amount_paid,cid,sid))
    con.commit()
    print("values inserted into sales table ")
    print('SALES:')
    print()
    cur.execute("select * from sales5")
    for row in cur.fetchall():
        print(row)
    print()
    


    for i in range(1, n+1):
        bname= input('enter book name :' + str(i) + ':')
        publisher = input('enter  publisher:' + str(i) + ':')
        loction= input('enter location: ' + str(i) + ':')
        nocp = input('enter copies: ' + str(i) + ':')
        price = input('enter price :' + str(i) + ':')
        author= input('enter name of author: ' + str(i) + ':')
        cur.execute("insert into books5 (bname,publisher,location,nocp,price,author) values(?,?,?,?)",
                (bname,publisher,location,nocp,price,author))
    con.commit()
    print("values inserted into books ")
    print('BOOKS TABLE')
    print()
    cur.execute("select * from books5")
    for row in cur.fetchall():
        print(row)
    print()
    
    
    for i in range(1, n+1):
        uid= input('enter user id:' + str(i) + ':')
        phno = input('enter  phone number:' + str(i) + ':')
        address= input('enter address: ' + str(i) + ':')
        cur.execute("insert into usr5 (uid,phno,address) values(?,?,?)",
                (uid,phno,address))
    con.commit()
    print("values inserted into user")
    print('USER TABLE')
    print()
    cur.execute("select * from usr5")
    for row in cur.fetchall():
        print(row)
    print()
    
    
    
    for i in range(1, n+1):
        address= input('enter address :' + str(i) + ':')
        phno = input('enter phone number:' + str(i) + ':')
        sname= input('enter name: ' + str(i) + ':')
        suid= input('enter id :' + str(i) + ':')
        cur.execute("insert into supplier5 (address,phno,sname,suid) values(?,?,?,?)",
                (address,phno,sname,suid))
    con.commit()
    print("values inserted into Supplier")
    print('SUPPLIER TABLE')
    print()
    cur.execute("select * from supplier5")
    for row in cur.fetchall():
        print(row)
    print()



    for i in range(1, n+1):
        pamount= input('enter amount: ' + str(i) + ':')
        pnote = input('enter note:' + str(i) + ':')
        balance = input('enter balance: ' + str(i) + ':')
        paid= input('enter paid amount: ' + str(i) + ':')
        pid= input('enter pid: ' + str(i) + ':')
        suid= input('enter id :' + str(i) + ':')
        cur.execute("insert into purchase5 (pamount,pnote,balance,paid,pid,suid) values(?,?,?,?,?,?)",
               (pamount,pnote,balance,paid,pid,suid))
    con.commit()
    print("values inserted into purchase")
    print('PURCHASE TABLE')
    print()
    cur.execute("select * from purchase5")
    for row in cur.fetchall():
        print(row)
    print()
    
    for i in range(1, n+1):
        
        nocp = input('enter copies: ' + str(i) + ':')
        price= input('enter amount: ' + str(i) + ':')
        pid= input('enter pid: ' + str(i) + ':')
        
        cur.execute("insert into precord5 (nocp,price,pid) values(?,?,?)",
               (nocp,price,pid))
    con.commit()
    print("values inserted into purchase record")
    print('PURCHASE RECORD TABLE')
    print()
    cur.execute("select * from precord5")
    for row in cur.fetchall():
        print(row)
    print()
    
except Exception as ex:
    print('error:', ex)

finally:
    con.close()
    print("database connection terminated. thank you. end of mini project")