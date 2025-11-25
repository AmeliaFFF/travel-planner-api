from main import ma
from models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for User model."""
    class Meta:
        model = User
        load_instance = True
        ordered = True
        fields = ("user_id", "name", "email")

user_schema = UserSchema()
users_schema = UserSchema(many=True)