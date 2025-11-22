from main import ma
from models.trip import Trip

class TripSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trip
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("trip_id", "user_id", "name", "primary_destination", "start_date", "end_date", "budget_amount", "currency_code", "notes")

trip_schema = TripSchema()
trips_schema = TripSchema(many=True)