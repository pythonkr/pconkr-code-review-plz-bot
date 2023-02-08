import os

from src.slack_client import SlackClient
from src.github_client import GithubClient

if __name__ == "__main__":
    slack_client = SlackClient()
    github_client = GithubClient()

    slack_client.delete_all_previous_message(channel_id=os.getenv("WEB_SERVICE_TEAM_CH_ID"), bot_id=os.getenv("BOT_ID"))

    pull_request_infos = []
    pull_request_infos += github_client.get_pull_request_list("pythonkr", "pyconkr-api-v2")
    pull_request_infos += github_client.get_pull_request_list("pythonkr", "pyconkr-2023-frontend")
    pull_request_infos += github_client.get_pull_request_list("pythonkr", "pyconkr-web-archieve")
    pull_request_infos += github_client.get_pull_request_list("pythonkr", "pyconkr-middleware")

    if len(pull_request_infos) > 0:
        slack_client.send(pull_request_infos)

    print("finish")

