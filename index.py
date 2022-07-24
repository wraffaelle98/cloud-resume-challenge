import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    dynamodb.update_item(
        TableName="visitors",
        Key={ "counter": { 'N': "0" } },
        ExpressionAttributeValues={ ":inc": {'N': "1"} },
        UpdateExpression="ADD visitor :inc"
    )
    response = dynamodb.get_item(TableName='visitors', Key={'counter':{'N': "0"}})
    n = response['Item']['visitor']['N']
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps(n)
    }