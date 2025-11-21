from main import ma

class ItineraryItemSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("itinerary_item_id", "trip_id", "date", "start_time", "end_time", "title", "category", "location", "notes", "cost_total", "currency_code")

itinerary_item_schema = ItineraryItemSchema()
itinerary_items_schema = ItineraryItemSchema(many=True)