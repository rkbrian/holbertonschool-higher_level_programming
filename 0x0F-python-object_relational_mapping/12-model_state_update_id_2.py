#!/usr/bin/python3
"""
    Write a script that changes the name of a State object from the database hbtn_0e_6_usa
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

    renew_state = news.query(State).filter_by(id=2).first()
    renew_state.name = "New Mexico"
    news.commit()
