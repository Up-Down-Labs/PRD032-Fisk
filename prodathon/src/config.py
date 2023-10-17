from Tkinter.utils.dbconfig import dbconfig


def config():
    db = dbconfig()
    cursor = db.cursor()

    cursor.execute("CREATE DATABASE Prodathon")

    
    #CREATE TABLES
    query = '''CREATE TABLE Prodathon.users(username Varchar(100) Primary key, masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL);'''
    res = cursor.execute(query)
    db.commit()
   
    # query = '''CREATE TABLE Prodathon.passwords(sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL);'''
    # res = cursor.execute(query)
    # db.commit()




config()







