#!/usr/bin/python3


'''
Takes in an argument and
displays all values in state
table of hbtn_0e_0_usa where
name matches arguments.
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
            "SELECT * FROM states WHERE name LIKE " "
            '{:s}' ORDER BY id ASC;".format(sys.argv[4]))
    states = DBCur.fetchall()

    for state in states:
        print(state)
