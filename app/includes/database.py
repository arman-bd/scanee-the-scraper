import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import HTTPException

async def connect_mongo():
    # Load the .env file
    load_dotenv()

    # get mongo username and password from .env file
    mongo_host = os.getenv("MONGODB_HOST")
    mongo_port = os.getenv("MONGODB_PORT")
    mongo_username = os.getenv("MONGODB_ROOT_USER")
    mongo_password = os.getenv("MONGODB_ROOT_PASS")

    # create mongo connection string
    mongo_connection_string = (
        "mongodb://"
        + mongo_username
        + ":"
        + mongo_password
        + "@"
        + mongo_host
        + ":"
        + mongo_port
        + "/"
        + "?authMechanism=DEFAULT"
    )

    try:
        conn = MongoClient(mongo_connection_string)
        # Database Connection
        return conn.database

    except Exception as e:
        print("> Error:", e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
