#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []


'''
        @property
        def reviews(self):
            """
            """
            review_list = []
            for review in models.storage.all('Review').values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            """
            return self.amenity_ids

        @amenity.setter
        def amenities(Self, value):
            """
            """
            for amenity in models.storage.all('Amenity').values():
                if amenity.id == self.id:
                    amenity_ids.append(amenity)

place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
                        primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
                        primary_key=True, nullable=False),
)

        reviews = relationship("Review", back_populates="place",
                                cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                  secondary=place_amenity, viewonly=False)
'''
