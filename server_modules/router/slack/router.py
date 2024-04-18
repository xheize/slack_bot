from fastapi import APIRouter
from slack_modules.main import SlackBot

router = APIRouter()
slack_instance = SlackBot()


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

