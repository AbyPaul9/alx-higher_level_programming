#!/usr/bin/python3
"""
    script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
        adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    query = session.query(State).filter(State.id == 2).order_by(State.id)
    if query.count() == 0:
        print("Not found")
    else:
        state = query.first()
        state.name = "New Mexico"
        session.add(state)
        session.commit()
    session.close()


if __name__ == "__main__":
    main()
