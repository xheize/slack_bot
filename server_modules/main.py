from server_modules.router.slack.router import router as slack_router
from fastapi import FastAPI

import uvicorn
import os

app = FastAPI()

app.include_router(prefix="/slack", router=slack_router)
# app.include_router(prefix="/api/v1", router=module_router)


@app.get("/api/v2/heart-beat")
def heart_beat():
    return {"heartbeat": True}


class APIServer:

    def __init__(self) -> None:
        self.app = app
        self.server = None
        self.status = "init"

    async def run(self):
        if self.server:
            print("Already Running Server")
            return
        config = uvicorn.Config(self.app, host="0.0.0.0", port=int(os.environ.get("SERVER_PORT")), log_level="info", loop="asyncio")
        self.server = uvicorn.Server(config)
        await self.server.serve()

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server = None


if __name__ == "__main__":
    print("It's Server Main.py File\nStandAlone run not support\nplz Combine with fork or Process")
