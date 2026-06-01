from bson import ObjectId
from consts import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient
import random


client = AsyncIOMotorClient(MONGO_URI)
db = client["my_database"]


async def get_database():
    return db

async def insert_one(collection, data: dict):
    result = await collection.insert_one(data)
    return str(result.inserted_id)

async def find_random_product(collection, query: dict | None = None):
    query = query or {}

    document = await collection.aggregate([
        {"$match": query},
        {"$sample": {"size": 1}}
    ]).to_list(length=1)

    if not document:
        return None

    products = document[0].get("products", [])

    if not products:
        return None

    return random.choice(products)

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
