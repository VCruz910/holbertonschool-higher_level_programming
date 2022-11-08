#!/usr/bin/python3
"""
Lists all states with name
starting with uppercase N
from hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    DB = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)

    DBCur = DB.cursor()
    DBCur.execute("SELECT * \
            FROM states \
            WHERE CONVERT('name' USING Latin1) \
            COLLATE Latin1_General_CS \
            LIKE 'N%';")
    states = DBCur.fetchall()

    for state in states:
        print(state)
