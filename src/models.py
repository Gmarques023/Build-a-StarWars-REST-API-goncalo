from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)
    peoples = db.relationship('People', backref='user', lazy=True)
    planets = db.relationship('Planets', backref='user', lazy=True)
    

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
        }
    
class Planets(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(250),nullable=False)
    population=db.Column(db.Integer)
    terrain=db.Column(db.String(250))
    climate=db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "population":self.population,
            "terrain": self.terrain,
            "climate":self.climate
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    favorite_planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    favorite_people_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favorite_planet_id": self.favorite_planet_id,
            "favorite_people_id": self.favorite_people_id,
        }