from lib1 import sum
import json

def lambda_handler(event, context):
    try:
        result = sum(5,4)

        return {
            "statusCode" : 200,
            "body" : "hi " + result
        }

    except Exception as e:
        print(e)