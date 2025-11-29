from marshmallow import validates_schema, ValidationError
from main import ma
from models.transport import TransportBooking

class TransportBookingSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for TransportBooking model. Includes validation to ensure departure time is before arrival time."""
    class Meta:
        model = TransportBooking
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("transport_id", "trip_id", "transport_type", "from_location", "to_location", "departure_datetime", "arrival_datetime", "carrier_name", "booking_reference", "cost_total", "currency_code")

    @validates_schema
    def validate_datetimes(self, data, **kwargs):
        departure_datetime = data.get("departure_datetime")
        arrival_datetime = data.get("arrival_datetime")

        if departure_datetime and arrival_datetime and departure_datetime >= arrival_datetime:
            raise ValidationError(
                "departure_datetime must be earlier than arrival_datetime.",
                field_name="departure_datetime"
            )

transport_booking_schema = TransportBookingSchema()
transport_bookings_schema = TransportBookingSchema(many=True)