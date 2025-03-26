from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY")

@app.get("/")
def home():
    return{"message":"Baackend is running!"}

class ImageRequest(BaseModel):
    prompt: str

@app.post("/generate-image")
def generate_image(request: ImageRequest):
    print(f"APIKEY: {DEEPAI_API_KEY}")
    response = requests.post(
        "https://api.deepai.org/api/text2img",
        data={"text": request.prompt},
        headers={"api-key": DEEPAI_API_KEY}
    )
    result = response.json()


    print(f"Recieved prompt: {request.prompt}")
    print(f"Recieved data: {result}")

    return {"image_url": result.get("output_url", "")} 
