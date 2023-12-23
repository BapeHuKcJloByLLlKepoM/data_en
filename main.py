from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
        text: str


app = FastAPI()

classifier = pipeline("sentiment-analysis")

@app.get("/")
async def root():
	return {"message": "HELLO"}

@app.post("/predict/")
def predict(item: Item):
        return classifier(item.text)[0]


#@app.get("/predict/")
#def predict():
        #return classifier("I like")[0]
