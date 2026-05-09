

from typing import Dict

Keywords = [
    "flight", "plane", "air travel",
    "petrol", "diesel", "gasoline",
    "shipping", "freight", "delivery truck"
]

def validate(row: dict, classification: dict, emissions: dict):
    issues = []

    desc = str(row.get("description", "")).lower()
    scope = classification.get("predicted_scope")
    co2 = emissions.get("co2_kg", 0)


    if "flight" in desc and scope != "Scope 3":
        issues.append("flight scope mismatch")

   
    if co2 < 0:
        issues.append("negative emissions")

  
    if co2 == 0 and any(k in desc for k in Keywords):
        issues.append("implausible zero emissions for high-impact activity")

  
    if any(k in desc for k in Keywords) and co2 < 1:
        issues.append("suspiciously low emissions for high-impact activity")

    return {
        "status": "verified" if not issues else "flagged",
        "confidence": classification.get("confidence", 0.5) if not issues else 0.3,
        "issues": issues
    }