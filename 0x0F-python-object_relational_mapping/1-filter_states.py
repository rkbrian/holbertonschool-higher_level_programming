#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N) from the database"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect("localhost",
                         sys.argv[1],
                         sys.argv[2],
                         sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for i in range(len(states)):
        if states[i][0] == "N":
            print(states[i])
