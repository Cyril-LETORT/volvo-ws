from . import DB_BASE

from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, Boolean

"""
Create staff,  customer, vehicle and inquiry models for an API, 
which enables the customers to leave inquiries regardinga vehicle they are interested in,
to which staff can then respond.
"""
