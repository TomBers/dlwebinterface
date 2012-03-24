from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, LargeBinary, Text, Integer, Date

Base = declarative_base()

class Asset(Base):
	__tablename__ = "assets"
	
	id = Column(Integer, primary_key=True)
	vendor = Column(String)
	description = Column(Text)
	installer = Column(String)
	serial_number = Column(String)
	purchase_date = Column(Date)
	install_date = Column(Date)
	quantity = Column(Text)
	
	def __init__(self, vendor, description, installer):
		self.vendor = vendor
		self.description = description
		self.installer = installer
	
	def __repr__(self):
		return "<Asset( '%s', '%s', '%s' )>" % (self.vendor, self.descripton, self.installer)
	