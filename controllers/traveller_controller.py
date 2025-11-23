from flask import Blueprint, jsonify, request, abort
from main import db
from models.traveller import Traveller
from schemas.traveller_schema import traveller_schema, travellers_schema

travellers = Blueprint("travellers", __name__, url_prefix="/travellers")

# GET all travellers
@travellers.route("/", methods=["GET"])
def get_travellers():
    stmt = db.select(Traveller)
    travellers_list = db.session.scalars(stmt)
    result = travellers_schema.dump(travellers_list)
    return jsonify(result), 200

# GET a single traveller by ID
@travellers.route("/<int:traveller_id>", methods=["GET"])
def get_traveller(traveller_id):
    traveller = Traveller.query.get(traveller_id)
    if not traveller:
        return jsonify({"error": f"Traveller with ID #{traveller_id} does not exist."}), 404
    result = traveller_schema.dump(traveller)
    return jsonify(result), 200