# lib/seed.py
import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Game

fake = Faker()

engine = create_engine('sqlite:///seed_db.db')
Session = sessionmaker(bind=engine)
session = Session()

print("Seeding games...")

# Delete everything before reseeding
session.query(Game).delete()
session.commit()

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for i in range(50)
]

session.bulk_save_objects(games)
session.commit()

print("Seeding complete!")
