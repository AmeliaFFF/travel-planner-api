from main import ma

class ExpenseSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("expense_id", "trip_id", "date", "category", "description", "cost_total", "currency_code")

expense_schema = ExpenseSchema()
expenses_schema = ExpenseSchema(many=True)