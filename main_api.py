from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK"}

@app.get("/info")
def info():
    return {"name": "language translator", "description": "Translate German Sentences into English."}

@app.get("/translate")
def translate(query: str):
    return translate(transformer, query)
