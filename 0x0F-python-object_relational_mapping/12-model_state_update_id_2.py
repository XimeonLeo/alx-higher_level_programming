#!/usr/bin/python3
""" A module that adds a state object to State table in database
    hbtn_0e_6_usa7
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    _user = sys.argv[1]
    _passwd = sys.argv[2]
    _db = sys.argv[3]

    # establishing connection to the database
    engine = create_engine(
        f"mysql+mysqldb://{_user}:{_passwd}@localhost:3306/{_db}",
        pool_pre_ping=True
            )
    # creating all tables related to the Base metadata
    Base.metadata.create_all(engine)

    # create session instance of the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the table
    mod_state = session.query(State).filter(State.id == 2).first()
    mod_state.name = "New Mexico"
    session.commit()

    # Closing session
    session.close()
