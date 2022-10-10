#!/usr/bin/python3
"""
    script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
        prints the State object with the name passed
        as argument from the database hbtn_0e_6_usa
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
    filteredQuery = query.filter(State.name == sys.argv[4])
    orderedQuery = filteredQuery.order_by(State.id)
    if orderedQuery.count() == 0:
        print("Not found")
    else:
        results = orderedQuery.all()
        for state in results:
            print(state.id)
    session.close()


if __name__ == "__main__":
    main()
