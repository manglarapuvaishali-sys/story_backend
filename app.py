from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
app=FastAPI()
client=genai.Client(api_key=os.environ["GEMINI_API_KEY"])
class storyrequest(BaseModel):
    prompt:str
@app.post("/story")
def chat(req:storyrequest):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=req.prompt
    )
    return {"question":req.prompt,"answer":response.text}
