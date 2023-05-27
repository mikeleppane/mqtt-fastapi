from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong() -> dict:
    return {"ping": "pong!"}
