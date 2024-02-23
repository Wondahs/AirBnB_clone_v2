#!/usr/bin/python3
'''Module containing Amenity Class'''
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import Relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    '''Amenity Class'''
    __tablename__ = "amenities"
    name: str = Column(String(128), nullable=False)
    place_amenities = Relationship("Place", secondary=place_amenity,
                                   viewonly=False, overlaps="amenities")

    def __init__(self, *args, **kwargs):
        '''Instantiation Method'''
        super().__init__(*args, **kwargs)
