#!/usr/bin/python3

import sys
import MySQLdb

def list_states(username, password, dbname):
    #connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    #create a cursor object
    cursor = db.cursor()

    #execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #fetch all the rows from the executed query
    rows = cursor.fetchall()

    #print the rows
    for row in rows:
        print(row)

    #close the cursor  and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_ststes(username, password, db_name)

