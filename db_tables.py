from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime


base = declarative_base()


class Trips(base):
    __tablename__ = 'trips'
    __table_args__ = {'schema': 'neuralworks'}
    trip_id = Column(Integer, primary_key=True)
    region = Column(String)
    origin_lat = Column(Float)
    origin_lon = Column(Float)
    dest_lat = Column(Float)
    dest_lon = Column(Float)
    datetime = Column(DateTime)
    datasource = Column(String)

