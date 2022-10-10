#!/usr/bin/python3
"""
    script that lists all State objects
    that contain the letter a from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
        lists all State objects that contain the letter a
        from the database hbtn_0e_6_usa
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
    query = session.query(State)
    filteredQuery = query.filter(State.name.like('%a%'))
    orderedQuery = filteredQuery.order_by(State.id)
    for state in orderedQuery.all():
        print("{:d}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    main()
