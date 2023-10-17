#IMPORT
import mysql.connector as sql

#CONNECT
def dbconfig():
    db = sql.connect(
        host = 'localhost',
        user = 'root',
        password = 'password'
        )  
    return db
