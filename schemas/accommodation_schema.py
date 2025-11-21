from main import ma

class AccommodationBookingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("accommodation_id", "trip_id", "name", "address", "check_in_date", "check_out_date", "booking_reference", "cost_total", "currency_code")

accommodation_booking_schema = AccommodationBookingSchema()
accommodation_bookings_schema = AccommodationBookingSchema(many=True)