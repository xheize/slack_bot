from fastapi import APIRouter

slack_router = APIRouter()


@slack_router.post("/incomingWebhook")
def test_api():
    return {"code": 200}
