from main import db

class TripTraveller(db.Model):
    __tablename__ = "trip_traveller"
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.trip_id"), primary_key=True)
    traveller_id = db.Column(db.Integer, db.ForeignKey("traveller.traveller_id"), primary_key=True)
    role = db.Column(db.String(50))

    trip = db.relationship("Trip", back_populates="trip_traveller")
    traveller = db.relationship("Traveller", back_populates="trip_traveller")