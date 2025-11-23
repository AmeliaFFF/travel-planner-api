from flask import Blueprint, jsonify, request, abort
from main import db
from models.transport import TransportBooking
from models.trip import Trip
from schemas.transport_schema import transport_booking_schema, transport_bookings_schema

transport_bookings = Blueprint("transport_bookings", __name__, url_prefix="/transport-bookings")

# GET all transport bookings
@transport_bookings.route("/", methods=["GET"])
def get_transport_bookings():
    stmt = db.select(TransportBooking)
    transport_bookings_list = db.session.scalars(stmt)
    result = transport_bookings_schema.dump(transport_bookings_list)
    return jsonify(result), 200

# GET a single transport booking by ID
@transport_bookings.route("/<int:transport_booking_id>", methods=["GET"])
def get_transport_booking(transport_booking_id):
    transport_booking = TransportBooking.query.get(transport_booking_id)
    if not transport_booking:
        return jsonify({"error": f"Transport booking with ID #{transport_booking_id} does not exist."}), 404
    result = transport_booking_schema.dump(transport_booking)
    return jsonify(result), 200

# GET all transport bookings for a specific trip by trip ID
@transport_bookings.route("/trip/<int:trip_id>", methods=["GET"])
def get_transport_bookings_for_trip(trip_id):
    # Check that the trip actually exists
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{trip_id} does not exist."}), 404
    # Fetch all transport bookings for this trip
    stmt = db.select(TransportBooking).filter_by(trip_id=trip_id)
    transport_bookings_list = db.session.scalars(stmt)
    result = transport_bookings_schema.dump(transport_bookings_list)
    # If the trip exists but has no transport bookings
    if len(result) == 0:
        return jsonify({
            "message": f"Trip with ID #{trip_id} has no transport bookings."
        }), 200
    # Return the trip's transport bookings
    return jsonify(result), 200

# POST a new transport booking
@transport_bookings.route("/", methods=["POST"])
def create_transport_booking():
    body_data = request.get_json()
    new_transport_booking = transport_booking_schema.load(body_data, session=db.session)
    db.session.add(new_transport_booking)
    db.session.commit()
    return transport_booking_schema.dump(new_transport_booking), 201

# PATCH an existing transport booking by ID
@transport_bookings.route("/<int:transport_booking_id>", methods=["PATCH"])
def update_transport_booking(transport_booking_id):
    transport_booking = TransportBooking.query.get(transport_booking_id)
    if not transport_booking:
        return jsonify({"error": f"Transport booking with ID #{transport_booking_id} does not exist."}), 404
    body_data = request.get_json()
    transport_booking = transport_booking_schema.load(body_data, instance=transport_booking, session=db.session, partial=True)
    db.session.commit()
    return transport_booking_schema.dump(transport_booking), 200

# DELETE an existing transport booking by ID
@transport_bookings.route("/<int:transport_booking_id>", methods=["DELETE"])
def delete_transport_booking(transport_booking_id):
    transport_booking = TransportBooking.query.get(transport_booking_id)
    if not transport_booking:
        return jsonify({"error": f"Transport booking with ID #{transport_booking_id} does not exist."}), 404
    db.session.delete(transport_booking)
    db.session.commit()
    return jsonify({"message": f"Transport booking with ID #{transport_booking_id} deleted successfully."}), 200