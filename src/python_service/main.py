from fastapi import FastAPI

from python_service.routers.items import router as items_router

app = FastAPI()
app.include_router(items_router, prefix="/api")


@app.get("/")
def get_root() -> dict[str, str]:
    return {"message": "Hello, World!"}
