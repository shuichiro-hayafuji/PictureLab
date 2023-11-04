from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/sample")
def sample():
    data = {
        "message": "Hello, Sample!",
        "status": 200
    }
    return JSONResponse(content=data)
