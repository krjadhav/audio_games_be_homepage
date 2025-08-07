from fastapi import FastAPI
import os
import uvicorn

app = FastAPI(title="Audio Games Homepage", version="1.0.0")

@app.get("/home")
def get_home():
    return {
        "tokens": 1500,
        "tiles":[{
            "id": 1,
            "type": "game",
            "name": "Trivia Champ",
            "game_type": "trivia_champ",
            "image_url": "https://imagedelivery.net/Ig_rE6uK4J6SFx9mrj42PA/62535c75-a1c3-42ce-1da5-4e72759a0000/public"
        },
        {
            "id": 2,
            "type": "game",
            "name": "Word Rescue",
            "game_type": "word_rescue",
            "image_url": "https://imagedelivery.net/Ig_rE6uK4J6SFx9mrj42PA/eb26c456-6497-4ec1-0ef1-65b79713db00/public"
        },
        {
            "id": 3,
            "type": "info",
            "name": "More Coming Soon!",
            "game_type": "",
            "image_url": "https://imagedelivery.net/Ig_rE6uK4J6SFx9mrj42PA/dd58a734-1c88-4208-947f-fc7c47c98d00/public"
        }
        ]
    }

@app.get("/health")
async def health():
    return {"status": "Audio Games is live!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)