from lib1 import sum
import json

def lambda_handler(event, context):
    print('hola')
    try:
        result = sum(5,4)
        print('hola')
        return {
            "statusCode" : 200,
            "body" : "hi " + result
        }

    except Exception as e:
        print(e)