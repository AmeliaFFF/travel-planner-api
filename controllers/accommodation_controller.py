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