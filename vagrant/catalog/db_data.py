from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base, Topic, Category, Article

engine = create_engine('sqlite:///compscicatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

AI = Topic(name='Artificial Intelligence', url='Artificial-Intelligence')
session.add(AI)
session.commit()

supervised_learning = Category(name='Supervised Learning', url='Supervised-Learning', topic_id=1)
session.add(supervised_learning)
session.commit()

unsupervised_learning = Category(name='Unsupervised Learning', url='Unupervised-Learning', topic_id=1)
session.add(unsupervised_learning)
session.commit()

human_computer_interaction = Topic(name='Human Computer Interaction', url='Human-Computer-Interaction')
session.add(human_computer_interaction)
session.commit()

augmented_reality = Category(name='Augmented Reality', url='Augmented-Reality', topic_id=2)
session.add(augmented_reality)
session.commit()

database_systems = Topic(name='Database Systems', url='Database-Systems')
session.add(database_systems)
session.commit()

relational_model = Category(name='Relational Model', url='Relational-Model', topic_id=3)
session.add(relational_model)
session.commit()

programming_languages = Topic(name='Programming Languages', url='Programming-Languages')
session.add(programming_languages)
session.commit()

python = Category(name='Python', url='Python', topic_id=4)
session.add(python)
session.commit()

computer_systems_networks = Topic(name='Computer Systems and Networks', url='Computer-Systems-Networks')
session.add(computer_systems_networks)
session.commit()

communication_networks = Category(name='Communication Networks', url='Communication-Networks', topic_id=5)
session.add(communication_networks)
session.commit()

software_engineering = Topic(name='Software Engineering', url='Software-Engineering')
session.add(software_engineering)
session.commit()

testing = Category(name='Testing', url='Testing', topic_id=6)
session.add(testing)
session.commit()

vision_graphics = Topic(name='Vision and Graphics', url='Vision-and-Graphics')
session.add(vision_graphics)
session.commit()

computer_vision = Category(name='Computer Vision', url='Computer-Vision', topic_id=7)
session.add(computer_vision)
session.commit()

numerical_analysis = Topic(name='Numerical Analysis', url='Numerical-Analysis')
session.add(numerical_analysis)
session.commit()

differential_equations = Category(name='Differential Equations', url='Differential-Equations', topic_id=8)
session.add(differential_equations)
session.commit()

theory_of_computing = Topic(name='Theory of Computing', url='Theory-of-Computing')
session.add(theory_of_computing)
session.commit()

computational_complexity_theory = Category(name='Computational Complexity Theory', url='Computational-Complexity-Theory', topic_id=9)
session.add(computational_complexity_theory)
session.commit()

bioinformatics = Topic(name='Bioinformatics', url='Bioinformatics')
session.add(bioinformatics)
session.commit()

DNA_sequencing = Category(name='DNA sequencing', url='DNA-Sequencing', topic_id=10)
session.add(DNA_sequencing)
session.commit()

print('Database data populated')