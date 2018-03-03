import sqlite3

conn = sqlite3.connect('/home/jhao/Databases/test.db')
# print("Opened database successfully")

cursor = conn.execute("SELECT  name, age from student")

for row in cursor :
	# print(type(row[1]))
	# ==> <class 'int'>
	tmp = row[1]
	print(tmp)