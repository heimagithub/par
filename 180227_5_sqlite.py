import os
import sqlite3

dbpath = '/home/heima/Databases/NewDB.db'

conn = sqlite3.connect(dbpath)
c = conn.cursor()

sql = ''' 	UPDATE LAND
			SET DATETIME = ?,
				SECTION = ?,
				LANDTYPE = ?,
				PRICE = ?,
				NOTE = ?
				WHERE ID = ?	'''

c.execute(sql, ('2018-02-28 08:09:00', '蘆竹區', '建地', '3,000', '坐北朝南', 4793098))


sql = ''' 	UPDATE LAND
			SET PRICE = ?
			WHERE ID = ?	'''

c.execute(sql, ('2,500', 4793098))

conn.commit()
conn.close()