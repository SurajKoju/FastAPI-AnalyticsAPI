from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from api.events.routing import router as event_router

app = FastAPI()
app.include_router(event_router, prefix='/api/events')

@app.get("/")
async def root():
    return HTMLResponse(content="<h1><center>Hello Goldie</h1></center>", status_code=200)

@app.get("/health")
def read_api_health():
    return {"status": "ok"}
