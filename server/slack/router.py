from fastapi import APIRouter

router = APIRouter()

@router.post("/incomingWebhook")
def test_api():
    return {"code": 200}


@router.post("/incomingWebhook")
def test_api():
    return {"code": 200}


@router.post("/incomingWebhook")
def test_api():
    return {"code": 200}
