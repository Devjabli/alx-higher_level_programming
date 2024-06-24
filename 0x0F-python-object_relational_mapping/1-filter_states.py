#!/usr/bin/python3
"""
This script retrieves all states from 
the hbtn_0e_0_usa database where the name begins with the letter N.
"""

import MySQLdb as db
from sys import argv

"""
his script connects to the hbtn_0e_0_usa
database and retrieves all states 
with a name starting with the letter N. 
"""

if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
