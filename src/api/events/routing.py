from fastapi import APIRouter, Depends, HTTPException
from .models import (EventModel, EventCreateSchema, EventListSchema, EventUpdateSchema, EventDeleteSchema)
from api.db.session import get_session
from sqlmodel import Session, select

import os

router = APIRouter()


@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):
    
    # query = "SELECT * FROM  eventmodel ORDER BY id DESC LIMIT 10"
    query = select(EventModel).order_by(EventModel.id.desc()).limit(50)
    results = session.exec(query).all()
    return {
        "results": results,
        "count": len(results)
    }
    
    
@router.post("/", response_model=EventModel)
def create_event(payload:EventCreateSchema, session: Session = Depends(get_session)):
    data = payload.model_dump() # Payload -> Dictionary
    obj = EventModel.model_validate(data) # Passing the data variable to the obj
    session.add(obj) # 
    session.commit() # adding to the database
    
    session.refresh(obj)
    return obj
    
    

@router.get("/{event_id}", response_model=EventModel)
# This parts represents the data to be sent to Model
def get_events(event_id:int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    
    if not result:
        raise HTTPException(status_code = 404, detail="event not found")
    return result
    
    

@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id:int, payload:EventUpdateSchema, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()

    if not obj:
        raise HTTPException(status_code = 404, detail="event not found")

    data = payload.model_dump() # Payload -> Dictionary
    
    for k, v in data.items():
        setattr(obj, k, v)
    
    session.add(obj) # 
    session.commit() # adding to the database
    
    session.refresh(obj)
    return obj


@router.delete("/{event_id}", response_model=EventDeleteSchema)
def delete_event(event_id: int, session: Session = Depends(get_session)):
    # Find the event
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")

    # Delete the event
    session.delete(obj)
    session.commit()

    return EventDeleteSchema(id=event_id)