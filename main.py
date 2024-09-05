from fastapi import FastAPI
from pydantic import BaseModel

class Test(BaseModel):
    text : str



app = FastAPI()


@app.post("/")
def gettest(req : Test):
    print(req.text)
    return "valid"