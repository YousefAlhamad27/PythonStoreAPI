from motor.motor_asyncio import AsyncIOMotorClient
from internal.config import settings


Mongo_String="mongodb://localhost:27017/"
#Mongo_String="mongodb://host.docker.internal:27017/"
#Mongo_String = "mongodb://mongo:27017/"


client=AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)

database=client.StoreDB
