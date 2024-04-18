from fastapi import APIRouter
from fastapi.responses import JSONResponse
from slack_modules.main import SlackBot

router = APIRouter()
slack_instance = SlackBot()


@router.post("/event")
def test_api():
    return {"code": 200}


@router.post("/command")
def status_command():
    data = {
        "response_type": "in_channel",
        "text": f"SLACK_BOT: {slack_instance.status}",
    }
    return JSONResponse(content=data)


@router.post("/webhook")
def status_command():
    result = slack_instance.send_webhook_message(webhook_name="AWS", msg={"text": "웹훅 테스트 압니다."})
    if result:
        data = {
            "code": "200",
            "data": f"ok",
        }
        return JSONResponse(content=data)
    else:
        data = {
            "code": "402",
            "data": f"failed",
        }
        return JSONResponse(content=data)


@router.post("/sendMsg")
def test_api(
        channel_id: str,
        msg: str,
):
    slack_instance.send_post_message(
        channel_id=channel_id,
        text=msg
    )
    return {"code": 200}
