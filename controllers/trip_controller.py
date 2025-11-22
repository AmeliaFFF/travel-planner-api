from flask import Blueprint, jsonify, request, abort
from main import db
from models.trip import Trip
from schemas.trip_schema import trip_schema, trips_schema

trips = Blueprint("trips", __name__, url_prefix="/trips")

# GET all trips
@trips.route("/", methods=["GET"])
def get_trips():
    stmt = db.select(Trip)
    trips_list = db.session.scalars(stmt)
    result = trips_schema.dump(trips_list)
    return jsonify(result), 200