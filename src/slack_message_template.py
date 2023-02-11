class SlackTemplate:
    def __init__(self, type: str):
        types = ["code_review", ]

        if type not in types:
            raise NotImplementedError("Invalid Type")

        if type == "code_review":
            self.block = self._init_title_section(
                "Code Review Please",
                "코드리뷰 할 대상이 있습니다.",
                "https://raw.githubusercontent.com/pythonkr/pconkr-code-review-plz-bot/master/static/image_100x100.jpg"
            )

    def get_block(self):
        return self.block

    def _init_title_section(self, title: str, sub_title: str, image_url: str) -> list:
        return [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": title,
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": sub_title
                },
                "accessory": {
                    "type": "image",
                    "image_url": image_url,
                    "alt_text": "대표 이미지"
                }
            }
        ]

    def get_attachment(self, infos: list):
        """블럭 포매터
        """
        attachment_block = []

        for elem in infos:
            attachment_block.extend(self._code_review_section(elem.get("repo_name"), elem.get("title"), elem.get("url")))
            # attachment_block.append({"type": "divider"})

        return [
            {
                "blocks": attachment_block
            }
        ]

    def _code_review_section(self, repo_name: str, pr_title: str, pr_url: str):
        return [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*{repo_name}*".format(repo_name=repo_name)
                },
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*{title}*".format(title=pr_title)
                    }
                ],
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "보기",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "url": pr_url,
                    "action_id": "button-action"
                }
            },
            {
                "type": "divider"
            }
        ]
