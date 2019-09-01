import requests
import json

slack_web_hook = 'https://hooks.slack.com/services/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'


def send_slack(event, context):
    print(str(event))
    slack_message = {'text': 'EC2 Instance Stopped'}
    resp = requests.post(slack_web_hook, data=json.dumps(slack_message))
    return resp.text
