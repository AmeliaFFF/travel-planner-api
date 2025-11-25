from main import db

class AccommodationBooking(db.Model):
    """Represents an accommodation booking for a trip."""
    __tablename__ = "accommodation_booking"
    accommodation_id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.trip_id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255))
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    booking_reference = db.Column(db.String(50))
    cost_total = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    currency_code = db.Column(db.String(3), nullable=False)

    trip = db.relationship("Trip", back_populates="accommodation_bookings")