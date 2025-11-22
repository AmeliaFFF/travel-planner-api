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