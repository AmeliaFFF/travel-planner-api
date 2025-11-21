from main import ma

class TravellerSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("traveller_id", "name", "email", "notes")

traveller_schema = TravellerSchema()
travellers_schema = TravellerSchema(many=True)