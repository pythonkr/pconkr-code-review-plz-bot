import os
import requests


class GithubClient:
    def __init__(self):
        self.github_token = os.getenv("GH_TOKEN")

    def get_pull_request_list(self, owner: str, repo: str):
        response = requests.get(
            url="https://api.github.com/repos/{OWNER}/{REPO}/pulls".format(OWNER=owner, REPO=repo),
            headers=self._get_header(),
        ).json()

        return [self._parse_response(repo, pr) for pr in response]

    def _get_header(self):
        return {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer {token}".format(token=self.github_token),
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def _parse_response(self, repo_name: str, response_json: dict) -> dict:
        return {
                "repo_name": repo_name,
                "title": response_json.get("title"),
                "url": response_json.get("html_url")
        }
