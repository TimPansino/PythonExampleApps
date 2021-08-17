import asyncio
from time import sleep

from fastapi import APIRouter, BackgroundTasks, Request

router = APIRouter()

async def some_task():
    asyncio.sleep(2)
    return


async def some_async_task():
    await asyncio.sleep(2)
    return


@router.post("/test-async-endpoint")
async def test_async_endpoint(
    request: Request, background_tasks: BackgroundTasks, a: str = "some param"
):
    background_tasks.add_task(some_async_task)
    asyncio.sleep(1)
    return {"return": a}


@router.post("/test-endpoint")
def test_endpoint(
    request: Request, background_tasks: BackgroundTasks, a: str = "some param"
):
    background_tasks.add_task(some_task)
    sleep(1)
    return {"return": a}
