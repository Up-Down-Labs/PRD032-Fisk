from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA512
from utils.dbconfig import dbconfig

import utils.encrypter
import random
import string

def generatePassword(length):
    syms = ['$','*','<','>']
    return ''.join([random.choice(string.ascii_letters + string.digits + random.choice(syms)) for i in range(length)]) 


def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count = 1000000, hmac_hash_module = SHA512)
    return key


def addEntry(mp, ds, sitename, siteurl, email, username, user):
    password = generatePassword(20)
    mk = computeMasterKey(mp, ds) 

    encrypted = utils.encrypter.encrypt(key = mk, source = password, keyType = "bytes")


    db = dbconfig()
    cursor = db.cursor()
    query = "INSERT INTO Prodathon." + user + "(sitename, siteurl, email, username, password) VALUES (%s, %s, %s, %s, %s);"
    values = (sitename, siteurl, email, username, encrypted)
    cursor.execute(query, values)
    db.commit()

    db.close()

    

