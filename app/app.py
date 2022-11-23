from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def home():
    return {"data": "you're off to a great start"}
