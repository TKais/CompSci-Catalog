from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base, Topic

engine = create_engine('sqlite:///cstopics.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

AI = Topic(name='Artificial Intelligence')
session.add(AI)
session.commit()

print('Dummy data populated')