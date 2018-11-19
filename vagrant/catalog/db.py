from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Topic(Base):
  __tablename__ = 'topic'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)

  @property
  def serialize(self):
    return {
      id: self.id,
      name: self.name
    }


class Article(Base):
  __tablename__ = 'article'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)

  @property
  def serialize(self):
    return {
      id: self.id,
      name: self.name
    }