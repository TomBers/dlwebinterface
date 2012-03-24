from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, LargeBinary, Integer

Base = declarative_base()

class Operator(Base):
	__tablename__ = "operators"
	
	id = Column(Integer, primary_key=True)
	first_name = Column(String(100))
	last_name = Column(String(255))
	email = Column(String)
	telephone= Column(String)
	photo = Column(LargeBinary)
	
	def __init__(self, first_name, last_name, email, telephone):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.telephone = telephone
		self.photo = photo
	
	def __repr__(self):
		return "<Operator( '%s', '%s', '%s', '%s' )>" % (self.first_name, self.last_name, self.email, self.telephone)
	