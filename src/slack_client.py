import os
import time

import slack_sdk

import src.slack_message_template as templates


class SlackClient:
    def __init__(self):
        self.client = slack_sdk.WebClient(token=os.getenv("SLACK_TOKEN"))

    def send(self, message_templates: list) -> None:
        template = templates.SlackTemplate("code_review")
        self.client.chat_postMessage(channel="6-홈페이지개발", blocks=template._code_review(message_templates))

    def delete_all_previous_message(self, channel_id: str, bot_id: str) -> None:
        delete_target = self.get_all_bot_message(channel_id, bot_id=bot_id)

        # for target in delete_target:    # 혹시 모르니 조회된 메시지 중 최근 1건만 삭제
        if len(delete_target) > 0:
            target = delete_target[0]
            response = self.client.chat_delete(channel=channel_id, ts=target.get("ts"))
            time.sleep(1)

    def get_all_bot_message(self, channel_id: str, bot_id: str) -> list:
        all_conversations_data = self.client.conversations_history(channel=channel_id).data["messages"]

        filtered = list(
            filter(
                lambda data: data.get("bot_id") == bot_id,
                all_conversations_data
            )
        )

        return filtered
