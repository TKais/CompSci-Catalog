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

database_systems = Topic(name='Database Systems')
session.add(database_systems)
session.commit()

programming_languages = Topic(name='Programming Languages')
session.add(programming_languages)
session.commit()

computer_systems_networks = Topic(name='Computer Systems and Networks')
session.add(computer_systems_networks)
session.commit()

software_engineering = Topic(name='Software Engineering')
session.add(software_engineering)
session.commit()

vision_graphics = Topic(name='Vision and Graphics')
session.add(vision_graphics)
session.commit()

numerical_analysis = Topic(name='Numerical Analysis')
session.add(numerical_analysis)
session.commit()

theory_of_computing = Topic(name='Theory of Computing')
session.add(theory_of_computing)
session.commit()

bioinformatics = Topic(name='Bioinformatics')
session.add(bioinformatics)
session.commit()

print('Database data populated')