#!/usr/bin/python3
'''
Lists all states from
hbtn_0e_0_usa database.
'''
import sys
import MySQLdb

if __name__ == '__main__':
    DB = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    DBCur = DB.cursor()
    DBCur.execute(
            "SELECT * FROM states WHERE name LIKE %s
            ORDER BY id ASC;", (sys.argv[4]))
    states = DBCur.fetchall()

    for state in states:
        print(state)
