import json
import boto3
import hashlib

ssm = boto3.client('ssm')
dynamodb = boto3.resource('dynamodb')
counter_table = dynamodb.Table('VisitorCounterIAC')
ip_table = dynamodb.Table('VisitorIPsIAC')

parameter = ssm.get_parameter(
    Name='/cloud-resume/visitor-counter/ip-salt',
    WithDecryption=True
)
IP_SALT = parameter["Parameter"]["Value"]

def hash_ip(ip):
    return hashlib.sha256(f"{IP_SALT}{ip}".encode()).hexdigest()

def lambda_handler(event, context):
    visitor_ip = event['requestContext']['identity']['sourceIp']
    hashed_visitor_ip = hash_ip(visitor_ip)

    ip_table_response = ip_table.get_item(Key={'ip': hashed_visitor_ip})

    if 'Item' not in ip_table_response:
        ip_table.put_item(Item={'ip': hashed_visitor_ip})

        counter_table_response = counter_table.update_item(
            Key={'id': 'visitor_count'},
            ExpressionAttributeNames={'#c': 'count'},
            ExpressionAttributeValues={':inc': 1},
            UpdateExpression="SET #c = #c + :inc",
            ReturnValues="UPDATED_NEW"
        )

        new_count = int(counter_table_response['Attributes']['count'])
    else:
        counter_table_response = counter_table.get_item(Key={'id': 'visitor_count'})
        new_count = int(counter_table_response['Item']['count'])
        
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'visitor_count': new_count})
    }