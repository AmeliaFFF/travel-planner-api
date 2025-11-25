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
    """Creates all database tables from models."""
    db.create_all()
    print("Tables created.")

@db_commands.cli.command("seed")
def seed_db():
    """Populates all tables in the database with sample data."""
    # DISCLAIMER: Sample data values (names, addresses, booking references, etc.) were generated with help from an AI tool to create realistic looking data. All code and database logic is my own work.

    # USERS
    alice = User(
        name="Alice Smith",
        email="alice@example.com"
    )

    john = User(
        name="John Taylor",
        email="john@example.com"
    )

    mia = User(
        name="Mia Thompson",
        email="mia@example.com"
    )

    oliver = User(
        name="Oliver Chen",
        email="oliver@example.com"
    )

    db.session.add_all([alice, john, mia, oliver])
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
        notes="John's partner"
    )

    mia_traveller = Traveller(
        name="Mia Thompson",
        email="mia@example.com",
        notes="Loves food tours"
    )

    oliver_traveller = Traveller(
        name="Oliver Chen",
        email="oliver@example.com",
        notes="Travel photographer"
    )

    sarah_traveller = Traveller(
        name="Sarah Patel",
        email="sarah.patel@example.com",
        notes="Friend who joins occasionally"
    )

    dylan_traveller = Traveller(
        name="Dylan Nguyen",
        email="dylan.nguyen@example.com",
        notes="Adventure traveller"
    )

    db.session.add_all([alice_traveller, emma_traveller, john_traveller, lucy_traveller, mia_traveller, oliver_traveller, sarah_traveller, dylan_traveller])
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

    # Trip 4 – Thailand (Mia)
    thailand_trip = Trip(
        user_id=mia.user_id,
        name="Thailand 2027",
        primary_destination="Bangkok & Phuket",
        start_date="2027-02-10",
        end_date="2027-02-20",
        budget_amount=3100.00,
        currency_code="AUD",
        notes="Food tour + island hopping"
    )

    # Trip 5 – Canada (Oliver)
    canada_trip = Trip(
        user_id=oliver.user_id,
        name="Canada 2027",
        primary_destination="Vancouver & Banff",
        start_date="2027-06-01",
        end_date="2027-06-15",
        budget_amount=5400.00,
        currency_code="CAD",
        notes="Photography trip in nature"
    )

    # Trip 6 – Singapore Weekend (Mia)
    sg_trip = Trip(
        user_id=mia.user_id,
        name="Singapore Weekend",
        primary_destination="Singapore",
        start_date="2027-03-15",
        end_date="2027-03-19",
        budget_amount=1600.00,
        currency_code="SGD",
        notes="Short weekend getaway"
    )

    db.session.add_all([japan_trip, nz_trip, italy_trip, thailand_trip, canada_trip, sg_trip])
    db.session.commit()

    # TRIP–TRAVELLER (join table)
    db.session.add_all([
        # Japan trip: Alice + Emma
        TripTraveller(trip_id=japan_trip.trip_id, traveller_id=alice_traveller.traveller_id, role="organiser"),
        TripTraveller(trip_id=japan_trip.trip_id, traveller_id=emma_traveller.traveller_id, role="companion"),

        # New Zealand trip: Alice only
        TripTraveller(trip_id=nz_trip.trip_id, traveller_id=alice_traveller.traveller_id, role="solo traveller"),

        # Italy trip: John + Lucy + Emma
        TripTraveller(trip_id=italy_trip.trip_id, traveller_id=john_traveller.traveller_id, role="organiser"),
        TripTraveller(trip_id=italy_trip.trip_id, traveller_id=lucy_traveller.traveller_id, role="companion"),
        TripTraveller(trip_id=italy_trip.trip_id, traveller_id=emma_traveller.traveller_id, role="friend"),

        # Thailand trip: Mia + Sarah + Dylan
        TripTraveller(trip_id=thailand_trip.trip_id, traveller_id=mia_traveller.traveller_id, role="organiser"),
        TripTraveller(trip_id=thailand_trip.trip_id, traveller_id=sarah_traveller.traveller_id, role="friend"),
        TripTraveller(trip_id=thailand_trip.trip_id, traveller_id=dylan_traveller.traveller_id, role="companion"),

        # Canada trip: Oliver + Mia
        TripTraveller(trip_id=canada_trip.trip_id, traveller_id=oliver_traveller.traveller_id, role="organiser"),
        TripTraveller(trip_id=canada_trip.trip_id, traveller_id=mia_traveller.traveller_id, role="friend"),

        # Singapore trip: Mia + Sarah
        TripTraveller(trip_id=sg_trip.trip_id, traveller_id=mia_traveller.traveller_id, role="organiser"),
        TripTraveller(trip_id=sg_trip.trip_id, traveller_id=sarah_traveller.traveller_id, role="friend"),
    ])
    db.session.commit()

    # ACCOMMODATION BOOKINGS
    db.session.add_all([
        # Japan trip accommodations
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
        # New Zealand trip accommodation
        AccommodationBooking(
            trip_id=nz_trip.trip_id,
            name="Queenstown Lakeview Holiday Park",
            address="Queenstown, South Island",
            check_in_date="2026-11-01",
            check_out_date="2026-11-05",
            booking_reference="NZ-QLD-55221",
            cost_total=480,
            currency_code="NZD"
        ),
        # Thailand trip accommodations
        AccommodationBooking(
            trip_id=thailand_trip.trip_id,
            name="Chatrium Hotel Riverside",
            address="Bangkok Riverside",
            check_in_date="2027-02-10",
            check_out_date="2027-02-14",
            booking_reference="TH-CHAT-12345",
            cost_total=540.00,
            currency_code="THB"
        ),
        AccommodationBooking(
            trip_id=thailand_trip.trip_id,
            name="The Shore at Katathani",
            address="Phuket",
            check_in_date="2027-02-14",
            check_out_date="2027-02-20",
            booking_reference="TH-PKT-67890",
            cost_total=1120.00,
            currency_code="THB"
        ),
        # Canada trip accommodations
        AccommodationBooking(
            trip_id=canada_trip.trip_id,
            name="Pan Pacific Vancouver",
            address="Vancouver",
            check_in_date="2027-06-01",
            check_out_date="2027-06-07",
            booking_reference="CA-VAN-44321",
            cost_total=1600.00,
            currency_code="CAD"
        ),
        AccommodationBooking(
            trip_id=canada_trip.trip_id,
            name="Fairmont Banff Springs",
            address="Banff National Park",
            check_in_date="2027-06-07",
            check_out_date="2027-06-15",
            booking_reference="CA-BANFF-11223",
            cost_total=2400.00,
            currency_code="CAD"
        ),
        # Italy trip accommodation
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
    ])
    db.session.commit()

    # TRANSPORT BOOKINGS
    db.session.add_all([
        # Japan trip transport
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
        ),
        # New Zealand trip transport
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
        ),
        # Italy trip transport
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
        ),
        # Thailand trip transport
        TransportBooking(
            trip_id=thailand_trip.trip_id,
            transport_type="flight",
            from_location="Sydney",
            to_location="Bangkok",
            departure_datetime="2027-02-10 08:00",
            arrival_datetime="2027-02-10 14:30",
            carrier_name="Thai Airways",
            booking_reference="TG476",
            cost_total=950.00,
            currency_code="AUD"
        ),
        TransportBooking(
            trip_id=thailand_trip.trip_id,
            transport_type="ferry",
            from_location="Phi Phi",
            to_location="Phuket",
            departure_datetime="2027-02-14 10:00",
            arrival_datetime="2027-02-14 12:00",
            carrier_name="Andaman Ferry",
            booking_reference="AF-PP-2027",
            cost_total=35.00,
            currency_code="THB"
        ),
        # Canada trip transport
        TransportBooking(
            trip_id=canada_trip.trip_id,
            transport_type="flight",
            from_location="Sydney",
            to_location="Vancouver",
            departure_datetime="2027-06-01 10:00",
            arrival_datetime="2027-06-01 08:00",
            carrier_name="Air Canada",
            booking_reference="AC34",
            cost_total=1800.00,
            currency_code="AUD"
        )
    ])
    db.session.commit()

    # ITINERARY ITEMS
    db.session.add_all([
        # Japan itinerary item
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
        # New Zealand itinerary item
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
        # Italy itinerary item
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
        # Thailand itinerary items
        ItineraryItem(
            trip_id=thailand_trip.trip_id,
            date="2027-02-11",
            title="Bangkok Food Tour",
            category="food",
            location="Old Bangkok",
            notes="Street food tour at night",
            cost_total=50,
            currency_code="THB"
        ),
        ItineraryItem(
            trip_id=thailand_trip.trip_id,
            date="2027-02-15",
            title="Phi Phi Island Day Trip",
            category="tour",
            location="Phuket",
            notes="Snorkelling included",
            cost_total=120,
            currency_code="THB"
        ),
        # Canada itinerary item
        ItineraryItem(
            trip_id=canada_trip.trip_id,
            date="2027-06-03",
            title="Stanley Park Photography Ride",
            category="activity",
            location="Vancouver",
            cost_total=25,
            currency_code="CAD"
        ),
    ])

    db.session.commit()

    # EXPENSES
    db.session.add_all([
        # Japan expense
        Expense(
            trip_id=japan_trip.trip_id,
            date="2026-04-12",
            category="food",
            description="Lunch - ramen",
            cost_total=1200,
            currency_code="JPY"
        ),
        # New Zealand expense
        Expense(
            trip_id=nz_trip.trip_id,
            date="2026-11-04",
            category="fuel",
            description="Petrol fill-up",
            cost_total=98.50,
            currency_code="NZD"
        ),
        # Italy expense
        Expense(
            trip_id=italy_trip.trip_id,
            date="2026-09-07",
            category="shopping",
            description="Leather wallet",
            cost_total=60.00,
            currency_code="EUR"
        ),
        # Thailand expense
        Expense(
            trip_id=thailand_trip.trip_id,
            date="2027-02-11",
            category="food",
            description="Pad Thai + Dessert",
            cost_total=180,
            currency_code="THB"
        ),
        # Canada expense
        Expense(
            trip_id=canada_trip.trip_id,
            date="2027-06-04",
            category="transport",
            description="Day parking in Vancouver",
            cost_total=28,
            currency_code="CAD"
        ),
    ])
    db.session.commit()

    print("Tables seeded.")

@db_commands.cli.command("drop")
def drop_db():
    """Drops all database tables."""
    db.drop_all()
    print("Tables dropped.")
