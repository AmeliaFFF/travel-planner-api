from flask import Blueprint, jsonify, request, abort
from main import db
from models.transport import TransportBooking
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