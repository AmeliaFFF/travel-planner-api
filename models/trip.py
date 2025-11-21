from main import db

class Trip(db.Model):
    __tablename__ = "trip"
    trip_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    primary_destination = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    budget_amount = db.Column(db.Numeric(precision=10, scale=2))
    currency_code = db.Column(db.String(3), nullable=False)
    notes = db.Column(db.String(500))

    user = db.relationship("User", back_populates="trips")
    accommodation_bookings = db.relationship("AccommodationBooking", back_populates="trip", cascade="all, delete-orphan")
    transport_bookings = db.relationship("TransportBooking", back_populates="trip", cascade="all, delete-orphan")
    itinerary_items = db.relationship("ItineraryItem", back_populates="trip", cascade="all, delete-orphan")
    expenses = db.relationship("Expense", back_populates="trip", cascade="all, delete-orphan")
    trip_travellers = db.relationship("TripTraveller", back_populates="trip", cascade="all, delete-orphan")