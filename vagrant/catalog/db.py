from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Topic(Base):
  __tablename__ = 'topic'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)
  url = Column(String(250), nullable = False)
  image = Column(String(250))

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'url': self.url,
      'image': self.image
    }


class Category(Base):
  __tablename__ = 'category'

  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)
  url = Column(String(250), nullable = False)
  image = Column(String(250))
  topic_id = Column(Integer, ForeignKey('topic.id'))
  topic = relationship(Topic)

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'url': self.url,
      'image': self.image,
      'topic_id': self.topic_id,
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
      'category_id': self.category_id,
    }


class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)
  email = Column(String(250), nullable=False)
  picture = Column(String(250))


engine = create_engine('sqlite:///compscicatalog.db')
Base.metadata.create_all(engine)