from main import ma

class TripTravellerSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("trip_id", "traveller_id", "role")

trip_traveller_schema = TripTravellerSchema()
trip_travellers_schema = TripTravellerSchema(many=True)