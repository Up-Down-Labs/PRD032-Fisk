from utils.dbconfig import dbconfig
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA512

import utils.encrypter


def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count = 1000000, hmac_hash_module = SHA512)
    return key


def retrieveEntry(mp, ds, sitename, email, user):
    db = dbconfig()
    cursor = db.cursor()

    query = "select * from Prodathon." + user + " where sitename = '{}' and email = '{}';".format(sitename, email)

    cursor.execute(query)
    results = cursor.fetchall()

    if len(results) == 0:
        return -1
 
    if (len(results) == 1):
        mk = computeMasterKey(mp, ds)
        decrypted = utils.encrypter.decrypt(key = mk, source = results[0][4], keyType = "bytes")

        return decrypted
    
    db.close()

