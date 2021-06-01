#!/usr/bin/python3
"""
    Write a script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""


import sys
from sqlalchemy.sql.sqltypes import BINARY
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect("localhost",
                         sys.argv[1],
                         sys.argv[2],
                         sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    LEFT JOIN states ON cities.state_id = states.id \
    WHERE BINARY states.name = %s", (sys.argv[4],))
    cities = cursor.fetchall()
    city_list = []
    for i in range(len(cities)):
        city_list.append(cities[i])
    print(", ".join(city_list))
