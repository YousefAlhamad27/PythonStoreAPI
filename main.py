from datetime import datetime, timezone

from fastapi import FastAPI
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

        existing_users_count = await User.find_all().count()
    
        if existing_users_count == 0:
          print("Users collection is empty. Seeding default user...")

          default_user = User(
            username="sql_veteran_100",
            email="nosql_newbie@example.com",
           memberSince=datetime(2026, 7, 20, 0, 0, 0, tzinfo=timezone.utc),
            address={
                "city": "Amman",
                "street": "Rainbow St"
            },
            orders=[
                {
                    "orderId": "ORD-1001",
                    "date": datetime(2026, 7, 20, 14, 5, 0, tzinfo=timezone.utc),
                    "items": [
                        {
                            "productId": "PROD-001",
                            "quantity": 1,
                            "priceAtPurchase": 129.99
                        },
                        {
                            "productId": "PROD-002",
                            "quantity": 2,
                            "priceAtPurchase": 18.5
                        }
                    ],
                    "status": "Processing"
                }
            ],
            # This hash represents the password "1234"
            password="$argon2id$v=19$m=65536,t=3,p=4$RxnuoNuU2jYD+xPVmp7u8A$ePz30Gj8sA1tgIhGDJQJ1vN8/xzrEFLxp7Wk4AFQRM0" 
        )
        
        # Insert the default user into the database
          await default_user.insert()
          print("Default user seeded successfully!")
        else:
         users=await User.find_all().to_list()
         await User.delete_all(users)
         print(f"Database already contains {existing_users_count} users. Skipping seed.")
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
 