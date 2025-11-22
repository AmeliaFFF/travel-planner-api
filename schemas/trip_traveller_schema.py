from main import ma
from models.trip_traveller import TripTraveller

class TripTravellerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TripTraveller
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("trip_id", "traveller_id", "role")

trip_traveller_schema = TripTravellerSchema()
trip_travellers_schema = TripTravellerSchema(many=True)