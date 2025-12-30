from settings import settings
from gpt_service import check_validity_by_llm


def check_input(query: str) -> dict:
    banned_words = settings.BANNED_KEYWORDS
    competitors = settings.COMPETITORS

    for word in banned_words:
        if word in query:
            return {"valid" : False, "reason" : f"You are using banned word : {word}"}
    
    for word in competitors:
        if word in query:
            return {"valid" : False, "reason" : f"You are using competitor word : {word}"}
        
    return {"valid" : True, "reason" : ""}