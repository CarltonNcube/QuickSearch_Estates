#!/usr/bin/python3
"""This module defines all models for QuickSearch Estates"""

from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

# Define association table for Place-Amenity many-to-many relationship
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

# Define association table for Preference-Amenity many-to-many relationship
preference_amenity = Table('preference_amenity', Base.metadata,
                           Column('preference_id', String(60), ForeignKey('preferences.id'), primary_key=True, nullable=False),
                           Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class BaseModel:
    """Base model class for all models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Save the object to the database"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """Delete the object from the database"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Return dictionary representation of the object"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict


class User(BaseModel, Base):
    """User model"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    preferences = relationship("Preference", back_populates="user")


class City(BaseModel, Base):
    """City model"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")


class County(BaseModel, Base):
    """County model"""
    __tablename__ = 'counties'
    name = Column(String(128), nullable=False)
    province_id = Column(String(60), ForeignKey('provinces.id'), nullable=False)


class Province(BaseModel, Base):
    """Province model"""
    __tablename__ = 'provinces'
    name = Column(String(128), nullable=False)
    country_id = Column(String(60), ForeignKey('countries.id'), nullable=False)
    states = relationship("State", back_populates="province")


class State(BaseModel, Base):
    """State model"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    province_id = Column(String(60), ForeignKey('provinces.id'), nullable=False)
    province = relationship("Province", back_populates="states")


class Country(BaseModel, Base):
    """Country model"""
    __tablename__ = 'countries'
    name = Column(String(128), nullable=False)
    continent_id = Column(String(60), ForeignKey('continents.id'), nullable=False)
    provinces = relationship("Province", back_populates="country")


class Continent(BaseModel, Base):
    """Continent model"""
    __tablename__ = 'continents'
    name = Column(String(128), nullable=False)
    countries = relationship("Country", back_populates="continent")


class Suburb(BaseModel, Base):
    """Suburb model"""
    __tablename__ = 'suburbs'
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)


class Property(BaseModel, Base):
    """Property model"""
    __tablename__ = 'properties'
    title = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    price = Column(Float, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    area = Column(Float, nullable=False)
    address = Column(String(256), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)


class Review(BaseModel, Base):
    """Review model"""
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)


class Amenity(BaseModel, Base):
    """Amenity model"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    places = relationship("Place", secondary=place_amenity, back_populates="amenities")
    preferences = relationship("Preference", secondary=preference_amenity, back_populates="amenities")


class Place(BaseModel, Base):
    """Place model"""
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)


class Preference(BaseModel, Base):
    """Preference model"""
    __tablename__ = 'preferences'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    min_price = Column(Float, nullable=True)
    max_price = Column(Float, nullable=True)
    min_bedrooms = Column(Integer, nullable=True)
    min_bathrooms = Column(Integer, nullable=True)
    min_area = Column(Float, nullable=True)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=True)
    amenities = relationship("Amenity", secondary=preference_amenity, back_populates="preferences")

