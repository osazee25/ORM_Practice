#!/usr/bin/python3
import sys
import MySQLdb

def list_states_starting_with_N(username, password, db_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Fetch all the rows from the executed query
    rows = cursor.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)
    
    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_states_starting_with_N(username, password, db_name)
