#!/usr/bin/python3
"""
    class definition of City
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model_state import State


Base = declarative_base()


class City(Base):
    """
        City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=false)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
