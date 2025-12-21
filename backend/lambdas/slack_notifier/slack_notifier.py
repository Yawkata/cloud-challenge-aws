import json
import boto3
import urllib.request

ssm = boto3.client('ssm')

def lambda_handler(event, context):
    parameter = ssm.get_parameter(
        Name='/cloud-resume/slack/webhook',
        WithDecryption=True
    )
    slack_webhook_url = parameter["Parameter"]["Value"]

    message = {
        "text": "ALERT!!! LMBDA IS NOT WORKING",
        "icon_emoji": ":rotating_light:"
    }

    payload = {"\"text\": \"ALERT!!! LMBDA IS NOT WORKING\", \"icon_emoji\": \":rotating_light:\""}

    req = urllib.request.Request(
        slack_webhook_url,
        data=json.dumps(message).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    urllib.request.urlopen(req)

    return {
        "statusCode": 200,
        "body": "Message was sent to Slack"
    }
