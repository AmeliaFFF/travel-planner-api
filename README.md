# Travel Planner API

*A backend application that centralises trip planning and travel-related data.*

## Description

The Travel Planner API is a RESTful backend service designed to help users organise and manage their holidays in one central place. It allows users to create trips, manage accommodation and transport bookings, add itinerary items, track expenses, and record the travellers associated with each trip.

This project was developed to solve a common problem: travel information is often scattered across emails, notes, and booking sites. By storing everything in a structured database, the API provides a single source of truth that keeps trip planning organised, consistent, and easy to access.

## Features

- Create and maintain multiple trips for each user.
- Add accommodation bookings, transport bookings, itinerary items, expenses, and travellers to any trip.
- Automatic ordering for accommodation (check-in date), transport (departure time), and itinerary items (date and start time).
- Clear RESTful structure with predictable endpoint behaviour.
- Full CRUD operations across all resources.
- Database seeding for quick development and testing.
- Input validation and serialisation using Marshmallow schemas.

## Technologies Used

- Python 3
- Flask (URL routing and CLI database commands)
- SQLAlchemy (object-relational mapping)
- Marshmallow (serialisation and validation)
- PostgreSQL (relational database)
- psycopg2 (PostgreSQL adapter)
- dotenv (environment variable loading)
- Virtual environment for dependency isolation

## Technical Prerequisites

- A computer running macOS, Windows, or Linux with the ability to install Python and PostgreSQL.
- A code editor (e.g., Visual Studio Code).
- Command Line Interface (CLI) access (e.g., Terminal, PowerShell, or the terminal within your code editor).
- (Optional) An API testing tool (e.g., Insomnia, Postman, Bruno).

## Installation

Follow the steps below to set up the Travel Planner API on your local machine. 

### Install Python 3
*Note: If you already have Python 3 installed, please skip to the next section.*

1. Run `python3 --version` in the CLI to confirm Python 3 is installed.
    - If it is already installed, this command will return a version number.  
    *Please continue to the next section.*
    - If it is not yet installed, follow the instructions for your operating system below.

- **Windows:**
    Download and install Python 3 using the official installer from python.org.

- **MacOS:**
    ```bash
    brew install python3
    python3 --version
    ```

- **Linux:**
    ```bash
    sudo apt install python3
    python3 --version
    ```

### Install PostgreSQL
*Note: If you already have PostgreSQL installed, please skip to the next section.*

1. Run `psql --version` in the CLI to confirm PostgreSQL is installed.
   - If it is already installed, this command will return a version number.  
   *Please continue to the next section.*
   - If it is not yet installed, follow the instructions for your operating system below.

- **Windows:**  
    Download and install PostgreSQL using the official installer from postgresql.org.

- **MacOS:**
    ```bash
    brew install postgresql
    brew services start postgresql
    psql --version
    ```

- **Linux:**
    ```bash
    sudo apt update
    sudo apt install postgresql postgresql-client
    sudo service postgresql start
    ```

### Create a Database

1. Start PostgreSQL by running the below command for your operating system:
- **macOS and Windows:**
    ```bash
    psql -d postgres
    ```
- **Linux:**
    ```bash
    sudo -u postgres psql
    ``` 

2. Create a new database:
   ```SQL
   CREATE DATABASE travel_planner_db;
   ```

3. Connect to the database:
   ```SQL
   \c travel_planner_db;
   ```

4. Create a user to manage the database:
    ```SQL
    CREATE USER travel_planner_dev WITH PASSWORD 'password123';
    ```

5. Grant all permissions to the new user:
    ```SQL
    GRANT ALL PRIVILEGES ON DATABASE travel_planner_db TO travel_planner_dev;
    ```

6. Grant all permissions on the default schemas:
    ```SQL
    GRANT ALL ON SCHEMA PUBLIC TO travel_planner_dev;
    ```

#### Additional Commands

1. To show all tables within the database:
    ```SQL
    \dt
    ```

2. To show all data within a specific table:
    ```SQL
    SELECT * FROM table_name;
    ```

3. To quit PostgreSQL:
    ```SQL
    \q
    ```

4. To reconnect to the database:

    - **macOS / Windows:**
        ```bash
        psql -d travel_planner_db -U travel_planner_dev
        ```
    - **Linux:**
        ```bash
        sudo -u postgres psql -d travel_planner_db
        ```

## Initialise the Project Locally

### Clone the Repository

1. Clone the repository to your local machine:
    - **HTTPS:**
        ```bash
        git clone https://github.com/AmeliaFFF/travel-planner-api.git
        ```
    - **SSH:**
        ```bash
        git clone git@github.com:AmeliaFFF/travel-planner-api.git
        ```

2. Navigate into the project directory:
    ```bash
    cd travel-planner-api
    ```

### Activate a Virtual Environment

1. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment:
    - **macOS / Linux:**
        ```bash
        source .venv/bin/activate
        ```
    - **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
        *If PowerShell blocks activation, run this once first:*  
        ```bash
        Set-ExecutionPolicy -Scope Process RemoteSigned
        ```

3. Confirm the environment is active before continuing.

### Install Dependencies

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. The application is now ready to be configured and started.

## Environment Configuration

### Local Database Environment

1. Duplicate the `.env.example` file and rename the duplicate to `.env`

2. Update the placeholder values (`database_user`, `database_password`, `database_name`) with your actual database credentials.

3. Save the file.

### Flask Environment

1. Duplicate the `.flaskenv.example` file and rename the duplicate to `.flaskenv`

2. This file is pre-configured for local development. Update the `FLASK_ENV` or `FLASK_DEBUG` if you want to change the environment settings.

3. Delete the instructional comments at the top of the file and save the file.  

## Running the API Locally

### Prepare the Environment

1. Ensure the virtual environment is active (refer to step 2 of [activate a virtual environment](#activate-a-virtual-environment)).

2. Make sure your `.env` and `.flaskenv` files are correctly configured (refer to [environment configuration](#environment-configuration)).

### Manage the Database

1. Create the database tables:
    ```bash
    flask db create
    ```
    Expected output:
    ```bash
    Tables created.
    ```

2. (Optional) Seed the database with dummy data:
    ```bash
    flask db seed
    ```
    Expected output:
    ```bash
    Tables seeded.
    ```

3. Drop all tables (useful if you want to reset the database or correct errors):
    ```bash
    flask db drop
    ```
    Expected output:
    ```bash
    Tables dropped.
    ```

### Start the Server

1. Run the Flask development server:
    ```bash
    flask run
    ```
    Expected output:
    ```bash                
    * Serving Flask app 'main:create_app'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 123-456-789
    ```

2. The API is now available at **http://127.0.0.1:5000**

## API Endpoints

The following tables describe all available API endpoints. Each section is grouped by resource and includes supported HTTP methods, endpoint paths, and a brief description of the operation performed.


### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | Retrieves all users. |
| GET | /users/<user_id> | Retrieves a single user by their user_id. |
| POST | /users | Creates a new user. |
| PATCH | /users/<user_id> | Updates specified fields of an existing user. |
| DELETE | /users/<user_id> | Deletes an existing user. |

### Trips

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /trips | Retrieves all trips. |
| GET | /trips/<trip_id> | Retrieves a single trip by its trip_id. |
| GET | /trips/user/<user_id> | Retrieves all trips created by a specific user_id. |
| POST | /trips | Creates a new trip. |
| PATCH | /trips/<trip_id> | Updates specified fields of an existing trip. |
| DELETE | /trips/<trip_id> | Deletes an existing trip and all associated data. |

### Accommodation Bookings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /accommodation-bookings | Retrieves all accommodation bookings, ordered by check-in date. |
| GET | /accommodation-bookings/<accommodation_booking_id> | Retrieves a single accommodation booking by its accommodation_booking_id. |
| GET | /accommodation-bookings/trip/<trip_id> | Retrieves all accommodation bookings for a specific trip by its trip_id. |
| POST | /accommodation-bookings | Creates a new accommodation booking. |
| PATCH | /accommodation-bookings/<accommodation_booking_id> | Updates specified fields of an existing accommodation booking. |
| DELETE | /accommodation-bookings/<accommodation_booking_id> | Deletes an existing accommodation booking. |

### Transport Bookings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /transport-bookings | Retrieves all transport bookings, ordered by departure time. |
| GET | /transport-bookings/<transport_booking_id> | Retrieves a single transport booking by its transport_booking_id. |
| GET | /transport-bookings/trip/<trip_id> | Retrieves all transport bookings for a specific trip by its trip_id. |
| POST | /transport-bookings | Creates a new transport booking. |
| PATCH | /transport-bookings/<transport_booking_id> | Updates specified fields of an existing transport booking. |
| DELETE | /transport-bookings/<transport_booking_id> | Deletes an existing transport booking. |

### Itinerary Items

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /itinerary-items | Retrieves all itinerary items, ordered by date and start time. |
| GET | /itinerary-items/<itinerary_item_id> | Retrieves a single itinerary item by its itinerary_item_id. |
| GET | /itinerary-items/trip/<trip_id> | Retrieves all itinerary items for a specific trip by its trip_id. |
| POST | /itinerary-items | Creates a new itinerary item. |
| PATCH | /itinerary-items/<itinerary_item_id> | Updates specified fields of an existing itinerary item. |
| DELETE | /itinerary-items/<itinerary_item_id> | Deletes an existing itinerary item. |

### Expenses

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /expenses | Retrieves all expenses, ordered by date. |
| GET | /expenses/<expense_id> | Retrieves a single expense by its expense_id. |
| GET | /expenses/trip/<trip_id> | Retrieves all expenses for a specific trip by its trip_id. |
| POST | /expenses | Creates a new expense. |
| PATCH | /expenses/<expense_id> | Updates specified fields of an existing expense. |
| DELETE | /expenses/<expense_id> | Deletes an existing expense. |

### Travellers

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /travellers | Retrieves all travellers. |
| GET | /travellers/<traveller_id> | Retrieves a single traveller by their traveller_id. |
| GET | /travellers/<traveller_id>/trips | Retrieves all trips for a specific traveller by their traveller_id. |
| POST | /travellers | Creates a new traveller. |
| PATCH | /travellers/<traveller_id> | Updates specified fields of an existing traveller. |
| DELETE | /travellers/<traveller_id> | Deletes an existing traveller. |

### Trip Travellers

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /trip-travellers | Retrieves all trip-traveller associations (trip_id and traveller_id pairs). |
| GET | /trip-travellers/<trip_id>/<traveller_id> | Retrieves a single trip-traveller association by trip_id and traveller_id. |
| POST | /trip-travellers | Creates a new trip-traveller association. |
| PATCH | /trip-travellers/<trip_id>/<traveller_id> | Updates "role" field of an existing trip-traveller association. |
| DELETE | /trip-travellers/<trip_id>/<traveller_id> | Deletes an existing trip-traveller association. |


## Usage Examples

Below are example JSON responses for each entity. These illustrate the structure and field names returned by the server, and can be used as a reference when constructing your own requests (e.g., for PATCH or POST operations).

### Users

```json
{
    "user_id": 1,
    "name": "Alice Smith",
    "email": "alice@example.com"
}
```

### Trips

```json
{
    "user": {
        "email": "alice@example.com",
        "name": "Alice Smith",
        "user_id": 1
    },
    "trip_id": 1,
    "name": "Japan 2026",
    "primary_destination": "Tokyo & Kyoto",
    "start_date": "2026-04-10",
    "end_date": "2026-04-24",
    "budget_amount": "4500.00",
    "currency_code": "AUD",
    "notes": "Cherry blossom season trip",
    "trip_travellers": [
        {
            "role": "organiser",
            "traveller": {
                "name": "Alice Smith",
                "email": "alice@example.com",
                "notes": "Primary account holder"
            }
        },
        {
            "role": "companion",
            "traveller": {
                "name": "Emma Johnson",
                "email": "emma.johnson@example.com",
                "notes": "Friend who joins multiple trips"
            }
        }
    ],
    "accommodation_bookings": [
        {
            "name": "Hotel Century Southern Tower",
            "address": "2-2-1 Yoyogi, Shibuya, Tokyo",
            "check_in_date": "2026-04-10",
            "check_out_date": "2026-04-15",
            "booking_reference": "JPN-HTL-44567",
            "cost_total": "78000",
            "currency_code": "JPY"
        },
        {
            "name": "Kyoto Ryokan Sakura",
            "address": "Higashiyama-ku, Kyoto",
            "check_in_date": "2026-04-15",
            "check_out_date": "2026-04-20",
            "booking_reference": "KYT-RYO-99812",
            "cost_total": "64000",
            "currency_code": "JPY"
        }
    ],
    "transport_bookings": [
        {
            "transport_type": "flight",
            "from_location": "Sydney",
            "to_location": "Tokyo (Haneda)",
            "departure_datetime": "2026-04-10T09:30:00",
            "arrival_datetime": "2026-04-10T17:00:00",
            "carrier_name": "Qantas",
            "booking_reference": "QF25-2026",
            "cost_total": "1450.00",
            "currency_code": "AUD"
        },
        {
            "transport_type": "flight",
            "from_location": "Tokyo (Haneda)",
            "to_location": "Sydney",
            "departure_datetime": "2026-04-23T22:00:00",
            "arrival_datetime": "2026-04-24T08:45:00",
            "carrier_name": "Qantas",
            "booking_reference": "QF26-2026",
            "cost_total": "1450.00",
            "currency_code": "AUD"
        }
    ],
    "itinerary_items": [
        {
            "date": "2026-04-12",
            "start_time": null,
            "end_time": null,
            "title": "TeamLab Planets",
            "category": "attraction",
            "location": "Toyosu, Tokyo",
            "notes": "Go early to avoid big crowds",
            "cost_total": "3800",
            "currency_code": "JPY"
        }
    ]
}
```

### Accommodation Bookings

```json
{
    "accommodation_id": 1,
    "trip_id": 1,
    "name": "Hotel Century Southern Tower",
    "address": "2-2-1 Yoyogi, Shibuya, Tokyo",
    "check_in_date": "2026-04-10",
    "check_out_date": "2026-04-15",
    "booking_reference": "JPN-HTL-44567",
    "cost_total": "78000",
    "currency_code": "JPY"
}
```

### Transport Bookings

```json
{
    "transport_id": 1,
    "trip_id": 1,
    "transport_type": "flight",
    "from_location": "Sydney",
    "to_location": "Tokyo (Haneda)",
    "departure_datetime": "2026-04-10T09:30:00",
    "arrival_datetime": "2026-04-10T17:00:00",
    "carrier_name": "Qantas",
    "booking_reference": "QF25-2026",
    "cost_total": "1450.00",
    "currency_code": "AUD"
}
```

### Itinerary Items

```json
{
    "itinerary_item_id": 1,
    "trip_id": 1,
    "date": "2026-04-12",
    "start_time": null,
    "end_time": null,
    "title": "TeamLab Planets",
    "category": "attraction",
    "location": "Toyosu, Tokyo",
    "notes": "Go early to avoid big crowds",
    "cost_total": "3800",
    "currency_code": "JPY"
}
```

### Expense

```json
{
    "expense_id": 1,
    "trip_id": 1,
    "date": "2026-04-12",
    "category": "food",
    "description": "Lunch - ramen",
    "cost_total": "1200",
    "currency_code": "JPY"
}
```

### Travellers

```json
{
    "traveller_id": 1,
    "name": "Alice Smith",
    "email": "alice@example.com",
    "notes": "Primary account holder"
}
```

### Trip Travellers

```json
{
    "trip_id": 1,
    "traveller_id": 2,
    "role": "companion",
    "traveller": {
        "name": "Emma Johnson",
        "email": "emma.johnson@example.com",
        "notes": "Friend who joins multiple trips"
    }
}
```

## Acknowledgements

This project was developed as part of a software engineering assignment and uses open-source tools including Flask, SQLAlchemy and PostgreSQL.

Sample seed data (names, addresses, locations, booking references, etc.) was generated with the assistance of an AI tool to create realistic examples. All design, modelling and code are my own work.

## Contact

If you have questions or would like to know more about this project, feel free to reach out via GitHub.