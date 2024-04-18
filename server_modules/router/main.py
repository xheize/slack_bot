# import json
#
# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
#
#
# slack_router = APIRouter()
#
#
# @slack_router.post("/event")
# def test_api():
#     return {"code": 200}
#
#
# @slack_router.post("/command")
# def status_command():
#     # slack_instance.send_webhook_message(webhook_name="AWS", msg={"text": "상태창 테스트"})
#     data = {
#         "response_type": "in_channel",
#         "text": f"SLACK_BOT: {slack_instance.status}",
#     }
#     return JSONResponse(content=data)
