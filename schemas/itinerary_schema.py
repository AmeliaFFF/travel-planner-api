from main import ma
from models.itinerary import ItineraryItem

class ItineraryItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItineraryItem
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("itinerary_item_id", "trip_id", "date", "start_time", "end_time", "title", "category", "location", "notes", "cost_total", "currency_code")

itinerary_item_schema = ItineraryItemSchema()
itinerary_items_schema = ItineraryItemSchema(many=True)