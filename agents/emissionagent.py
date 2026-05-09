


from config.config import EmissionFactors

class EmissionsAgent:
    def __init__(self):
        self.factors = EmissionFactors

    def calculate(self, row: dict, classification: dict) -> dict:
        amount = row.get("amount")

        if amount is None:
            return {"co2_kg": 0, "confidence": 0.0}

        try:
            amount = float(amount)
        except:
            return {"co2_kg": 0, "confidence": 0.0}

        factor = self.factors.get(classification.get("expense_type"), 0.1)
        co2 = amount * factor

        return {
            "co2_kg": round(co2, 2),
            "confidence": classification.get("confidence", 0.8)
        }