from marshmallow import fields
from main import ma
from models.trip import Trip
from schemas.accommodation_schema import AccommodationBookingSchema
from schemas.itinerary_schema import ItineraryItemSchema
from schemas.transport_schema import TransportBookingSchema
from schemas.trip_traveller_schema import TripTravellerSchema
from schemas.user_schema import UserSchema

class TripSchema(ma.SQLAlchemyAutoSchema):

    accommodation_bookings = fields.Nested("AccommodationBookingSchema", only=["name", "address", "check_in_date", "check_out_date", "booking_reference", "cost_total", "currency_code"], many=True)
    
    itinerary_items = fields.Nested("ItineraryItemSchema", only=["date", "start_time", "end_time", "title", "category", "location", "notes", "cost_total", "currency_code"], many=True)
    
    transport_bookings = fields.Nested("TransportBookingSchema", only=["transport_type", "from_location", "to_location", "departure_datetime", "arrival_datetime", "carrier_name", "booking_reference", "cost_total", "currency_code"], many=True)
    
    trip_travellers = fields.Nested("TripTravellerSchema", only=["role", "traveller"], many=True)
    
    user = fields.Nested("UserSchema", only=["user_id", "name", "email"])
    
    class Meta:
        model = Trip
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("user", "trip_id", "name", "primary_destination", "start_date", "end_date", "budget_amount", "currency_code", "notes", "trip_travellers", "accommodation_bookings", "transport_bookings", "itinerary_items")

trip_schema = TripSchema()
trips_schema = TripSchema(many=True)