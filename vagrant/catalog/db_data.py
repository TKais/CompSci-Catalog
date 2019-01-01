from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import url_for

from db import Base, Topic, Category, Article

engine = create_engine('sqlite:///compscicatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

AI = Topic(name='Artificial Intelligence', url='Artificial-Intelligence', image='AI.jpeg')
session.add(AI)
session.commit()

supervised_learning = Category(name='Supervised Learning', url='Supervised-Learning', topic_id=1, image='supervised.png')
session.add(supervised_learning)
session.commit()

neural_networks = Article(name='Neural Networks', category_id=1, content='Artificial neural networks (ANN) or connectionist systems are computing systems vaguely inspired by the biological neural networks that constitute animal brains.[1] The neural network itself is not an algorithm, but rather a framework for many different machine learning algorithms to work together and process complex data inputs.[2] Such systems "learn" to perform tasks by considering examples, generally without being programmed with any task-specific rules. For example, in image recognition, they might learn to identify images that contain cats by analyzing example images that have been manually labeled as "cat" or "no cat" and using the results to identify cats in other images. They do this without any prior knowledge about cats, for example, that they have fur, tails, whiskers and cat-like faces. Instead, they automatically generate identifying characteristics from the learning material that they process.')
session.add(neural_networks)
session.commit()

unsupervised_learning = Category(name='Unsupervised Learning', url='Unupervised-Learning', topic_id=1, image='unsupervised.png')
session.add(unsupervised_learning)
session.commit()

human_computer_interaction = Topic(name='Human Computer Interaction', url='Human-Computer-Interaction', image='human-computer.jpg')
session.add(human_computer_interaction)
session.commit()

augmented_reality = Category(name='Augmented Reality', url='Augmented-Reality', topic_id=2, image='augmented-reality.jpg')
session.add(augmented_reality)
session.commit()

database_systems = Topic(name='Database Systems', url='Database-Systems', image='db.png')
session.add(database_systems)
session.commit()

relational_model = Category(name='Relational Model', url='Relational-Model', topic_id=3, image='relational.jpg')
session.add(relational_model)
session.commit()

programming_languages = Topic(name='Programming Languages', url='Programming-Languages', image='languages.jpg')
session.add(programming_languages)
session.commit()

python = Category(name='Python', url='Python', topic_id=4, image='python.png')
session.add(python)
session.commit()

computer_systems_networks = Topic(name='Computer Systems and Networks', url='Computer-Systems-Networks', image='networks.jpg')
session.add(computer_systems_networks)
session.commit()

communication_networks = Category(name='Communication Networks', url='Communication-Networks', topic_id=5, image='comm-networks.jpg')
session.add(communication_networks)
session.commit()

software_engineering = Topic(name='Software Engineering', url='Software-Engineering', image='software-engineering.jpg')
session.add(software_engineering)
session.commit()

testing = Category(name='Testing', url='Testing', topic_id=6, image='testing.png')
session.add(testing)
session.commit()

vision_graphics = Topic(name='Vision and Graphics', url='Vision-and-Graphics', image='vision.jpg')
session.add(vision_graphics)
session.commit()

computer_vision = Category(name='Computer Vision', url='Computer-Vision', topic_id=7, image='vision2.jpg')
session.add(computer_vision)
session.commit()

numerical_analysis = Topic(name='Numerical Analysis', url='Numerical-Analysis', image='numerical.jpg')
session.add(numerical_analysis)
session.commit()

differential_equations = Category(name='Differential Equations', url='Differential-Equations', topic_id=8, image='differential.png')
session.add(differential_equations)
session.commit()

theory_of_computing = Topic(name='Theory of Computing', url='Theory-of-Computing', image='theory.jpg')
session.add(theory_of_computing)
session.commit()

computational_complexity_theory = Category(name='Computational Complexity Theory', url='Computational-Complexity-Theory', topic_id=9, image='complexity.jpg')
session.add(computational_complexity_theory)
session.commit()

bioinformatics = Topic(name='Bioinformatics', url='Bioinformatics', image='bioinformatics.jpeg')
session.add(bioinformatics)
session.commit()

DNA_sequencing = Category(name='DNA sequencing', url='DNA-Sequencing', topic_id=10, image='DNA.jpg')
session.add(DNA_sequencing)
session.commit()

print('Database data populated')