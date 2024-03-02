from fastapi import FastAPI

from server_modules.router.slack.router import router as slack_router

import uvicorn

app = FastAPI()

app.include_router(prefix="/slack", router=slack_router)


@app.get("/api/v2/heart-beat")
def heart_beat():
    return {"heartbeat": True}


config = uvicorn.Config(app, port=8000, log_level="info")
server = uvicorn.Server(config)

if __name__ == "__main__":
    print("It's Server Main.py File\nStandAlone run not support\nplz Combine with fork or Process")
