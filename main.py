
from fastapi import FastAPI
import pandas as pd
import os
import logging

from agents.classificationagent import ClassificationAgent
from agents.emissionagent import EmissionsAgent
from agents.criticagent import validate
from config.config import Logfile
from services.pipeline import AuditPipeline

from config.config import (
    OPENAI_API_KEY,
    RawPath,
   ProcessedPath,
   Logfile,
  
)


app = FastAPI()


classifier = ClassificationAgent(api_key=OPENAI_API_KEY)
emissions = EmissionsAgent()
pipeline = AuditPipeline(classifier, emissions, validate)


logging.basicConfig(
    filename=Logfile,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.get("/run-audit")
def runaudit():
    try:
        logging.info("Starting audit pipeline")

        df = pd.read_csv(RawPath)
        df = df.head(10)

        result_df = pipeline.run(df)

        result_df.to_csv(ProcessedPath, index=False)

        logging.info(f"Audit completed for {len(result_df)} rows")

        return result_df.to_dict(orient="records")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        return {"error": str(e)}


@app.get("/")
def home():
    return {"message": "Sustainability Auditor API is running"}