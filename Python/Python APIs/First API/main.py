from fastapi import FastAPI
from routers import MyFirstAPI,CustomersAPI,ProductsAPI
from database import client,database
from beanie import init_beanie
from contextlib import asynccontextmanager
from Models.Customers import Customer
from Models.Users import User
from Models.Products import Product

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_beanie(database=database,document_models=[Customer,Product,User])
    print("Connecting to DB")
    yield
    print("Closing Connection")
    client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(MyFirstAPI.router)
app.include_router(CustomersAPI.router)
app.include_router(ProductsAPI.router)


# def hello():
#     print("sup")

# hello()    
 