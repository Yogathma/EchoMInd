%%writefile app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="EchoMind – Personality Aware Companion AI",
    description="Memory Extraction + Personality Engine",
    version="1.0"
)

class Messages(BaseModel):
    messages: List[str]

class PersonalityRequest(BaseModel):
    base_reply: str
    personality: str

@app.post("/extract_memory")
def extract_memory(data: Messages):
    preferences = []
    emotions = []
    facts = []

    for msg in data.messages:
        m = msg.lower()

        if "like" in m or "love" in m or "prefer" in m:
            preferences.append(msg)

        if any(w in m for w in ["stress", "nervous", "happy", "sad", "scared", "anxious"]):
            emotions.append(msg)

        if any(w in m for w in ["study", "studying", "intern", "robot", "name", "work"]):
            facts.append(msg)

    return {
        "user_preferences": list(set(preferences)),
        "emotional_patterns": list(set(emotions)),
        "facts_to_remember": list(set(facts))
    }

@app.post("/personality")
def personality_engine(req: PersonalityRequest):
    base = req.base_reply
    p = req.personality.lower()

    if p == "mentor":
        styled = f"Certainly. {base} Let us approach this step by step."
    elif p == "witty":
        styled = f"{base} 😄🔥 Chill da, we got this!"
    elif p == "therapist":
        styled = f"I hear you. {base} How does this make you feel?"
    else:
        styled = base

    return {"styled_reply": styled}

@app.get("/")
def root():
    return {"status": "Backend running successfully"}
