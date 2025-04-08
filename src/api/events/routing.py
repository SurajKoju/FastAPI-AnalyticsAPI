from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema


router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [{"id": 1}, {"id": 2}, {"id": 3}],
        "count": 3
    }
    

'''
data: dict This parameter takes the user-sent data and returns the same data. 
            The variable type is important for returning the data correctly.
'''    

@router.post("/")
def create_event(data:dict):
    return data
    
    
@router.get("/{event_id}")
# This parts represents the data to be sent to schema
def get_events(event_id:int) -> EventSchema:
    return {
        "id": event_id
    }