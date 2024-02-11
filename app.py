import json

def serverless(api):
    def function(event, context):
        body = api(event, context)
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response
    return function

@serverless
def lambda_handler(event, context):
    print("event:", event)
    data = json.loads(event['body'])
    return { "hello": data.get('name', 'world') }