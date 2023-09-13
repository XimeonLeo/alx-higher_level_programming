#!/usr/bin/python3
""" A module that list all states with name starting with N """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cusr = db.cursor()
    cusr.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    states = cusr.fetchall()

    for state in states:
        print(state)

    cusr.close()
    db.close()
