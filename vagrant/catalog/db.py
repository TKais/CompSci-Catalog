from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Topic(Base):
  __tablename__ = 'topic'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name
    }


class Category(Base):
  __tablename__ = 'category'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)
  topic_id = Column(Integer, ForeignKey('topic.id'))
  topic = relationship(Topic)

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name
    }


class Article(Base):
  __tablename__ = 'article'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)
  content = Column(String(250), nullable = False)
  category_id = Column(Integer, ForeignKey('category.id'))
  category = relationship(Category)

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'content': self.content,
    }


engine = create_engine('sqlite:///cstopics.db')
Base.metadata.create_all(engine)