import os

import slack_sdk

import src.slack_message_template as templates


class SlackClient:
    def __init__(self):
        self.client = slack_sdk.WebClient(token=os.getenv("SLACK_TOKEN"))

    def send(self, message_templates: list) -> None:
        template = templates.SlackTemplate("code_review")
        self.client.chat_postMessage(channel="bot-test", blocks=template._code_review(message_templates))
