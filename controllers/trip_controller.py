from flask import Blueprint, jsonify, request, abort
from main import db
from models.trip import Trip
from models.user import User
from schemas.trip_schema import trip_schema, trips_schema

trips = Blueprint("trips", __name__, url_prefix="/trips")

@trips.route("/", methods=["GET"])
def get_trips():
    """Retrieves all trips."""
    stmt = db.select(Trip)
    trips_list = db.session.scalars(stmt)
    result = trips_schema.dump(trips_list)
    return jsonify(result), 200

@trips.route("/<int:trip_id>", methods=["GET"])
def get_trip(trip_id):
    """Retrieves a single trip by its trip_id."""
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{trip_id} does not exist."}), 404
    result = trip_schema.dump(trip)
    return jsonify(result), 200

@trips.route("/user/<int:user_id>", methods=["GET"])
def get_trips_for_user(user_id):
    """Retrieves all trips created by a specific user_id."""
    # Check that the user actually exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": f"User with ID #{user_id} does not exist."}), 404
    # Fetch all trips for this user
    stmt = db.select(Trip).filter_by(user_id=user_id)
    trips_list = db.session.scalars(stmt)
    result = trips_schema.dump(trips_list)
    # If the user exists but has no trips
    if len(result) == 0:
        return jsonify({
            "message": f"User with ID #{user_id} has no trips."
        }), 200
    # Return the user's trips
    return jsonify(result), 200

@trips.route("/", methods=["POST"])
def create_trip():
    """Creates a new trip."""
    body_data = request.get_json()
    new_trip = trip_schema.load(body_data, session=db.session)
    db.session.add(new_trip)
    db.session.commit()
    return trip_schema.dump(new_trip), 201

@trips.route("/<int:trip_id>", methods=["PATCH"])
def update_trip(trip_id):
    """Updates specified fields of an existing trip."""
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{trip_id} does not exist."}), 404
    body_data = request.get_json()
    trip = trip_schema.load(body_data, instance=trip, session=db.session, partial=True)
    db.session.commit()
    return trip_schema.dump(trip), 200

@trips.route("/<int:trip_id>", methods=["DELETE"])
def delete_trip(trip_id):
    """Deletes an existing trip and all associated data."""
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{trip_id} does not exist."}), 404
    db.session.delete(trip)
    db.session.commit()
    return jsonify({"message": f"Trip with ID #{trip_id} deleted successfully."}), 200