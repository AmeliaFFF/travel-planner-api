from flask import Blueprint, jsonify, request, abort
from main import db
from models.expense import Expense
from schemas.expense_schema import expense_schema, expenses_schema

expenses = Blueprint("expenses", __name__, url_prefix="/expenses")

# GET all expenses
@expenses.route("/", methods=["GET"])
def get_expenses():
    stmt = db.select(Expense)
    expenses_list = db.session.scalars(stmt)
    result = expenses_schema.dump(expenses_list)
    return jsonify(result), 200

# GET a single expense by ID
@expenses.route("/<int:expense_id>", methods=["GET"])
def get_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": f"Expense with ID #{expense_id} does not exist."}), 404
    result = expense_schema.dump(expense)
    return jsonify(result), 200

# POST a new expense
@expenses.route("/", methods=["POST"])
def create_expense():
    body_data = request.get_json()
    new_expense = expense_schema.load(body_data, session=db.session)
    db.session.add(new_expense)
    db.session.commit()
    return expense_schema.dump(new_expense), 201