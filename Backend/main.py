from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEEPAI_API_KEY = "8715588c-32f1-4c98-8b35-0382f330b74d"

@app.get("/")
def home():
    return{"message":"Baackend is running!"}

class ImageRequest(BaseModel):
    prompt: str

@app.post("/generate-image")
def generate_image(request: ImageRequest):
    response = requests.post(
        "https://api.deepai.org/api/text2img",
        data={"text": request.prompt},
        headers={"api-key": DEEPAI_API_KEY}
    )
    result = response.json()


    print(f"Recieved prompt: {request.prompt}")
    print(f"Recieved data: {result}")

    return {"image_url": result.get("output_url", "")} 
