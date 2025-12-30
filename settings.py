import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME")

    BANNED_KEYWORDS = ["fees", "harm", "suicide", "attack", "explosive"]

    COMPETITORS = ["newton", "scaler", "udemy"]

    with open("masai_policy.txt", "r") as file:
        POLICY_TEXT = file.read()


settings = Settings()