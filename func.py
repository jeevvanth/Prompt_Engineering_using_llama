from model import TranslationRequest
# from openai import OpenAI
import groq
import os

os.environ["GROQ_API_KEY"] = ""
client = groq.Client(api_key=os.environ["GROQ_API_KEY"])



def translate_text(input_str:str) :
    completion=client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are an expert translator who translates text from english to spanish and only return translated text",
            },
            {"role": "user", "content": input_str},
        ]
    )

    return completion.choices[0].message.content


request_obj = TranslationRequest(input_str="")
translated_text = translate_text(request_obj.input_str)
