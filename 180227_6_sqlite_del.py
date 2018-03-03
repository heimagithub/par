import os
import sqlite3

dbpath = '/home/heima/Databases/NewDB.db'

conn = sqlite3.connect(dbpath)
c = conn.cursor()


c.execute('DELETE from LAND where ID = 4838674')

conn.commit()
conn.close()