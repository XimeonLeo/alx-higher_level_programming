#!/usr/bin/python3
""" Using SQLAlchemy to access database from python """
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.orm import relationship


class State(Base):
    """ Defines a clasa State that inherits from Base

        __tablename__: container for the table name State
        id: the state's id
        name: the state's name'
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
