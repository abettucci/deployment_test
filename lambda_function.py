from lib1 import sum
# import json

def lambda_handler(event, context):
    # result = sum(5,4)
    result = 9

    return {
        "statusCode" : 200,
        "body" : "hi " + result
    }