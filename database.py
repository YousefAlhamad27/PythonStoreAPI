from motor.motor_asyncio import AsyncIOMotorClient



#Mongo_String="mongodb://localhost:27017/"
#Mongo_String="mongodb://host.docker.internal:27017/"
Mongo_String = "mongodb://mongo:27017/"


client=AsyncIOMotorClient(Mongo_String)

database=client.StoreDB
