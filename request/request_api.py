from fastapi import APIRouter
from database.request_service import add_request


request_router = APIRouter(prefix='/request', tags=['Запросы и Ответы'])


@request_router.post('/request')
async def requests(request: str):
    result = add_request(request)
    return {'message': result}
