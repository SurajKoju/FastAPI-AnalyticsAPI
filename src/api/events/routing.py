from fastapi import APIRouter
from .models import (EventModel, EventListModel, EventCreateModel, EventUpdateModel)
import os

router = APIRouter()


@router.get("/")
def read_events() -> EventListModel:
    return {
        "results": [{"id": 1}, {"id": 2}, {"id": 3}],
        "count": 3
    }
    
    
@router.post("/")
def create_event(payload:EventCreateModel) -> EventModel:
    data = payload.model_dump() #payload -> Dictionary
    return {"id": 123, **data} # Unpacking - data can have many values dictionary
    
    
@router.get("/{event_id}")
# This parts represents the data to be sent to Model
def get_events(event_id:int) -> EventModel:
    return {
        "id": event_id
    }
    
    
#PUT method is typically used to update an existing resource.
@router.put("/{event_id}")
def update_event(event_id:int, payload:EventUpdateModel) -> EventModel:
    data = payload.model_dump() #payload -> Dictionary
    return {"id": event_id, **data}
    