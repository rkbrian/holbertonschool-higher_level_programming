#!/usr/bin/python3
"""
    Write a script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument. But this
    time, write one that is safe from MySQL injections!
"""


import sys
from sqlalchemy.sql.sqltypes import BINARY
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                        port="3306",
                        username=sys.argv[1],
                        password=sys.argv[2],
                        db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s", (sys.argv[4]))
    states = cursor.fetchall()
    for i in range(len(states)):
        print(states[i])
