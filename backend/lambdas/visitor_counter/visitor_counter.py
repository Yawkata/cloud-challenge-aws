import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):

    response = table.get_item(Key={'id': 'visitor_count'})

    response = table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression="SET #c = #c + :inc",
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':inc': 1},
        ReturnValues="UPDATED_NEW"
    )

    new_count = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'visitor_count': new_count})
    }