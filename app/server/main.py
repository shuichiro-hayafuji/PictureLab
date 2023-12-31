from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from app.server.api.crud_user import router as crud_user_router
from app.server.api.sample import router as sample_router

app = FastAPI()
app.include_router(crud_user_router)
app.include_router(sample_router)

@app.get("/api")
def api():
    data = {
        "message": "Hello, FastAPI",
        "status": 200
    }
    return JSONResponse(content=data)

# staticディレクトリにあるindex.htmlを使う (Svelte用)
app.mount("/", StaticFiles(directory="app/server/static", html=True), name="static")
