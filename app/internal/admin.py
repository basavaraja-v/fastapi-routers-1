from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    print("request.json")
    return {"message": "Admin getting schwifty"}