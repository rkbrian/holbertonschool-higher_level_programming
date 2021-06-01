#!/usr/bin/python3
"""
    Write a script that lists all State objects that contain the letter
    a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    newsess = sessionmaker(bind=engine)
    news = newsess()
    stateinf = news.query(State)
    for states in stateinf:
        if "a" in states.name:
            print("{}: {}".format(states.id, states.name))
