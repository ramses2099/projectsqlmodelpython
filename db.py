from sqlmodel import create_engine, SQLModel
from sqlmodel import Session


db_name = "database.db"
DATABASE_URL = f"sqlite:///{db_name}"
connect_args = {"check_same_thread":False}

engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    
