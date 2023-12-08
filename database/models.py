from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base


class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    request = Column(String)
