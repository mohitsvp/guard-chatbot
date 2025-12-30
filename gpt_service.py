from settings import settings
from groq import Groq
from pydantic import BaseModel
import json

class ValiditySchema(BaseModel):
    valid : bool
    reason : str

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_answer(conversation) -> str:
    
    if len(conversation) == 0:
        return "No query found"
    
    prompt = "You are a edtech agent name Masai, you have to reply to the query about Masai School please be brief"

    system_message = [{"role" : "system", "content" : prompt}]

    input_messages = system_message + conversation
    
    response = client.chat.completions.create(
        model=settings.GROQ_MODEL_NAME,
        messages=input_messages,
        temperature=0.5
    )

    return response.choices[0].message.content


def check_validity_by_llm(query: str) -> ValiditySchema:
    if not query:
        return "No query provided"
    
    prompt = f"""Act as a security checker, your task is to flag inappropriate queries by valid as False which are violating the policy otherwise reply with True validity which has no reason
    
    === POLICY AT MASAI ===
    {settings.POLICY_TEXT}
    === POLICY END HERE ==
    """

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL_NAME,
        messages=[
            {"role" : "system", "content" : prompt},
            {"role" : "user", "content": query}
        ],
        response_format={
            "type" : "json_schema",
            "json_schema": {
                "name": "validity_schema",
                "schema": ValiditySchema.model_json_schema()
            }
        }
    )

    return json.loads(response.choices[0].message.content)

