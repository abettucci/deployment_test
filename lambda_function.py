from lib import lib1
import json

def lambda_handler(event, context):
    result = lib1.sum(5,4)

    return {
        "statusCode" : 200,
        "body" : "hi " + result
    }