from flask import Blueprint, jsonify, request
from main import db
from models.itinerary import ItineraryItem
from models.trip import Trip
from schemas.itinerary_schema import itinerary_item_schema, itinerary_items_schema

itinerary_items = Blueprint("itinerary_items", __name__, url_prefix="/itinerary-items")

@itinerary_items.route("/", methods=["GET"])
def get_itinerary_items():
    """Retrieves all itinerary items, ordered by date and start time."""
    stmt = (db.select(ItineraryItem).order_by(ItineraryItem.date, ItineraryItem.start_time))
    itinerary_items_list = db.session.scalars(stmt)
    result = itinerary_items_schema.dump(itinerary_items_list)
    return jsonify(result), 200

@itinerary_items.route("/<int:itinerary_item_id>", methods=["GET"])
def get_itinerary_item(itinerary_item_id):
    """Retrieves a single itinerary item by its itinerary_item_id."""
    itinerary_item = ItineraryItem.query.get(itinerary_item_id)
    if not itinerary_item:
        return jsonify({"error": f"Itinerary item with ID #{itinerary_item_id} does not exist."}), 404
    result = itinerary_item_schema.dump(itinerary_item)
    return jsonify(result), 200

@itinerary_items.route("/trip/<int:trip_id>", methods=["GET"])
def get_itinerary_items_for_trip(trip_id):
    """Retrieves all itinerary items for a specific trip by its trip_id."""
    # Check that the trip actually exists
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{trip_id} does not exist."}), 404
    # Fetch all itinerary items for this trip
    stmt = (db.select(ItineraryItem).filter_by(trip_id=trip_id).order_by(ItineraryItem.date, ItineraryItem.start_time))
    itinerary_items_list = db.session.scalars(stmt)
    result = itinerary_items_schema.dump(itinerary_items_list)
    # If the trip exists but has no itinerary items
    if len(result) == 0:
        return jsonify({
            "message": f"Trip with ID #{trip_id} has no itinerary items."
        }), 200
    # Return the trip's itinerary items
    return jsonify(result), 200

@itinerary_items.route("/", methods=["POST"])
def create_itinerary_item():
    """Creates a new itinerary item."""
    body_data = request.get_json()
    new_itinerary_item = itinerary_item_schema.load(body_data, session=db.session)
    db.session.add(new_itinerary_item)
    db.session.commit()
    return itinerary_item_schema.dump(new_itinerary_item), 201

@itinerary_items.route("/<int:itinerary_item_id>", methods=["PATCH"])
def update_itinerary_item(itinerary_item_id):
    """Updates specified fields of an existing itinerary item."""
    itinerary_item = ItineraryItem.query.get(itinerary_item_id)
    if not itinerary_item:
        return jsonify({"error": f"Itinerary item with ID #{itinerary_item_id} does not exist."}), 404
    body_data = request.get_json()
    itinerary_item = itinerary_item_schema.load(body_data, instance=itinerary_item, session=db.session, partial=True)
    db.session.commit()
    return itinerary_item_schema.dump(itinerary_item), 200

@itinerary_items.route("/<int:itinerary_item_id>", methods=["DELETE"])
def delete_itinerary_item(itinerary_item_id):
    """Deletes an existing itinerary item."""
    itinerary_item = ItineraryItem.query.get(itinerary_item_id)
    if not itinerary_item:
        return jsonify({"error": f"Itinerary item with ID #{itinerary_item_id} does not exist."}), 404
    db.session.delete(itinerary_item)
    db.session.commit()
    return jsonify({"message": f"Itinerary item with ID #{itinerary_item_id} deleted successfully."}), 200