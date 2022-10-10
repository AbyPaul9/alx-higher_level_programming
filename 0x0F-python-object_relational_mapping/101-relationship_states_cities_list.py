#!/usr/bin/python3
"""
    script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""


from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
        script that lists all State objects, and corresponding City objects,
        contained in the database hbtn_0e_101_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()
    statesQuery = session.query(State).order_by(State.id)
    for state in statesQuery.all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()


if __name__ == "__main__":
    main()
