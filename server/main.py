from typing import Union
from fastapi import FastAPI, APIRouter

from slack.router import router as slack_router

import uvicorn

app = FastAPI()

app.include_router(prefix="/slack", router=slack_router)


@app.get("/ping")
def heart_beat():
    return {"heartbeat": True}


if __name__ == "__main__":
    config = uvicorn.Config(app, port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
