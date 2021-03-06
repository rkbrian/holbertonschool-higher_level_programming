#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""


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
        print(states[i])
