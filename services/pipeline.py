import pandas as pd
import math

class AuditPipeline:
    def __init__(self, classifier, emissions_agent, validator):
        self.classifier = classifier
        self.emissions_agent = emissions_agent
        self.validator = validator

    def _safe_value(self, val):
        if val is None:
            return 0
        if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
            return 0
        try:
            return float(val)
        except:
            return 0

   
    def constraints(self, result, row, emissions):
        desc = str(row.get("description", "")).lower()
        co2 = self._safe_value(emissions.get("co2_kg"))

        HIGH_RISK_KEYWORDS = [
            "flight", "plane", "air travel",
            "petrol", "fuel", "diesel", "gasoline",
            "electricity", "shipping", "freight"
        ]

        if co2 == 0 and any(k in desc for k in HIGH_RISK_KEYWORDS):
            result["status"] = "flagged"
            result["confidence"] = min(result.get("confidence", 0.5), 0.2)

            issues = result.get("issues", [])
            issues.append("hard constraint: zero CO2 for high-impact activity")
            result["issues"] = issues

        
        if co2 < 0:
            result["status"] = "flagged"
            result["confidence"] = 0.1

            issues = result.get("issues", [])
            issues.append("negative emissions detected")
            result["issues"] = issues

        return result

    def show(self, row: dict):
        classification = self.classifier.classify(row)
        emissions = self.emissions_agent.calculate(row, classification)
        audit = self.validator(row, classification, emissions)
        audit = self.constraints(audit, row, emissions)

        return {
        "transaction_id": row.get("transaction_id"),
        "vendor": row.get("vendor"),
        "description": row.get("description"),
        "predicted_scope": classification.get("predicted_scope"),
        "co2_kg": self._safe_value(emissions.get("co2_kg")),
        "status": audit.get("status"),
        "confidence": self._safe_value(audit.get("confidence"))
    }
  
  
    
   
    def run(self, df: pd.DataFrame):
        results = []

        for _, row in df.iterrows():
            results.append(self.show(row.to_dict()))

        out = pd.DataFrame(results)

 

        return out