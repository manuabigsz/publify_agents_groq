from fastapi import FastAPI
from pydantic import BaseModel
from src.novo_back.main import run

app = FastAPI()

class InputData(BaseModel):
    topic: str
    url: str
    platform: str
    text_length: str
    target_public:str
    tone: str
    
@app.post("/generate")
def generate_content(data: InputData):
    try:
        result = run(data.topic, data.url, data.platform, data.text_length, data.target_public,data.tone)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
