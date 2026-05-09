import openai
import random
import pandas as pd
from datetime import date, timedelta, datetime

vendors = ["IndiGo", "AWS", "Shell", "Marriott", "Uber", "Tata Power"]
expense_types = ["flight", "electricity", "petrol", "hotel", "transport"]

units = {
    "flight": "km",
    "electricity": "kwh",
    "petrol": "liters",
    "hotel": "nights",
    "transport": "km"
}

locations = ["India", "US", "UK"]

def random_date():
    start=datetime(2024,1,1)
    return start+timedelta(days=random.randint(0,365))

def generate_row(i):
    expense = random.choice(expense_types)
    vendor = random.choice(vendors)
    loc = random.choice(locations)

    noise_options = [
        "",
        " plus baggage",
        " tax included",
        " emergency booking",
        " includes service fee",
        " rush travel booking",
        " corporate discount applied"
    ]

    noise = random.choice(noise_options)

    description = f"{expense.capitalize()} at {vendor} in {loc}{noise}"

    return {
        "transaction_id": f"TXNID_{1000+i}",
        "date": random_date().strftime("%Y-%m-%d"),
        "vendor": vendor,
        "description": description,
        "amount": round(random.uniform(10, 1000), 2),
        "unit": units[expense],
        "location": loc,
        "expense_type": expense,
        "category": "travel" if expense in ["flight", "transport", "hotel"] else "energy",
        "expected_scope": (
            "Scope 1" if expense == "petrol"
            else "Scope 2" if expense == "electricity"
            else "Scope 3"
        )
    }
data =[generate_row(i) for i in range(1000)]
df=pd.DataFrame(data)
df.to_csv("sustainability_audit.csv", index=False)
print("file created")

