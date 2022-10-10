#!/usr/bin/python3
"""
    a script that prints all City objects from the database hbtn_0e_14_usa
"""


from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
        a script prints all City objects from the database hbtn_0e_14_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()
    citiesQuery = session.query(City).order_by(City.id)
    for city in citiesQuery.all():
        stateQuery = session.query(State).filter(State.id == city.state_id)
        if stateQuery.count() > 0:
            state = stateQuery.first()
            print("{}: ({:d}) {}".format(state.name, city.id, city.name))
    session.close()

if __name__ == "__main__":
    main()
