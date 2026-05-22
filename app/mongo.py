from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from consts import MONGO_URI

client: AsyncIOMotorClient | None = None


async def get_database():
    global client

    if client is None:
        client = AsyncIOMotorClient(MONGO_URI)

    return client["my_database"]


async def insert_one(collection, data: dict):
    result = await collection.insert_one(data)
    return str(result.inserted_id)


async def find_one(collection, filters: dict):
    document = await collection.find_one(filters)

    if document:
        document["_id"] = str(document["_id"])

    return document


async def find_many(collection, filters: dict = None):
    filters = filters or {}

    documents = []

    async for document in collection.find(filters):
        document["_id"] = str(document["_id"])
        documents.append(document)

    return documents


async def update_one(collection, filters: dict, data: dict):
    result = await collection.update_one(filters, {"$set": data})

    return result.modified_count


async def delete_one(collection, filters: dict):
    result = await collection.delete_one(filters)
    return result.deleted_count


async def find_by_id(collection, id: str):
    document = await collection.find_one({"_id": ObjectId(id)})

    if document:
        document["_id"] = str(document["_id"])

    return document
