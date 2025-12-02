import mysql.connector
try :
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ravi@123",
        database="ravi")
    print("Connection Successful")
    cur = con.cursor()

    print("*****  Enter your Account number for delete ******")
    acc_no = int(input("Enter your Account Number: "))
    
    q = f"delete from account where acc_no ={acc_no}"
    
    cur.execute(q)
    con.commit()

    print("commited")

    if cur.rowcount == 0:
        print("Invalid Account number")
    else:
        print("Deleted")
    con.close()
    print("Connection closed")
except Exception as e:
    print("Connection failed",e)