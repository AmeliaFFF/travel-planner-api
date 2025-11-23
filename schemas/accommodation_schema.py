from marshmallow import validates_schema, ValidationError
from main import ma
from models.accommodation import AccommodationBooking

class AccommodationBookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AccommodationBooking
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("accommodation_id", "trip_id", "name", "address", "check_in_date", "check_out_date", "booking_reference", "cost_total", "currency_code")

    @validates_schema
    def validate_dates(self, data, **kwargs):
        check_in_date = data.get("check_in_date")
        check_out_date = data.get("check_out_date")

        if check_in_date and check_out_date and check_in_date >= check_out_date:
            raise ValidationError(
                "check_in_date must be earlier than check_out_date.",
                field_name="check_in_date"
            )

accommodation_booking_schema = AccommodationBookingSchema()
accommodation_bookings_schema = AccommodationBookingSchema(many=True)