from main import db

class TransportBooking(db.Model):
    __tablename__ = "transport_booking"
    transport_id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.trip_id"), nullable=False)
    transport_type = db.Column(db.String(50), nullable=False)
    from_location = db.Column(db.String(100), nullable=False)
    to_location = db.Column(db.String(100), nullable=False)
    departure_datetime = db.Column(db.DateTime, nullable=False)
    arrival_datetime = db.Column(db.DateTime, nullable=False)
    carrier_name = db.Column(db.String(100))
    booking_reference = db.Column(db.String(50))
    cost_total = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    currency_code = db.Column(db.String(3), nullable=False)

    trip = db.relationship("Trip", back_populates="transport_booking")