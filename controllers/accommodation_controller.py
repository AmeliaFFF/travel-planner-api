from flask import Blueprint, jsonify, request, abort
from main import db
from models.accommodation import AccommodationBooking
from schemas.accommodation_schema import accommodation_booking_schema, accommodation_bookings_schema

accommodation_bookings = Blueprint("accommodation_bookings", __name__, url_prefix="/accommodation-bookings")

# GET all accommodation bookings
@accommodation_bookings.route("/", methods=["GET"])
def get_accommodation_bookings():
    stmt = db.select(AccommodationBooking)
    accommodation_bookings_list = db.session.scalars(stmt)
    result = accommodation_bookings_schema.dump(accommodation_bookings_list)
    return jsonify(result), 200

# GET a single accommodation booking by ID
@accommodation_bookings.route("/<int:accommodation_booking_id>", methods=["GET"])
def get_accommodation_booking(accommodation_booking_id):
    accommodation_booking = AccommodationBooking.query.get(accommodation_booking_id)
    if not accommodation_booking:
        return jsonify({"error": f"Accommodation booking with ID #{accommodation_booking_id} does not exist."}), 404
    result = accommodation_booking_schema.dump(accommodation_booking)
    return jsonify(result), 200

# POST a new accommodation booking
@accommodation_bookings.route("/", methods=["POST"])
def create_accommodation_booking():
    body_data = request.get_json()
    new_accommodation_booking = accommodation_booking_schema.load(body_data, session=db.session)
    db.session.add(new_accommodation_booking)
    db.session.commit()
    return accommodation_booking_schema.dump(new_accommodation_booking), 201