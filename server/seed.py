#!/usr/bin/env python3
#server/seed.py

from random import choice as rc
from app import app
from models import db, Pet
from faker import Faker

with app.app_context():

    # Creates and initializes the faker generator
    fake = Faker()

    # Deletes all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []


    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some Pet instances to the list
    for i in range(10):
        pet = Pet(name = fake.first_name(), species = rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()