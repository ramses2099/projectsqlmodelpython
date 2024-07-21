import datetime
from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
   
# other models 
class Customer(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   firstname:str
   lastname:str
   streetadress:str
   city:str
   state:str
   zipcode:str
   phonenumber:str
   update_at: Optional[datetime.datetime]
   create_at: datetime.datetime = Field(default=datetime.datetime.now())
   # relations
   orders: list["Order"] = Relationship(back_populates = "customer")
  
class Employee(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   firstname:str
   lastname:str
   dob:datetime.datetime
   streetadress:str
   city:str
   state:str
   zipcode:str
   phonenumber:str
   update_at: Optional[datetime.datetime]
   create_at: datetime.datetime = Field(default=datetime.datetime.now())
    # relations employee with order
   orders: list["Order"] = Relationship(back_populates = "employee")
    
class Order(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   orderdate: datetime.datetime = Field(default=datetime.datetime.now())
   shipdate: Optional[datetime.datetime]
   # test
   customerid: int = Field(foreign_key="customer.id")
   employeeid: int = Field(foreign_key="employee.id")  
   update_at: Optional[datetime.datetime]
   create_at: datetime.datetime = Field(default=datetime.datetime.now())
   # relations
   customer: Customer = Relationship(back_populates="orders")   
   # relations order with orderdetails
   orderdetails: list["OrderDetail"] = Relationship(back_populates = "order")
   # relations order with employee
   employee: Employee = Relationship(back_populates="orders")   
   
class OrderDetail(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   order_id:int = Field(foreign_key="order.id")
   product_id: int = Field(foreign_key="product.id")
   price: float
   quantity: int  
   update_at: Optional[datetime.datetime]
   create_at: datetime.datetime = Field(default=datetime.datetime.now())
   # relations order with orderdetails
   order: Order = Relationship(back_populates = "orderdetails")   
   # relations orde details with product
   products: List["Product"] = Relationship(back_populates="orderdetail")

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    update_at: Optional[datetime.datetime]
    create_at: datetime.datetime = Field(default=datetime.datetime.now())
    # relation category with product
    products: list["Product"] = Relationship(back_populates = "category")
 
class ProductVendor(SQLModel, table=True):
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    vendor_id: int = Field(foreign_key="vendor.id", primary_key=True)
    wholesaleprice: float
    daystodeliver: int
    update_at: Optional[datetime.datetime]
    create_at: datetime.datetime = Field(default=datetime.datetime.now())
 
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    reatilprice: float
    quantityonhad: int
    category_id: int = Field(foreign_key="category.id")
    update_at: Optional[datetime.datetime]
    create_at: datetime.datetime = Field(default=datetime.datetime.now())
    # relation product with category
    category: Category = Relationship(back_populates="products")
    # realtion detatils with product
    orderdetail: OrderDetail = Relationship(back_populates="products")
    # realiton many to may product vendor
    vendors: list["Vendor"] = Relationship(back_populates="products", link_model=ProductVendor)

class Vendor(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   firstname:str
   lastname:str
   streetadress:str
   city:str
   state:str
   zipcode:str
   phonenumber:str
   faxnumber:Optional[str]
   webpage:Optional[str]
   email:str
   update_at: Optional[datetime.datetime]
   create_at: datetime.datetime = Field(default=datetime.datetime.now())
   # realiton many to may product vendor
   products: list["Product"] = Relationship(back_populates="vendors", link_model=ProductVendor)
 

    
  
