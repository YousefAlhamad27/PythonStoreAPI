from fastapi import FastAPI
# Update these lines to point inside the 'src' folder:
from src.Routers import MyFirstAPI, CustomersAPI, ProductsAPI, AuthAPI, RealAuthAPI,UserAPI
from src.Database.database import client, database
from src.Models.Customers import Customer
from src.Models.Users import User
from src.Models.Products import Product
from beanie import init_beanie
from contextlib import asynccontextmanager
 

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
app.include_router(UserAPI.router)
# app.include_router(AuthAPI.router)
app.include_router(RealAuthAPI.router)  
# def hello():
#     print("sup")

# hello()    
 