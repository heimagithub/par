import os
import sqlite3

dbpath = '/home/heima/Databases/land591.db'

iniF = 0

if (os.path.isfile(dbpath)) :
	print('Read land591!!!')
else :
	iniF = 1
	print('Create land591!!!')

conn = sqlite3.connect(dbpath)
c = conn.cursor()

if iniF == 1 :
	c.execute('''CREATE TABLE LAND(
	ID 			INT 	PRIMARY KEY NOT NULL,
	DATETIME 	TEXT	NOT NULL,
	SECTION		TEXT 	NOT NULL,
	LANDTYPE	TEXT	NOT NULL,
	PRICE 		TEXT 	NOT NULL,
	NOTE		TEXT 	NOT NULL);''')

# c.execute("INSERT INTO LAND(ID, DATETIME, SECTION, LANDTYPE, PRICE, NOTE) \
# 	VALUES (4793098, '2018-02-27 10:00:32', '八德區', '農地', '1,680', '崁頂')");

c.execute("INSERT INTO LAND(ID, DATETIME, SECTION, LANDTYPE, PRICE, NOTE) \
	VALUES (4838674, '2018-02-27 10:10:04', '蘆竹區', '農地', '3,200', '新興街')");


conn.commit()
conn.close()



