#!/usr/bin/python3
"""This is the security class"""
from sqlalchemy import Column, Boolean, ForeignKey
from models.base_model import BaseModel, Base


class Security(BaseModel, Base):
    """This is the class for Security
    Attributes:
        place_id: place id
        guard_present: Boolean indicating if guard is present
    """
    __tablename__ = "securities"
    guard_present = Column(Boolean, default=False, nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
