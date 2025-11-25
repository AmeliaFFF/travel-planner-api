from marshmallow import validates_schema, ValidationError
from main import ma
from models.itinerary import ItineraryItem

class ItineraryItemSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for ItineraryItem model. Includes validation to ensure start time is before end time when both are provided."""
    class Meta:
        model = ItineraryItem
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("itinerary_item_id", "trip_id", "date", "start_time", "end_time", "title", "category", "location", "notes", "cost_total", "currency_code")

    @validates_schema
    def validate_times(self, data, **kwargs):
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        if start_time and end_time and start_time >= end_time:
            raise ValidationError(
                "start_time must be earlier than end_time.",
                field_name="start_time"
            )

itinerary_item_schema = ItineraryItemSchema()
itinerary_items_schema = ItineraryItemSchema(many=True)