#!/usr/bin/python3
"""This is the county class"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class County(BaseModel, Base):
    """This is the class for County
    Attributes:
        name: name of county
        province_id: province id
    """
    __tablename__ = "counties"
    name = Column(String(128), nullable=False)
    province_id = Column(String(60), ForeignKey('provinces.id'), nullable=False)

