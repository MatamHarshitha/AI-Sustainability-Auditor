
from openai import OpenAI
from pydantic import BaseModel
from typing import Literal
import os


class ClassificationOutput(BaseModel):
    expense_type: str
    predicted_scope: Literal["Scope 1", "Scope 2", "Scope 3"]
    reasoning: str
    confidence: float


class ClassificationAgent:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def _build_prompt(self, row: dict) -> str:
        return f"""
Classify the emission scope.

Return JSON:
{{
  "expense_type": "",
  "predicted_scope": "",
  "reasoning": "",
  "confidence": 0.0
}}

DATA:
{row}
"""

    def classify(self, row: dict) -> dict:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Return valid JSON only"},
                {"role": "user", "content": self._build_prompt(row)}
            ],
            response_format={"type": "json_object"},
            temperature=0
        )

        try:
            return ClassificationOutput.model_validate_json(
                response.choices[0].message.content
            ).model_dump()
        except Exception:
            return {
                "expense_type": row.get("expense_type"),
                "predicted_scope": "Scope 3",
                "reasoning": "fallback",
                "confidence": 0.0
            }