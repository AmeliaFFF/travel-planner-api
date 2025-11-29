from controllers.accommodation_controller import accommodation_bookings
from controllers.expense_controller import expenses
from controllers.itinerary_controller import itinerary_items
from controllers.transport_controller import transport_bookings
from controllers.traveller_controller import travellers
from controllers.trip_controller import trips
from controllers.trip_traveller_controller import trip_travellers
from controllers.user_controller import users

registerable_controllers = [
    accommodation_bookings, 
    expenses,
    itinerary_items,
    transport_bookings,
    travellers,
    trips,
    trip_travellers,
    users
]