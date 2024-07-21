from typing import List
from fastapi import FastAPI
from database import *
from model.models import *

# create tables
create_db_and_tables()

# fastapi object
app = FastAPI()

# get categories
@app.get("/categories")
def get_categories() -> List[Category]:
    with Session(engine) as session:
        categories = session.exec(select(Category)).all()
        return categories
    

# post categories
@app.post("/categories")
def create_category(category: Category) -> None:
    with Session(engine) as session:
        cat = session.add(category)
        session.commit()
        return cat