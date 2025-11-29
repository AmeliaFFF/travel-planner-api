from main import db

class Expense(db.Model):
    """Represents an expense incurred during a trip."""
    __tablename__ = "expense"
    expense_id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.trip_id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    cost_total = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    currency_code = db.Column(db.String(3), nullable=False)

    trip = db.relationship("Trip", back_populates="expenses")