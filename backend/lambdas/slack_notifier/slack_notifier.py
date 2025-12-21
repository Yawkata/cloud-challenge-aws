import json
import boto3
import urllib.request
from datetime import datetime

ssm = boto3.client('ssm')

def lambda_handler(event, context):
    parameter = ssm.get_parameter(
        Name='/cloud-resume/slack/webhook',
        WithDecryption=True
    )
    slack_webhook_url = parameter["Parameter"]["Value"]

    sns_message_str = event["Records"][0]["Sns"]["Message"]
    sns_message = json.loads(sns_message_str)
    alarm_name = sns_message.get("AlarmName")
    alarm_state = sns_message.get("NewStateValue")
    alarm_reason = sns_message.get("NewStateReason")
    alarm_timestamp = sns_message.get("StateChangeTime")
    dt = datetime.strptime(alarm_timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")
    formatted_time = dt.strftime("%Y-%m-%d %I:%M:%S %p %Z")

    message = {
        "text": (
            f"*CloudWatch Alarm Triggered*\n"
            f"*Alarm*: {alarm_name}\n"
            f"*State*: {alarm_state}\n"
            f"*Reason*: {alarm_reason}\n"
            f"*Time*: {formatted_time}"
        ),
        "icon_emoji": ":rotating_light:"
    }

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
