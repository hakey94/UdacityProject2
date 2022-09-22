import logging
import os
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://hakey94:bGnwh6CpMBvGZ6nB5fb8BXfY6FCkD22Dusum0fG4mRAOE3tLAimOhK72bMTVk3L6f9GTC0yYRbR0Rx600SVGlQ==@hakey94.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&maxIdleTimeMS=120000&appName=@hakey94@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['hakeydb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)