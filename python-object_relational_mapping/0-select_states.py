#!/usr/bin/python3
"""
Lists all states from
hbtn_0e_0_usa database.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    DB = MYSQLdb.connect(USER=sys.argv[1],
            PASSWD=sys.argv[2], DB=sys.argv[3],
            PORT=3306)
    CURSOR = DB.CURSOR()
    CURSOR.execute("SELECT * FROM states;")
    states = CURSOR.fetchall()

    for state in states:
        print(state)
