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
    state = State()
    state.name = "Louisiana"
    session.add(state)
    session.commit()
    print(state.id)
    session.close()


if __name__ == "__main__":
    main()
