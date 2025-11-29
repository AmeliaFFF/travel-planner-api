from main import ma
from models.expense import Expense

class ExpenseSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for Expense model."""
    class Meta:
        model = Expense
        load_instance = True
        ordered = True
        include_fk = True
        fields = ("expense_id", "trip_id", "date", "category", "description", "cost_total", "currency_code")

expense_schema = ExpenseSchema()
expenses_schema = ExpenseSchema(many=True)