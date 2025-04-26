from fastapi import FastAPI
from pydantic import BaseModel
from services.openai_service import generate_image  #type: ignore

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate-image")
def generate_image_endpoint(request: PromptRequest):
    image_url = generate_image(request.prompt)
    return {"image_url": image_url}
