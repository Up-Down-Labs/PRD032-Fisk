from utils.dbconfig import dbconfig
import random
import string
import hashlib



def generateDeviceSecret(length = 10):
    return ''.join(random.choices((string.ascii_uppercase + string.digits), k = length))

def new_user(username, password):
    db = dbconfig()
    cursor = db.cursor()

    hashed_mp = hashlib.sha256(password.encode()).hexdigest()
  
    ds = generateDeviceSecret()


    #ADD BOTH TO TABLE
    query = '''INSERT INTO Prodathon.users(username, masterkey_hash, device_secret) VALUES(%s, %s, %s)'''
    values = (username, hashed_mp, ds)
    cursor.execute(query, values)
    db.commit()

    #CREATE TABLE FOR THEIR PASSWORDS
    query = "CREATE TABLE IF NOT EXISTS Prodathon."+ username +"(sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL);"
    values = (username)
    res = cursor.execute(query, values)
    db.commit()


    db.close()
