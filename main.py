import uvicorn

from fastapi import FastAPI
from api import all_routers

app = FastAPI(title="Market place by Minzifa Travel")

for router in all_routers:
    app.include_router(router, prefix='/v1')

# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
# from redis import asyncio as aioredis


# @app.on_event("startup")
# async def startup_event():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)