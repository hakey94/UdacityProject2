import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://hakey94:bGnwh6CpMBvGZ6nB5fb8BXfY6FCkD22Dusum0fG4mRAOE3tLAimOhK72bMTVk3L6f9GTC0yYRbR0Rx600SVGlQ==@hakey94.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&maxIdleTimeMS=120000&appName=@hakey94@" # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['hakeydb']
            collection = database['posts']

            query = {'_id': str(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)