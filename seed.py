from models import Cupcake, db
from app import app

# (venv) python seed.py

#Create tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
Cupcake.query.delete()

#Create cupcakes
chocolate = Cupcake(flavor = "Chocolate", size = "medium", rating = "9", image = "https://tinyurl.com/demo-cupcake")

vanilla = Cupcake(flavor = "Vanilla", size = "medium", rating = "8", image = "https://tinyurl.com/demo-cupcake")

chocolate_rasp = Cupcake(flavor = "Chocolate Raspberry", size = "medium", rating = "10", image = "https://tinyurl.com/demo-cupcake")

red_velvet = Cupcake(flavor = "Red Velvet", size = "medium", rating = "5", image = "https://tinyurl.com/demo-cupcake")

lemon = Cupcake(flavor = "Lemon", size = "medium", rating = "10", image = "https://tinyurl.com/demo-cupcake")

carrot_cake = Cupcake(flavor = "Carrot Cake", size = "medium", rating = "4", image = "https://tinyurl.com/demo-cupcake")

# Add new cupcake objects to the session
db.session.add(chocolate)
db.session.add(vanilla)
db.session.add(chocolate_rasp)
db.session.add(red_velvet)
db.session.add(lemon)
db.session.add(carrot_cake)

# Commit 
db.session.commit()