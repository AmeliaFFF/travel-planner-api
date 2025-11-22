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