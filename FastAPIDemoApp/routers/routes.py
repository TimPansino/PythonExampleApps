import asyncio
import time
import random

from fastapi import APIRouter, BackgroundTasks, Request

router = APIRouter()


@router.get("/")
def index(request: Request, background_tasks: BackgroundTasks):
    return "Hello from FastAPI!"


@router.get("/async")
async def index_async(request: Request, background_tasks: BackgroundTasks):
    return "Hello from FastAPI!"


@router.get("/error")
async def error(request: Request, background_tasks: BackgroundTasks):
    raise RuntimeError("Oops")

@router.get('/spotty')
async def spotty():
    if random.randint(1, 5) == 5:
        raise RuntimeError("Oops")
    else:
        return "Hello from Flask!"

@router.get('/slow')
async def slow():
    time.sleep(5)
    return "Hello from Falcon! (slowly)"
