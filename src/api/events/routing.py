from fastapi import APIRouter
from .schemas import EventSchema


router = APIRouter()


@router.get("/")
def read_events():
    return {
        "results": [1,2,3]
    }
    
@router.get("/{event_id}")

# This parts represents the data to be sent to schema
def get_events(event_id:int) -> EventSchema:
    return {
        "id": event_id
    }