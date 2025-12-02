import mysql.connector
try :
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ravi@123",
        database="ravi")
    print("Connection Successful")
    cur = con.cursor()

    print("*****  Deposit operation ******")
    acc_no = int(input("Enter your Account Number: "))
    #name = input("Enter your Name :")
    balance = int(input("Enter balance: "))

    q = f"update account set balance = balance+ {balance} where acc_no ={acc_no}"
    
    cur.execute(q)
    con.commit()

    print("commited")

    if cur.rowcount > 0:
        print("Deposited")
    else:
        print("Error - no such account")
    con.close()
    print("Connection closed")
except Exception as e:
    print("Connection failed",e)