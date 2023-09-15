#!/usr/bin/python3
"""A module that prints the state id of a particular state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    _user = sys.argv[1]
    _passwd = sys.argv[2]
    _db = sys.argv[3]
    _state = sys.argv[4]

    # creating link to database
    engine = create_engine(
        f"mysql+mysqldb://{_user}:{_passwd}@localhost:3306/{_db}"
            )
    # creating all table associated with the engine
    Base.metadata.create_all(engine)

    # creating a session and binding it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # making a query to get desired result
    state = session.query(State).filter(State.name.like(_state)).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)
