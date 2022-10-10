#!/usr/bin/python3
"""
    class definition of a State
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false


Base = declarative_base()


class State(Base):
    """
        State class
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=True,
        nullable=True,
        primary_key=True,
        unique=True
    )
    name = Column(String(128), nullable=False)
