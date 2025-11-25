from flask import Blueprint, jsonify, request
from main import db
from models.traveller import Traveller
from models.trip import Trip
from models.trip_traveller import TripTraveller
from schemas.traveller_schema import traveller_schema, travellers_schema
from schemas.trip_schema import trip_schema, trips_schema
from schemas.trip_traveller_schema import trip_traveller_schema, trip_travellers_schema

travellers = Blueprint("travellers", __name__, url_prefix="/travellers")

@travellers.route("/", methods=["GET"])
def get_travellers():
    """Retrieves all travellers."""
    stmt = db.select(Traveller)
    travellers_list = db.session.scalars(stmt)
    result = travellers_schema.dump(travellers_list)
    return jsonify(result), 200

@travellers.route("/<int:traveller_id>", methods=["GET"])
def get_traveller(traveller_id):
    """Retrieves a single traveller by their traveller_id."""
    traveller = Traveller.query.get(traveller_id)
    if not traveller:
        return jsonify({"error": f"Traveller with ID #{traveller_id} does not exist."}), 404
    result = traveller_schema.dump(traveller)
    return jsonify(result), 200

@travellers.route("/<int:traveller_id>/trips", methods=["GET"])
def get_trips_for_traveller(traveller_id):
    """Retrieves all trips for a specific traveller by their traveller_id."""
    # Check that the traveller actually exists
    traveller = Traveller.query.get(traveller_id)
    if not traveller:
        return jsonify({"error": f"Traveller with ID #{traveller_id} does not exist."}), 404
    # Fetch all trip-traveller links for this traveller
    stmt = db.select(TripTraveller).filter_by(traveller_id=traveller_id)
    links = db.session.scalars(stmt)
    # Extract trips
    trips = [link.trip for link in links]
    # If the traveller exists but is not part of any trips
    if len(trips) == 0:
        return jsonify({
            "message": f"Traveller with ID #{traveller_id} is not part of any trips."
        }), 200
    return jsonify(trips_schema.dump(trips)), 200

@travellers.route("/", methods=["POST"])
def create_traveller():
    """Creates a new traveller."""
    body_data = request.get_json()
    new_traveller = traveller_schema.load(body_data, session=db.session)
    db.session.add(new_traveller)
    db.session.commit()
    return traveller_schema.dump(new_traveller), 201

@travellers.route("/<int:traveller_id>", methods=["PATCH"])
def update_traveller(traveller_id):
    """Updates specified fields of an existing traveller."""
    traveller = Traveller.query.get(traveller_id)
    if not traveller:
        return jsonify({"error": f"Traveller with ID #{traveller_id} does not exist."}), 404
    body_data = request.get_json()
    traveller = traveller_schema.load(body_data, instance=traveller, session=db.session, partial=True)
    db.session.commit()
    return traveller_schema.dump(traveller), 200

@travellers.route("/<int:traveller_id>", methods=["DELETE"])
def delete_traveller(traveller_id):
    """Deletes an existing traveller."""
    traveller = Traveller.query.get(traveller_id)
    if not traveller:
        return jsonify({"error": f"Traveller with ID #{traveller_id} does not exist."}), 404
    db.session.delete(traveller)
    db.session.commit()
    return jsonify({"message": f"Traveller with ID #{traveller_id} deleted successfully."}), 200