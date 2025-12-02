import mysql.connector
try :
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ravi@123",
        database="ravi")
    print("Connection Successful")
    cur = con.cursor()
    q = 'create table account (name varchar(20), acc_no int(10), balance float(10))'
    cur.execute(q)
    print("Table created successfully")
    con.close()
    print("Connection closed")
except Exception as e:
    print("Connection failed",e)