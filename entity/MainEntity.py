class MainEntity(object):
    income = ""
    outcome = ""
    total_income = ""
    total_outcome = ""

    def serialize(self):
        return {
            'income': self.income,
            'outcome': self.outcome,
            'total_income': self.total_income,
            'total_outcome': self.total_outcome
        }
