from main import ma
from models.transport import TransportBooking

class TransportBookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TransportBooking
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("transport_id", "trip_id", "transport_type", "from_location", "to_location", "departure_datetime", "arrival_datetime", "carrier_name", "booking_reference", "cost_total", "currency_code")

transport_booking_schema = TransportBookingSchema()
transport_bookings_schema = TransportBookingSchema(many=True)