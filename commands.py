from main import db
from flask import Blueprint
from datetime import date, datetime, time
from models.accommodation import AccommodationBooking
from models.expense import Expense
from models.itinerary import ItineraryItem
from models.transport import TransportBooking
from models.traveller import Traveller
from models.trip_traveller import TripTraveller
from models.trip import Trip
from models.user import User

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created.")

@db_commands.cli.command("seed")
def seed_db():
    # USERS
    alice = User(
        name="Alice Smith",
        email="alice@example.com"
    )
    john = User(
        name="John Taylor",
        email="john@example.com"
    )

    db.session.add_all([alice, john])
    db.session.commit()

    # TRAVELLERS
    alice_traveller = Traveller(
        name="Alice Smith",
        email="alice@example.com",
        notes="Primary account holder"
    )

    emma_traveller = Traveller(
        name="Emma Johnson",
        email="emma.johnson@example.com",
        notes="Friend who joins multiple trips"
    )

    john_traveller = Traveller(
        name="John Taylor",
        email="john@example.com",
        notes="Primary account holder"
    )

    lucy_traveller = Traveller(
        name="Lucy Romano",
        email="lucy.romano@example.com",
        notes="John’s partner"
    )

    db.session.add_all([alice_traveller, emma_traveller, john_traveller, lucy_traveller])
    db.session.commit()

    # TRIPS

    # Trip 1 – Japan (Alice)
    japan_trip = Trip(
        user_id=alice.user_id,
        name="Japan 2026",
        primary_destination="Tokyo & Kyoto",
        start_date="2026-04-10",
        end_date="2026-04-24",
        budget_amount=4500.00,
        currency_code="AUD",
        notes="Cherry blossom season trip"
    )

    # Trip 2 – New Zealand Road Trip (Alice)
    nz_trip = Trip(
        user_id=alice.user_id,
        name="New Zealand Road Trip",
        primary_destination="South Island",
        start_date="2026-11-01",
        end_date="2026-11-10",
        budget_amount=2200.00,
        currency_code="AUD",
        notes="Solo self-drive trip"
    )

    # Trip 3 – Italy (John)
    italy_trip = Trip(
        user_id=john.user_id,
        name="Italy 2026",
        primary_destination="Rome, Florence & Venice",
        start_date="2026-09-05",
        end_date="2026-09-20",
        budget_amount=6200.00,
        currency_code="EUR",
        notes="Anniversary holiday"
    )

    db.session.add_all([japan_trip, nz_trip, italy_trip])
    db.session.commit()

    # TRIP–TRAVELLER (JOIN TABLE)
    db.session.add_all([
        # Japan trip: Alice + Emma
        TripTraveller(trip_id=japan_trip.trip_id, traveller_id=alice_traveller.traveller_id, role="organiser"),
        TripTraveller(trip_id=japan_trip.trip_id, traveller_id=emma_traveller.traveller_id, role="companion"),

        # NZ trip: Alice only
        TripTraveller(trip_id=nz_trip.trip_id, traveller_id=alice_traveller.traveller_id, role="solo traveller"),

        # Italy trip: John + Lucy + Emma
        TripTraveller(trip_id=italy_trip.trip_id, traveller_id=john_traveller.traveller_id, role="organiser"),
        TripTraveller(trip_id=italy_trip.trip_id, traveller_id=lucy_traveller.traveller_id, role="companion"),
        TripTraveller(trip_id=italy_trip.trip_id, traveller_id=emma_traveller.traveller_id, role="friend"),
    ])
    db.session.commit()

    # ACCOMMODATION BOOKINGS
    db.session.add_all([
        AccommodationBooking(
            trip_id=japan_trip.trip_id,
            name="Hotel Century Southern Tower",
            address="2-2-1 Yoyogi, Shibuya, Tokyo",
            check_in_date="2026-04-10",
            check_out_date="2026-04-15",
            booking_reference="JPN-HTL-44567",
            cost_total=78000,
            currency_code="JPY"
        ),
        AccommodationBooking(
            trip_id=japan_trip.trip_id,
            name="Kyoto Ryokan Sakura",
            address="Higashiyama-ku, Kyoto",
            check_in_date="2026-04-15",
            check_out_date="2026-04-20",
            booking_reference="KYT-RYO-99812",
            cost_total=64000,
            currency_code="JPY"
        ),
    ])

    db.session.add(
        AccommodationBooking(
            trip_id=nz_trip.trip_id,
            name="Queenstown Lakeview Holiday Park",
            address="Queenstown, South Island",
            check_in_date="2026-11-01",
            check_out_date="2026-11-05",
            booking_reference="NZ-QLD-55221",
            cost_total=480,
            currency_code="NZD"
        )
    )

    db.session.add(
        AccommodationBooking(
            trip_id=italy_trip.trip_id,
            name="Hotel Artemide",
            address="Via Nazionale, Rome",
            check_in_date="2026-09-05",
            check_out_date="2026-09-10",
            booking_reference="ITA-ROM-12098",
            cost_total=750,
            currency_code="EUR"
        )
    )

    db.session.commit()

    # TRANSPORT BOOKINGS
    db.session.add(
        TransportBooking(
            trip_id=japan_trip.trip_id,
            transport_type="flight",
            from_location="Sydney",
            to_location="Tokyo (Haneda)",
            departure_datetime="2026-04-10 09:30",
            arrival_datetime="2026-04-10 17:00",
            carrier_name="Qantas",
            booking_reference="QF25-2026",
            cost_total=1450.00,
            currency_code="AUD"
        )
    )

    db.session.add(
        TransportBooking(
            trip_id=nz_trip.trip_id,
            transport_type="car_rental",
            from_location="Christchurch Airport",
            to_location="Christchurch Airport",
            departure_datetime="2026-11-01 10:00",
            arrival_datetime="2026-11-10 14:00",
            carrier_name="NZ Rentals",
            booking_reference="NZ-CR-72819",
            cost_total=680.00,
            currency_code="NZD"
        )
    )

    db.session.add(
        TransportBooking(
            trip_id=italy_trip.trip_id,
            transport_type="train",
            from_location="Rome",
            to_location="Florence",
            departure_datetime="2026-09-10 09:00",
            arrival_datetime="2026-09-10 11:30",
            carrier_name="Trenitalia",
            booking_reference="TRN-IT-45671",
            cost_total=42.00,
            currency_code="EUR"
        )
    )

    db.session.commit()

    # ITINERARY ITEMS
    db.session.add_all([
        ItineraryItem(
            trip_id=japan_trip.trip_id,
            date="2026-04-12",
            title="TeamLab Planets",
            category="attraction",
            location="Toyosu, Tokyo",
            notes="Go early to avoid big crowds",
            cost_total=3800,
            currency_code="JPY"
        ),
        ItineraryItem(
            trip_id=nz_trip.trip_id,
            date="2026-11-03",
            title="Shotover Jet Ride",
            category="activity",
            location="Queenstown",
            notes="Pre-book required",
            cost_total=169,
            currency_code="NZD"
        ),
        ItineraryItem(
            trip_id=italy_trip.trip_id,
            date="2026-09-06",
            title="Colosseum Tour",
            category="tour",
            location="Rome",
            notes="Booked skip-the-line ticket",
            cost_total=45,
            currency_code="EUR"
        ),
    ])
    db.session.commit()

    # EXPENSES
    db.session.add_all([
        Expense(
            trip_id=japan_trip.trip_id,
            date="2026-04-12",
            category="food",
            description="Lunch - ramen",
            cost_total=1200,
            currency_code="JPY"
        ),
        Expense(
            trip_id=nz_trip.trip_id,
            date="2026-11-04",
            category="fuel",
            description="Petrol fill-up",
            cost_total=98.50,
            currency_code="NZD"
        ),
        Expense(
            trip_id=italy_trip.trip_id,
            date="2026-09-07",
            category="shopping",
            description="Leather wallet",
            cost_total=60.00,
            currency_code="EUR"
        ),
    ])
    db.session.commit()

    print("Tables seeded.")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped.")
