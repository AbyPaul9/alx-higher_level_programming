#!/usr/bin/python3
"""
    class definition of a State
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false
from sqlalchemy.orm import relationship
from relationship_city import Base, City


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
    cities = relationship("City", backref="state", cascade="all, delete")
