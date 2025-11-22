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