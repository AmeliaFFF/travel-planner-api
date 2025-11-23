from flask import Blueprint, jsonify, request, abort
from main import db
from models.trip_traveller import TripTraveller
from schemas.trip_traveller_schema import trip_traveller_schema, trip_travellers_schema

trip_travellers = Blueprint("trip_travellers", __name__, url_prefix="/trip-travellers")

# GET all trip travellers
@trip_travellers.route("/", methods=["GET"])
def get_trip_travellers():
    stmt = db.select(TripTraveller)
    trip_travellers_list = db.session.scalars(stmt)
    result = trip_travellers_schema.dump(trip_travellers_list)
    return jsonify(result), 200

# GET fallback route when only one ID is provided
@trip_travellers.route("/<int:id>", methods=["GET"])
def invalid_trip_traveller_usage(id):
    return jsonify({
        "error": "This endpoint requires 2 IDs: /trip-travellers/<trip_id>/<traveller_id>",
        "example": "/trip-travellers/1/2",
        "received": id
    }), 400

# GET a single trip traveller by ID
@trip_travellers.route("/<int:trip_id>/<int:traveller_id>", methods=["GET"])
def get_trip_traveller(trip_id, traveller_id):
    trip_traveller = TripTraveller.query.get((trip_id, traveller_id))
    if not trip_traveller:
        return jsonify({"error": f"Trip traveller with Trip ID #{trip_id} and Traveller ID #{traveller_id} does not exist."}), 404
    result = trip_traveller_schema.dump(trip_traveller)
    return jsonify(result), 200