from main import ma
from models.trip_traveller import TripTraveller
from schemas.traveller_schema import TravellerSchema

class TripTravellerSchema(ma.SQLAlchemyAutoSchema):
    traveller = ma.Nested(TravellerSchema, only=["name", "email", "notes"])
    class Meta:
        model = TripTraveller
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("trip_id", "traveller_id", "role", "traveller")

trip_traveller_schema = TripTravellerSchema()
trip_travellers_schema = TripTravellerSchema(many=True)