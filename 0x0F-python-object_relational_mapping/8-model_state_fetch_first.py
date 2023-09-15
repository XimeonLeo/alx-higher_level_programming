#!/usr/bin/python3
"""A module that list the first State in database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    _user = sys.argv[1]
    _passwd = sys.argv[2]
    _db = sys.argv[3]
    engine = create_engine(
            f"mysql+mysqldb://{_user}:{_passwd}@localhost:3306/{_db}"
        )

    # create table from metadata
    Base.metadata.create_all(engine)

    # create session bounded to the engine created
    Session = sessionmaker(bind=engine)
    session = Session()

    # Qurey all states present in the database and order by s.id
    state = session.query(State).order_by(State.id).first()

    # Printing results
    if state is None:
        print()
    else:
        print(f"{state.id}: {state.name}")

    session.close()
