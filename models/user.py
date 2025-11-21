from main import db

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    trips = db.relationship("Trip", back_populates="user", cascade="all, delete-orphan")