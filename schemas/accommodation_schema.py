from main import ma
from models.accommodation import AccommodationBooking

class AccommodationBookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AccommodationBooking
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("accommodation_id", "trip_id", "name", "address", "check_in_date", "check_out_date", "booking_reference", "cost_total", "currency_code")

accommodation_booking_schema = AccommodationBookingSchema()
accommodation_bookings_schema = AccommodationBookingSchema(many=True)