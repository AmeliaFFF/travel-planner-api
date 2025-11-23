from flask import Blueprint, jsonify, request, abort
from main import db
from models.trip_traveller import TripTraveller
from models.trip import Trip
from models.traveller import Traveller
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

# POST a new trip traveller
@trip_travellers.route("/", methods=["POST"])
def create_trip_traveller():
    body_data = request.get_json()
    # Check all required fields are present
    required_fields = ["trip_id", "traveller_id"]
    missing = [field for field in required_fields if field not in body_data]
    if missing:
        return jsonify({
            "error": "Missing required field(s).",
            "missing_fields": missing,
            "example_required_format": {
                "trip_id": 1,
                "traveller_id": 2,
            }
        }), 400
    new_trip_traveller = trip_traveller_schema.load(body_data, session=db.session)
    # Check that the trip exists
    trip = Trip.query.get(new_trip_traveller.trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{new_trip_traveller.trip_id} does not exist."}), 404
    # Check that the traveller exists
    traveller = Traveller.query.get(new_trip_traveller.traveller_id)
    if not traveller:
        return jsonify({"error": f"Traveller with ID #{new_trip_traveller.traveller_id} does not exist."}), 404
    # Check if this trip/traveller combo already exists
    existing = TripTraveller.query.get((new_trip_traveller.trip_id, new_trip_traveller.traveller_id))
    if existing:
        return jsonify({"error": "This traveller is already linked to this trip."}), 400
    # Save and submit
    db.session.add(new_trip_traveller)
    db.session.commit()
    return trip_traveller_schema.dump(new_trip_traveller), 201

# PATCH an existing trip traveller by ID
@trip_travellers.route("/<int:trip_id>/<int:traveller_id>", methods=["PATCH"])
def update_trip_traveller(trip_id, traveller_id):
    trip_traveller = TripTraveller.query.get((trip_id, traveller_id))
    if not trip_traveller:
        return jsonify({"error": f"Trip traveller with Trip ID #{trip_id} and Traveller ID #{traveller_id} does not exist."}), 404
    body_data = request.get_json()
    allowed_fields = {"role"}
    sent_fields = set(body_data.keys())
    disallowed = sent_fields - allowed_fields
    if disallowed:
        return jsonify({
            "error": "These fields cannot be updated.",
            "invalid_fields": list(disallowed),
            "allowed_updatable_field": ["role"],
            "example_format": {
                "role": "friend"
            }
        }), 400
    if "role" not in body_data:
        return jsonify({
            "error": "Missing required field.",
            "required_updatable_field": "role",
            "example_format": {
                "role": "friend"
            }
        }), 400
    trip_traveller.role = body_data["role"]
    db.session.commit()
    return trip_traveller_schema.dump(trip_traveller), 200

# DELETE an existing trip traveller by ID
@trip_travellers.route("/<int:trip_id>/<int:traveller_id>", methods=["DELETE"])
def delete_trip_traveller(trip_id, traveller_id):
    trip_traveller = TripTraveller.query.get((trip_id, traveller_id))
    if not trip_traveller:
        return jsonify({"error": f"No link exists between Trip ID #{trip_id} and Traveller ID #{traveller_id}."}), 404
    db.session.delete(trip_traveller)
    db.session.commit()
    return jsonify({
        "message": f"Traveller #{traveller_id} removed from Trip #{trip_id}."
    }), 200

# DELETE fallback route when only one ID is provided
@trip_travellers.route("/<int:id>", methods=["DELETE"])
def invalid_trip_traveller_delete(id):
    return jsonify({
        "error": "This endpoint requires 2 IDs: /trip-travellers/<trip_id>/<traveller_id>",
        "example": "/trip-travellers/1/2",
        "received": id
    }), 400