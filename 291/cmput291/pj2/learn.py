import os
import sys
from bsddb3 import db



DB_re = "ye.idx"
global curs_re
global database_re    
database_re = db.DB()#set up database for records
database_re.open(DB_re,None, db.DB_BTREE, db.DB_CREATE)
curs_re = database_re.cursor()

item=curs_re.first()
while item:
    print(item)
    item=curs_re.next()
print("\n")
printer=curs_re.set(b'2015')
if (curs_re.next)!=None:
    print("haha")
