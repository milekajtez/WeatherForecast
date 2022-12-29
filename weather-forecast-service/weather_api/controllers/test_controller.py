from fastapi import APIRouter

router = APIRouter()


@router.get("", tags=['test'])
async def get_test_message():
    return 'This is test message'
