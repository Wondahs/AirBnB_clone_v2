#!/usr/bin/python3
'''Module containing Review Class'''
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Relationship


class Review(BaseModel, Base):
    '''Review Class'''
    __tablename__ = "reviews"
    place_id: str = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id: str = Column(String(60), ForeignKey("users.id"), nullable=False)
    text: str = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        '''Instantiation Method'''
        super().__init__(*args, **kwargs)
