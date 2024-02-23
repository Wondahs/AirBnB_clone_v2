#!/usr/bin/python3
'''Module containing User Class'''
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import Relationship


class User(BaseModel, Base):
    '''User Class'''
    __tablename__ = "users"
    email: str = Column(String(128), nullable=False)
    password: str = Column(String(128), nullable=False)
    first_name: str = Column(String(128))
    last_name: str = Column(String(128))
    # One to many relationship with Place
    places = Relationship("Place", backref="user", cascade="all, delete-orphan")
    # One to many relationship with Review
    reviews = Relationship("Review", backref="user", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        '''Instantiation Method'''
        super().__init__(*args, **kwargs)
