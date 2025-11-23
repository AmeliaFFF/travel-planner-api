from flask import Blueprint, jsonify, request, abort
from main import db
from models.user import User
from schemas.user_schema import user_schema, users_schema

users = Blueprint("users", __name__, url_prefix="/users")

# GET all users
@users.route("/", methods=["GET"])
def get_users():
    stmt = db.select(User)
    users_list = db.session.scalars(stmt)
    result = users_schema.dump(users_list)
    return jsonify(result), 200

# GET a single user by ID
@users.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": f"User with ID #{user_id} does not exist."}), 404
    result = user_schema.dump(user)
    return jsonify(result), 200