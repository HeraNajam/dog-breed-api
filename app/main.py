from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ImageInput(BaseModel):
    image_url: str

@app.post("/predict")
def predict(input: ImageInput):
    # placeholder
    return {"breed": "Golden Retriever"}
