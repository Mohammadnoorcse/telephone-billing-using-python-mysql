import mysql.connector as mq
from tabulate import tabulate

def menu():
    print('\t\t\tTELEPHONE BILLING SYSTEM')
    print('\t\t\t========================\n\n')
    print('\t\t\t\tMAIN MENU')
    print('\t\t\t\t========')

    print('\t\t1.Register User \t 2.search customer \n\t\t3.Update Customer \t 4.Generate Bill')
    print('\t\t5.Delete Customer \t 6. Help \n\t\t7.Exit\n')
def register():
    print('\n\t\tNew Customer Registration\n')
    print('\n\t\t---------------------------\n')
    ph = int(input('Enter your phone num : '))
    nam = input('Enter Name: ')
    add = input('Enter Address : ')
    aadhar = input('Enter Aadhar num: ')
    
    con = mq.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='allah',
                        database='telephone',
                        auth_plugin='mysql_native_password'
                        )
    cur = con.cursor()
    query = "insert into cust(phno,name,addr,aadhar) values({},'{}','{}','{}')".format(ph,nam,add,aadhar)
    cur.execute(query)
    con.commit()
    print('\nSuccessfully Registered the User...')
    con.close()
    
def search():
    
    print('\n\t\tSearch Customer')
    print('\t\t----------------\n')
    ph = int(input('Enter your phone num : '))
    con = mq.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='allah',
                        database='telephone',
                        auth_plugin='mysql_native_password'
                        )
    cur = con.cursor()
    query = "select * from cust where phno = {}".format(ph)
    cur.execute(query)
    res = cur.fetchall()
    h =['phno','name','addr','aadhar','bill','status']
    if res == []:
        print('\nCustomer doesnt Exit')
    else:
        
        print(tabulate(res,headers = h))
        
        
    con.close()        

def modify():
    
    print('\n\t\tupdate Customer Date')
    print('\t\t--------------------\n')
    ph = int(input('Enter your phone num : '))
    con = mq.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='allah',
                        database='telephone',
                        auth_plugin='mysql_native_password'
                        )
    cur = con.cursor()
    query = "select * from cust where phno = {}".format(ph)
    cur.execute(query)
    res = cur.fetchall()
    if res == []:
        
        print('\nCustomer doesnt Exit')
    
    else:
        print('1.Name\n2.Adress\n3.Aadhar No')
        ch = int(input('Enter Choice to Update : '))
        if ch == 1:
            nam = input('Enter New Name : ')
            query = "update cust set name = '{}' where phno = {}".format(nam,ph)
            cur.execute(query)
            con.commit()
            print("\nSuccessfully Updated Name...")
            
        elif ch == 2:
            add = input('Enter New Address : ')
            query = "update cust set addr = '{}' where phno = {}".format(add,ph)
            cur.execute(query)
            con.commit()
            
            print("\nSuccessfully Updated Address...")
        
        elif ch == 3:
            
            aadar = input('Enter New Name : ')
            query = "update cust set aadhar = '{}' where phno = {}".format(aadar,ph)
            cur.execute(query)
            con.commit()
            
            print("\nSuccessfully Updated Aadar...")
        
        else:
            print('Please choose correct choice ..')
    con.close()        

def billing():

    ph = int(input('Enter your phone num : '))
    con = mq.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='allah',
                        database='telephone',
                        auth_plugin='mysql_native_password'
                        )
    cur = con.cursor()
    query = "select * from cust where phno = {}".format(ph)
    cur.execute(query)
    res = cur.fetchall()
    if res == []:
        
        print('\nCustomer doesnt Exit')
    
    else:
        calls = int(input('Enter No of Calls : '))
        
        bill = 0
        if calls>150:
            bill = bill + (calls-150)*3 + 50*2.5 + 50*1.5
        
        elif 100<calls<=150:
            bill = bill + (calls-100)*2.5 + 50*1.5
        
        elif 50<calls<=100:
            bill = bill +(calls-50)*1.5
        print('\t\t\t Billing')
        print('\t\t-----------------\n')
        if res[0][5] !="Paid":
            old_bill = res[0][4]
        else:
            old_bill = 0
       
        print('\n\t\tPending Bill Amount ',old_bill)
        print('\n\t\tNew Bill Amount ',bill)
        print('\t\t------------------------')
        print('\t\tTotal Bill Amount ',bill+old_bill)
        print('\t\t---------------------------')
        
        ch = input('Press Y to pay Bill Now or Any other key to Pay later : ')
        
        if ch in ['Y','y']:
            query = "update cust set bill = {},status = 'Paid' where phno = {}".format(bill+old_bill,ph)
            cur.execute(query)
            con.commit()
            print('\nSuccessfully Paid the Bill')
        
        else:
            query = "update cust set bill = {},status = 'UnPaid' where phno = {}".format(bill+old_bill,ph)
            cur.execute(query)
            con.commit()
            print('\nPlease make payment as soon as possible')
    con.close()
        

def remove():
    ph = int(input('Enter your phone num : '))
    con = mq.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='allah',
                        database='telephone',
                        auth_plugin='mysql_native_password'
                        )
    cur = con.cursor()
    query = "select * from cust where phno = {}".format(ph)
    cur.execute(query)
    res = cur.fetchall()
    if res == []:
        
        print('\nCustomer doesnt Exit')
    
    else:
        ch = input("Are you sure to delete customer..Y/N : ")
        if ch in ['y','Y']:
            query = "delete from cust where phno = {}".format(ph)
            cur.execute(query)
            con.commit()
            print('\nSuccessfully Deleted Customer from Database')
        
        else:
            print('No changes made in your database')
            
    con.close()
    

def helping():
    
    print('\t\t\tHelp')
    print('\t\t\t=====')
    print('First 50 Calls are free')
    print('50-100 calls are 1.5Rs per call')
    print('101-150 calls are 2.5Rs per call')
    print('Above 150 calls are 1.5Rs per call')
    
    
while True:
    menu()
    ch = int(input('Enter your choice : '))
    if ch == 1:
        register()
    elif ch == 2:
        search()
    elif ch == 3:
        modify()
    elif ch ==4:
        billing()
    elif ch == 5:
        remove()
    elif ch == 6:
        helping()
    elif ch == 7:
        exit()

    else:
        print('\nPlease Choose correct choice and Try Again...')
    
    ch=int(input('\nPress 0 to continue...Any other key to Exit : '))
    
    if ch!=0:
        break