#!/usr/bin/python3

import sys
import MySQLdb

def name_filter_states(username, password, db_name, state_name):
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

cursor = db.cursor()

query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

cursor.execute(query, (state_name,))

rows = cursor.fetchall()

for row in rows:
	print(row)

cursor.close()
db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        list_states_with_name(username, password, db_name, state_name)
