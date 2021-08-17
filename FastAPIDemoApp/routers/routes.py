import asyncio
from time import sleep

from fastapi import APIRouter, BackgroundTasks, Request

router = APIRouter()

@router.get("/")
def index(request: Request, background_tasks: BackgroundTasks):
    return "Hello from FastAPI!"

@router.get("/async")
async def index_async(request: Request, background_tasks: BackgroundTasks):
    return "Hello from FastAPI!"

@router.get("/error")
async def index_async(request: Request, background_tasks: BackgroundTasks):
    raise RuntimeError("Oops")
