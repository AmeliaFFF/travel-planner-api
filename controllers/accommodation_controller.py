from flask import Blueprint, jsonify, request
from main import db
from models.accommodation import AccommodationBooking
from models.trip import Trip
from schemas.accommodation_schema import accommodation_booking_schema, accommodation_bookings_schema

accommodation_bookings = Blueprint("accommodation_bookings", __name__, url_prefix="/accommodation-bookings")

@accommodation_bookings.route("/", methods=["GET"])
def get_accommodation_bookings():
    """Retrieves all accommodation bookings, ordered by check-in date."""
    stmt = db.select(AccommodationBooking).order_by(AccommodationBooking.check_in_date)
    accommodation_bookings_list = db.session.scalars(stmt)
    result = accommodation_bookings_schema.dump(accommodation_bookings_list)
    return jsonify(result), 200

@accommodation_bookings.route("/<int:accommodation_booking_id>", methods=["GET"])
def get_accommodation_booking(accommodation_booking_id):
    """Retrieves a single accommodation booking by its accommodation_booking_id."""
    accommodation_booking = AccommodationBooking.query.get(accommodation_booking_id)
    if not accommodation_booking:
        return jsonify({"error": f"Accommodation booking with ID #{accommodation_booking_id} does not exist."}), 404
    result = accommodation_booking_schema.dump(accommodation_booking)
    return jsonify(result), 200

@accommodation_bookings.route("/trip/<int:trip_id>", methods=["GET"])
def get_accommodation_bookings_for_trip(trip_id):
    """Retrieves all accommodation bookings for a specific trip by its trip_id."""
    # Check that the trip actually exists
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{trip_id} does not exist."}), 404
    # Fetch all accommodation bookings for this trip
    stmt = (db.select(AccommodationBooking).filter_by(trip_id=trip_id).order_by(AccommodationBooking.check_in_date))
    accommodation_bookings_list = db.session.scalars(stmt)
    result = accommodation_bookings_schema.dump(accommodation_bookings_list)
    # If the trip exists but has no accommodation bookings
    if len(result) == 0:
        return jsonify({
            "message": f"Trip with ID #{trip_id} has no accommodation bookings."
        }), 200
    # Return the trip's accommodation bookings
    return jsonify(result), 200

@accommodation_bookings.route("/", methods=["POST"])
def create_accommodation_booking():
    """Creates a new accommodation booking."""
    body_data = request.get_json()
    new_accommodation_booking = accommodation_booking_schema.load(body_data, session=db.session)
    db.session.add(new_accommodation_booking)
    db.session.commit()
    return accommodation_booking_schema.dump(new_accommodation_booking), 201

@accommodation_bookings.route("/<int:accommodation_booking_id>", methods=["PATCH"])
def update_accommodation_booking(accommodation_booking_id):
    """Updates specified fields of an existing accommodation booking."""
    accommodation_booking = AccommodationBooking.query.get(accommodation_booking_id)
    if not accommodation_booking:
        return jsonify({"error": f"Accommodation booking with ID #{accommodation_booking_id} does not exist."}), 404
    body_data = request.get_json()
    accommodation_booking = accommodation_booking_schema.load(body_data, instance=accommodation_booking, session=db.session, partial=True)
    db.session.commit()
    return accommodation_booking_schema.dump(accommodation_booking), 200

@accommodation_bookings.route("/<int:accommodation_booking_id>", methods=["DELETE"])
def delete_accommodation_booking(accommodation_booking_id):
    """Deletes an existing accommodation booking."""
    accommodation_booking = AccommodationBooking.query.get(accommodation_booking_id)
    if not accommodation_booking:
        return jsonify({"error": f"Accommodation booking with ID #{accommodation_booking_id} does not exist."}), 404
    db.session.delete(accommodation_booking)
    db.session.commit()
    return jsonify({"message": f"Accommodation booking with ID #{accommodation_booking_id} deleted successfully."}), 200