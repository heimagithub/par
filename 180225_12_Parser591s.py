import os
import sqlite3

dbpath = '/home/heima/Databases/land591.db'

conn = sqlite3.connect(dbpath)
c = conn.cursor()

c.execute(''' 	UPDATE LAND
								SET DATETIME = ?, 
									SECTION = ?, 
									LANDTYPE = ?, 
									AREA = ?, 
									PRICE = ?, 
									NOTE = ?
								WHERE ID = ? ''', 
									('2018-02-28 08:09:32', 
										'蘆竹區', 
										'建地',
										'116.8',
										'4,999',
										'新興路',
										4839065));


conn.commit()
conn.close()