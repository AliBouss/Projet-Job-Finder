from fastapi import FastAPI

import uvicorn

app = FastAPI(title='jobboard', version="O.1.0")


@app.get("/")
def test_api():
    return {"test": "hello world"}