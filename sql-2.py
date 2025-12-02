import mysql.connector
try :
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ravi@123",
        database="ravi")
    print("Connection Successful")
    cur = con.cursor()

    print("Enter Account Details :")
    acc_no = int(input("Enter your Account Number: "))
    name = input("Enter your Name :")
    balance = int(input("Enter balance: "))

    q = f"insert into account values('{name}',{acc_no},{balance})"
    cur.execute(q)
    con.commit()

    print("commited")
    con.close()
    print("Connection closed")
except Exception as e:
    print("Connection failed",e)