from main import ma

class TripSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("trip_id", "user_id", "name", "primary_destination", "start_date", "end_date", "budget_amount", "currency_code", "notes")

trip_schema = TripSchema()
trips_schema = TripSchema(many=True)