from dataclasses import dataclass

@dataclass
class Expense:
    title:str
    category:str
    amount:float
    expense_date:str
    notes:str=""
    