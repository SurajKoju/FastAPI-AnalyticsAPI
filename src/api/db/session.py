# Creating Database Instance Engine to create the database table itself
import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplementedError("Database URL needs to be setup")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print("creating Database")
    # Connects to database and ensures the table which are created from the models class
    SQLModel.metadata.create_all(engine)
    
    
    
def get_session():
    with Session(engine) as session:
        yield session