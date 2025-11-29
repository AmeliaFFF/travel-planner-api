from main import ma
from models.traveller import Traveller

class TravellerSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for Traveller model."""
    class Meta:
        model = Traveller
        load_instance = True
        ordered = True
        fields = ("traveller_id", "name", "email", "notes")

traveller_schema = TravellerSchema()
travellers_schema = TravellerSchema(many=True)