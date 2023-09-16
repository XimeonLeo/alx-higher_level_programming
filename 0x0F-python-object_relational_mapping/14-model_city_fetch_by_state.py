#!/usr/bin/python3
""" A module that prints all the city object from a database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    _user = sys.argv[1]
    _passwd = sys.argv[2]
    _db = sys.argv[3]

    # Creating link to the database
    engine = create_engine(
        f"mysql+mysqldb://{_user}:{_passwd}@localhost:3306/{_db}",
        pool_pre_ping=True)

    # Creating all table associated with tge metadata
    Base.metadata.create_all(engine)

    # Establishung sessions
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    query = session.query(City, State)
    states = query.filter(City.state_id == State.id)\
                  .order_by(City.id)

    # Printing results
    for city, state in tuple(states):
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
