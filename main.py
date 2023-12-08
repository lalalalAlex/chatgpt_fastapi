from fastapi import FastAPI
from request.request_api import request_router

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url='/',
    title='ChatGPT 4'
)

app.include_router(request_router)