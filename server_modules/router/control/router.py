from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def send_msg():

    return {"code": 200}
