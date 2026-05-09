AI Sustainability Auditor
AI Sustainability Auditor is a modular carbon auditing platform designed to classify enterprise expenses into greenhouse gas emission scopes and estimate carbon emissions automatically.
The project combines LLM-based classification, deterministic validation logic, and an interactive dashboard to simulate how modern sustainability auditing systems work in enterprise environments.
The system is built using FastAPI, OpenAI, Pandas, and Streamlit.

________________________________________
Features

•	AI-based emission scope classification 

•	Carbon emission estimation engine 

•	Validation and audit checks 

•	Retry mechanism for failed classifications 

•	REST API with FastAPI 

•	Interactive Streamlit dashboard 

•	CSV export support 

•	Structured logging 

•	Modular project architecture 

________________________________________
Tech Stack

•	Python 

•	FastAPI 

•	Streamlit 

•	OpenAI API 

•	Pandas 

•	Pydantic 
________________________________________
Project Structure

AI-Sustainability-Auditor/


├── agents/

│   ├── classificationagent.py

│   ├── emissionagent.py

│   ├── criticagent.py

│   └── ingestionagent.py

│

├── services/

│   └── pipeline.py

│

├── config/

│   └── config.py

│

├── data/

│   ├── raw/

│   │   └── sustainability_audit.csv

│   │

│   └── processed/

│       └── final_output.csv

│    │

│    └── scripts/

│       └── generator.py

│

├── logs/

│   └── app.log

│

├── .gitignore

├──.env

├── dashboard.py

├── main.py

├── requirements.txt

└── README.md


________________________________________
Setup

Clone the repository

    git clone <your-repository-url>
    cd AI-Sustainability-Auditor

________________________________________
Create virtual environment

Windows
      
      python -m venv .venv
      .venv\Scripts\activate
Mac/Linux

      python3 -m venv .venv
      source .venv/bin/activate

________________________________________
Install dependencies

      pip install -r requirements.txt

________________________________________
Create .env file
Create a .env file in the project root directory.
       
       OPENAI_API_KEY=your_openai_api_key
________________________________________
Generate Dataset
Run the synthetic data generator:
python generator.py
This creates:
data/raw/sustainability_audit.csv
________________________________________
Run FastAPI Server
uvicorn main:app --reload
API URL:
http://127.0.0.1:8000
Swagger documentation:
http://127.0.0.1:8000/docs
________________________________________
Run Audit Pipeline
Open:
http://127.0.0.1:8000/run-audit
The pipeline:
•	loads transaction data 
•	classifies emission scope 
•	estimates emissions 
•	validates audit integrity 
•	saves processed results 
Output file:
data/processed/final_output.csv
________________________________________
Run Dashboard

streamlit run dashboard/dashboard.py

Dashboard includes:

•	total emissions 

•	emissions by scope 

•	vendor-level analysis 

•	transaction explorer 

•	CSV download 
________________________________________
Logging
Application logs are stored in:
logs/app.log
________________________________________
Future Improvements

•	ChromaDB integration 

•	Async processing 

•	Authentication 

•	Docker deployment 

•	CI/CD pipeline 

•	Cloud deployment 

•	Real emission factor datasets 

