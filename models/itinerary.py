from main import db

class ItineraryItem(db.Model):
    __tablename__ = "itinerary_item"
    itinerary_item_id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.trip_id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50)) 
    location = db.Column(db.String(255))
    notes = db.Column(db.String(500))
    cost_total = db.Column(db.Numeric(precision=10, scale=2))
    currency_code = db.Column(db.String(3))

    trip = db.relationship("Trip", back_populates="itinerary_item")