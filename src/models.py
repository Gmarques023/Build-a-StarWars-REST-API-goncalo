from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
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


