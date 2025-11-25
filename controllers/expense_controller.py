from flask import Blueprint, jsonify, request, abort
from main import db
from models.expense import Expense
from models.trip import Trip
from schemas.expense_schema import expense_schema, expenses_schema

expenses = Blueprint("expenses", __name__, url_prefix="/expenses")

@expenses.route("/", methods=["GET"])
def get_expenses():
    """Retrieves all expenses, ordered by date."""
    stmt = (db.select(Expense).order_by(Expense.date))
    expenses_list = db.session.scalars(stmt)
    result = expenses_schema.dump(expenses_list)
    return jsonify(result), 200

@expenses.route("/<int:expense_id>", methods=["GET"])
def get_expense(expense_id):
    """Retrieves a single expense by its expense_id."""
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": f"Expense with ID #{expense_id} does not exist."}), 404
    result = expense_schema.dump(expense)
    return jsonify(result), 200

@expenses.route("/trip/<int:trip_id>", methods=["GET"])
def get_expenses_for_trip(trip_id):
    """Retrieves all expenses for a specific trip by its trip_id."""
    # Check that the trip actually exists
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": f"Trip with ID #{trip_id} does not exist."}), 404
    # Fetch all expenses for this trip
    stmt = (db.select(Expense).filter_by(trip_id=trip_id).order_by(Expense.date))
    expenses_list = db.session.scalars(stmt)
    result = expenses_schema.dump(expenses_list)
    # If the trip exists but has no expenses
    if len(result) == 0:
        return jsonify({
            "message": f"Trip with ID #{trip_id} has no expenses."
        }), 200
    # Return the trip's expenses
    return jsonify(result), 200

@expenses.route("/", methods=["POST"])
def create_expense():
    """Creates a new expense."""
    body_data = request.get_json()
    new_expense = expense_schema.load(body_data, session=db.session)
    db.session.add(new_expense)
    db.session.commit()
    return expense_schema.dump(new_expense), 201

@expenses.route("/<int:expense_id>", methods=["PATCH"])
def update_expense(expense_id):
    """Updates specified fields of an existing expense."""
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": f"Expense with ID #{expense_id} does not exist."}), 404
    body_data = request.get_json()
    expense = expense_schema.load(body_data, instance=expense, session=db.session, partial=True)
    db.session.commit()
    return expense_schema.dump(expense), 200

@expenses.route("/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    """Deletes an existing expense."""
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": f"Expense with ID #{expense_id} does not exist."}), 404
    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": f"Expense with ID #{expense_id} deleted successfully."}), 200