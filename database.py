from sqlmodel import create_engine, SQLModel

db_name = "database.db"
engine = create_engine(f"sqlite:///{db_name}", echo=True)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)