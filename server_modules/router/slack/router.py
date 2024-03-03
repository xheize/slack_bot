from fastapi import APIRouter

from slack_modules.slack_client import SlackBot

router = APIRouter()
slack_instance = SlackBot()


@router.post("/sendMsg")
def test_api(
        channel_id: str,
        msg: str,
):
    slack_instance.send_static_msg(
        channel_id=channel_id,
        msg_string=msg
    )
    return {"code": 200}

