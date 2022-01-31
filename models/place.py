#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship('Review', cascade='delete', backref='Place')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
    else:
        city_id = user_id = name = description = ""
        number_rooms = number_bathrooms = max_guest = price_by_night = 0
        latitude = longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ list of reviews"""
            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review.append(review)
            return review_list

        @property
        def amenities(self):
            """ list of amenities """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """ set id to perspective atrribute """
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
