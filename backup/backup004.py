from sqlmodel import create_engine, SQLModel
from sqlmodel import Session, select

db_name = "database.db"
sqlite_url = f"sqlite:///{db_name}"
connect_args = {"check_same_thread":False}

engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
    
