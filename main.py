import uvicorn

from fastapi import FastAPI
from api import all_routers
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Market place by Minzifa Travel")
from pathlib import Path

current_file = Path(__file__)
current_file_dir = current_file.parent
project_root = current_file_dir.parent
project_root_absolute = project_root.resolve()
static_root_absolute = project_root_absolute / "static"  # or wherever the static folder actually is
app.mount("/static", StaticFiles(directory=static_root_absolute))


for router in all_routers:
    app.include_router(router, prefix='/v1')


origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
# from redis import asyncio as aioredis


# @app.on_event("startup")
# async def startup_event():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)