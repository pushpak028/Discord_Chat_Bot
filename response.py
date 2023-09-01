import load_json
from difflib import get_close_matches
import random

def find_tag(userin,kb):
    tag = get_close_matches(userin,[i["tag"]for i in kb["intents"]],n=1,cutoff=0.6)
    if tag:
        return tag[0]
    else:
        return None

def response(question,kb):
    for i in kb["intents"]:
        if i["tag"] == question:
            answer = random.choice(i["responses"])
            return answer

def pattern(question,kb):
    for i in kb["intents"]:
        if i["tag"] == question:
            answer = random.choice(i["patterns"])
            return answer
    
def chatbot(question):
    kb : dict = load_json.load1("intents.json")
    if question:
        answer = response(question,kb)
        if answer!= "...":
            return answer
        else:
            answer = pattern(question,kb)
            return answer






