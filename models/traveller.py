from main import db

class Traveller(db.Model):
    __tablename__ = "traveller"
    traveller_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True)
    notes = db.Column(db.String(500))

    trip_travellers = db.relationship("TripTraveller", back_populates="traveller", cascade="all, delete-orphan")