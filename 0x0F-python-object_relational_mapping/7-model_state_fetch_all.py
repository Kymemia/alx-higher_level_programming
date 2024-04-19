#!/usr/bin/python3

"""This is a script that lists all state objects from DB, hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_states(username, password, database_name):
    """lists all the state objects from hbtn_0e_6_usa.
    Args:
        username (str): Username for connecting to the MySQL server
        password (str): The password for connecting to the MySQL server
        database_name (str): The name of the database

    Returns:
        None"""
    engine = create_engine('mysql+mysqldb://{}:@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3],
                            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session() #session creation

    #extraction of states
    states = session.query(State).order_by(State_id).all()

    #loop to print all states
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()

if __name == "__main__":
    """condition to check accurate number of arguments"""
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
