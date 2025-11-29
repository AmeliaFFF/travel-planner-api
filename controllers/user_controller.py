from flask import Blueprint, jsonify, request
from main import db
from models.user import User
from schemas.user_schema import user_schema, users_schema

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def get_users():
    """Retrieves all users."""
    stmt = db.select(User)
    users_list = db.session.scalars(stmt)
    result = users_schema.dump(users_list)
    return jsonify(result), 200

@users.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Retrieves a single user by their user_id."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": f"User with ID #{user_id} does not exist."}), 404
    result = user_schema.dump(user)
    return jsonify(result), 200

@users.route("/", methods=["POST"])
def create_user():
    """Creates a new user."""
    body_data = request.get_json()
    new_user = user_schema.load(body_data, session=db.session)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.dump(new_user), 201

@users.route("/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    """Updates specified fields of an existing user."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": f"User with ID #{user_id} does not exist."}), 404
    body_data = request.get_json()
    user = user_schema.load(body_data, instance=user, session=db.session, partial=True)
    db.session.commit()
    return user_schema.dump(user), 200

@users.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Deletes an existing user."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": f"User with ID #{user_id} does not exist."}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User with ID #{user_id} deleted successfully."}), 200