from lib1 import sum
import json

def lambda_handler(event, context):
    result = sum(5,4)

    return {
        "statusCode" : 200,
        "body" : "hi " + str(result)
    }