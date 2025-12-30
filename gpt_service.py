from settings import settings
from groq import Groq

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_answer(conversation) -> str:
    
    if len(conversation) == 0:
        return "No query found"
    
    prompt = "You are a edtech agent name Masai, you have to reply to the query about Masai School please be brief"

    system_message = [{"role" : "system", "content" : prompt}]

    input_messages = system_message + conversation

    print(input_messages)
    
    response = client.chat.completions.create(
        model=settings.GROQ_MODEL_NAME,
        messages=input_messages,
        temperature=0.5
    )

    return response.choices[0].message.content
