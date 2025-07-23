from pydantic import BaseModel

class TranslationRequest(BaseModel) :
    input_str:str