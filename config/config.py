


import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Error , Missing API key")

MODELNAME = "gpt-4o-mini"
TEMPERATURE = 0


MAX_RETRIES = 2
DEFAULT_CONFIDENCE = 0.8


BaseIp = os.path.dirname(os.path.abspath(__file__))

RawPath = r"data\raw\sustainability_audit.csv"
ProcessedPath = r"data\processed\final_output.csv"


Logfile = r"logs\app.log"


EmissionFactors = {
    "flight": 0.115,
    "electricity": 0.5,
    "petrol": 2.31,
    "hotel": 15,
    "transport": 0.08
}