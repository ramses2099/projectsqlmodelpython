from sqlmodel import Session, select
from database import engine, create_db_and_tables
from model.models import *
import os

def select_herores() -> None:
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        heros = results.all()
        for h in heros:
            print(h)
            
def select_herores_limit_and_offset(limit: int, offset: int) -> None:
    with Session(engine) as session:
        statement = select(Hero).offset(offset).limit(limit)
        results = session.exec(statement)
        heros = results.all()
        for h in heros:
            print(h)

def select_hero_byid(id: int) -> None:
    with Session(engine) as session:
        hero = session.get(Hero, id)      
        print(hero)

def insert_data() -> None:
    teams =[
        Team(name="Preventers", headquarters="Sharp Tower"),
        Team(name="Z-Force", headquarters="Sister Margarets Bar"),
    ]
        
    heros = [
        Hero(name="Deadpond", secret_name="Dive Wilson", team_id=1),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador", team_id=2),
        Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48, team_id=2),
        Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
        Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
        Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
        Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93),
    ]
   
      
    # insert into the database
    with Session(engine) as session:
        for te in teams:
           session.add(te) 
        
        for he in heros:
            session.add(he)
        session.commit()

def update_heroes() -> None:
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 2)
        results = session.exec(statement)
        hero = results.one()
        hero.age = 12
        session.add(hero)
        session.commit()
        session.refresh(hero)

def delete_hero_byid(id: int) -> None:
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == id)
        results = session.exec(statement)
        hero = results.one()
        print(f"Hero: {hero}")
        
        session.delete(hero)
        session.commit()
        

def main():
    
    # create tables
    create_db_and_tables()
    # select from the database
    # with Session(engine) as session:
    #     statement = select(Hero).where(Hero.name == "Spider-Boy")
    #     hero = session.exec(statement).first()
    #     print(hero)
    
    # select_herores()
    # update_heroes()
    # select_hero_byid(2)

    # select_herores_limit_and_offset(3, 3)
    # delete_hero_byid(id=2)
    # select_herores()
    
    # with Session(engine) as session:
    #     cat = Category(description="Tete 4")
    #     session.add(cat)
    #     session.commit()
        
    #     proct = Product(name="product03",
    #                     description="description product01",
    #                     reatilprice=20.2,
    #                     quantityonhad=20,
    #                     category_id=cat.id)
    #     session.add(proct)
    #     session.commit()
    
    # with Session(engine) as session:
    #     cat = Category(description="Tete 5")
        
    #     proct = Product(name="product04",
    #                     description="description product01",
    #                     reatilprice=28.2,
    #                     quantityonhad=2,
    #                     category=cat)
    #     session.add(proct)
    #     session.commit()
    
    # with Session(engine) as session:
    #     proct01 = Product(name="product06",
    #                     description="description product06",
    #                     reatilprice=30.2,
    #                     quantityonhad=5)
    #     proct02 = Product(name="product07",
    #                     description="description product07",
    #                     reatilprice=22.2,
    #                     quantityonhad=5)
        
    #     cat = Category(description="category 6",products=[proct01, proct02])
        
    #     session.add(cat)
    #     session.commit()
    
    # with Session(engine) as session:
    #     statement = select(Product).where(Product.id == 2)
    #     result = session.exec(statement)
    #     product = result.one()
    #     category = product.category
    #     print(f"Caterory product 1: {category.description}")
    
    
    print("ok")

if __name__ == "__main__":
    os.system("cls")
    main()