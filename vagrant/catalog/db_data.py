from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base, Topic

engine = create_engine('sqlite:///compscicatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

AI = Topic(name='Artificial Intelligence')
session.add(AI)
session.commit()

human_computer_interaction = Topic(name='Human Computer Interaction')
session.add(human_computer_interaction)
session.commit()

print('Database data populated')