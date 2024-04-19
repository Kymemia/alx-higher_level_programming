#!/usr/bin/python3

"""This is a script that lists all state objects from DB, hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3],
                            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State).order_by(State_id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
