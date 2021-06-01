#!/usr/bin/python3
"""
    Write a script that lists all cities from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect("localhost",
                         sys.argv[1],
                         sys.argv[2],
                         sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities LEFT JOIN states ON cities.state_id = states.id")
    states = cursor.fetchall()
    for i in range(len(states)):
        print(states[i])
