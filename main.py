from src.slack_client import SlackClient
from src.github_client import GithubClient

if __name__ == "__main__":
    github_client = GithubClient()
    pull_request_infos = github_client.get_pull_request_list("pythonkr", "pyconkr-api-v2")

    slack_client = SlackClient()
    slack_client.send(pull_request_infos)
