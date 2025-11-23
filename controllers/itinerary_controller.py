from flask import Blueprint, jsonify, request, abort
from main import db
from models.itinerary import ItineraryItem
from schemas.itinerary_schema import itinerary_item_schema, itinerary_items_schema

itinerary_items = Blueprint("itinerary_items", __name__, url_prefix="/itinerary-items")

# GET all itinerary items
@itinerary_items.route("/", methods=["GET"])
def get_itinerary_items():
    stmt = db.select(ItineraryItem)
    itinerary_items_list = db.session.scalars(stmt)
    result = itinerary_items_schema.dump(itinerary_items_list)
    return jsonify(result), 200

# GET a single itinerary item by ID
@itinerary_items.route("/<int:itinerary_item_id>", methods=["GET"])
def get_itinerary_item(itinerary_item_id):
    itinerary_item = ItineraryItem.query.get(itinerary_item_id)
    if not itinerary_item:
        return jsonify({"error": f"Itinerary item with ID #{itinerary_item_id} does not exist."}), 404
    result = itinerary_item_schema.dump(itinerary_item)
    return jsonify(result), 200

# POST a new itinerary item
@itinerary_items.route("/", methods=["POST"])
def create_itinerary_item():
    body_data = request.get_json()
    new_itinerary_item = itinerary_item_schema.load(body_data, session=db.session)
    db.session.add(new_itinerary_item)
    db.session.commit()
    return itinerary_item_schema.dump(new_itinerary_item), 201