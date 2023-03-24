#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Place class to store information on all AirBnB listings """
    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
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

        @property
        def reviews(self):
            """ Returns list of Review instances with place_id == Place.id"""
            review_list = []
            for review in models.storage.all('Review').values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            """
            amenity_list = []
            for key, amenity in models.storage.all('Amenity').items():
                if amenity.place_id == self.id:
                # if key.split('.')[1] in self.amenity_ids:
                    amenity_list.append(amenity.id)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity=None):
            """
            """
            if amenity and type(amenity).__name__ == "Amenity":
                # for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    self.amenity_ids.append(amenity.id)
