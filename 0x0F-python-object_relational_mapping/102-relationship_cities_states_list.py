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
    citiesQuery = session.query(City).order_by(City.id)
    for city in citiesQuery.all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()


if __name__ == "__main__":
    main()
