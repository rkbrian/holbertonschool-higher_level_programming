#!/usr/bin/python3
"""
    Write a script that lists all State objects
    If the table states is empty, print Nothing followed by a new line
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    newsess = sessionmaker(bind=engine)
    news = newsess()
    stateinf = news.query(State).first()
    if stateinf is None:
        print("Nothing")
    else:
        print("{}: {}".format(stateinf.id, stateinf.name))
