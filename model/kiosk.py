from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Kiosk(Base):
	__tablename__ = "kiosks"
	
	id = Column(Integer, primary_key=True)
	location = Column(String)
	lat = Column(Float)
	long = Column(Float)
	
	def __init__(self, location, lat, long):
		self.location = location
		self.lat = lat
		self.long = long
	
	def __repr__(self):
		return "<Kiosk( '%s', '%s', '%s' )>" % (self.location, self.lat, self.long)


	