#!/usr/bin/python3


"""This file contains the class definition of a State
and an instance"""

from sql alchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """this is a class representation
    of State that inherits from SQLAlchemy's Base class"""
    __tablename__ = 'states'

    id = Column(Integer(11), primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    """checks the value of the special variable"""
    engine = create_engine('mysql://username:password@localhost:3306/database')
    Base.metadata.create_all(engine)
