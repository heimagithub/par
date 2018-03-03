import sqlite3

conn = sqlite3.connect('/home/heima/Databases/land591.db')
c  = conn.cursor()
c.execute('''CREATE TABLE LAND591
	(ID INT PRIMARY KEY NOT NULL,
	NAME 	TEXT	NOT NULL,
	AGE		INT 	NOT NULL);''')

conn.commit()
conn.close()