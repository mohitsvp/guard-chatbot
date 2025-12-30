from settings import settings


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