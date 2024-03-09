def lambda_handler(event, context):
    result = 9

    return {
        "statusCode" : 200,
        "body" : "hi " + result
    }