#!/usr/bin/python3

"""This file contains the class definition of a State
and an instance"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class representation of State
    that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer(11), primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    engine = create_engine('mysql://username:password@localhost:3306/database')
    Base.metadata.create_all(engine)
