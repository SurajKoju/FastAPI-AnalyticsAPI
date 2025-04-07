from fastapi import FastAPI
from api.events.routing import router as event_router

app = FastAPI()
app.include_router(event_router, prefix='/api/events')

@app.get("/")
async def root():
    return {"message": "Hello Goldie"}

@app.get("/health")
def read_api_health():
    return {"status": "ok"}

