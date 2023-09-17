#!/usr/bin/python3
""" A module that creates a city and state with relationship """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    _user = sys.argv[1]
    _passwd = sys.argv[2]
    _db = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{_user}:{_passwd}@localhost:3306/{_db}",
        pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")

    session.close()
