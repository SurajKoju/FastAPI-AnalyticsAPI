from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.events.routing import router as event_router
from contextlib import asynccontextmanager
from api.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix='/api/events')

@app.get("/")
async def root():
    return HTMLResponse(content="<h1><center>Hello Goldie</h1></center>", status_code=200)

@app.get("/health")
def read_api_health():
    return {"status": "ok"}
