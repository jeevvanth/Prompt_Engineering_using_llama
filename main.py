from typing import Union
from fastapi import FastAPI,HTTPException
from openai import OpenAI
from func import translate_text
from model import TranslationRequest
import os


app=FastAPI()

# client=OpenAI()



@app.get("/")
def readroot():
    return {"Hello":" World!"}

@app.get("/items/{itemid}")
def readitem(itemid:int,q:Union[str,None]=None):
    return {"itemid": itemid,"q":q}

@app.post("/translate/")

async def translate(request:TranslationRequest) :
    try:
        translated_text=translate_text(request.input_str)
        return {"translated text":translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

