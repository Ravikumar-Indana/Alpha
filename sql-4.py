import mysql.connector
try :
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ravi@123",
        database="ravi")
    print("Connection Successful")
    cur = con.cursor()

    q = f"select * from account"
    
    cur.execute(q)
    
    table = cur.fetchall()

    for record in table:
        print(record)

    con.close()
    print("Connection closed")
except Exception as e:
    print("Connection failed",e)