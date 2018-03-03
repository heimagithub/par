import sqlite3

def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE EXAMPLE
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''

    cur = conn.cursor()
    cur.execute(sql, task)

def create_connection(db_file):

	conn = sqlite3.connect(db_file)
	c  = conn.cursor()
	c.execute('''CREATE TABLE EXAMPLE 
		(PR 		INT 	PRIMARY KEY NOT NULL,
		begin_date 	TEXT	NOT NULL,
		end_date	TEXT 	NOT NULL,
		id, 		INT 	NOT NULL);''')
    # try:
    #     conn = sqlite3.connect(db_file)
    #     return conn
    # except Error as e:
    #     print(e)
 
    # return None

def main():
    database = "/home/heima/Databases/maindb.db"
 
    # create a database connection
    conn = create_connection(database)

    update_task(conn, (2, '2015-01-04', '2015-01-06',2))

if __name__ == "__main__":
	main()