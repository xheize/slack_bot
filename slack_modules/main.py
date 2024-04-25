from __future__ import annotations

import os
import asyncio

from slack_sdk import WebClient
from slack_sdk import errors
from slack_sdk.webhook import WebhookClient


class SlackBot:
    _instance = None
    _is_initalize = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SlackBot, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initalize:
            self.webhook_list: list | list[webhookClient] = []
            self.bot = None
            self.status = "init"

    async def run(self):
        try:
            token = os.environ.get("SLACK_APP_TOKEN")
            if not token:
                raise EnvironmentError("토큰값이 존재 하지 않습니다.")
            else:
                self.bot = WebClient(token)
            webhook_url_value = os.environ.get("SLACK_WEBHOOK_URL")
            webhook_name_value = os.environ.get("SLACK_WEBHOOK_NAME")
            if webhook_url_value:
                webhook_url_list = webhook_url_value.split(",")
            if webhook_name_value:
                webhook_name_list = webhook_name_value.split(",")
            for webhook_url, webhook_name in zip(webhook_url_list, webhook_name_list):
                instance = webhookClient(name=webhook_name, url=webhook_url)
                self.webhook_list.append(instance)
            return
        except errors.SlackClientConfigurationError:
            ConnectionError("Cannot connect SLACK Server\ncheck token Value")

    def get_status(self):
        bot_status = self.bot.bots_info()
        return bot_status

    def send_post_message(self, channel_id: str, text: str | None = "", msg_block: dict | None = None,
                          thread_ts: str = None, reply_broadcast: bool = False,
                          ):
        self.bot.chat_postMessage(
            channel=channel_id,
            text=text,
            attachments=msg_block,
            thread_ts=thread_ts,
            reply_broadcast=reply_broadcast
        )

    def send_webhook_message(self, webhook_name: str, msg: dict):
        for webhook_instance in self.webhook_list:
            if webhook_name == str(webhook_instance):
                _text = msg.get("text")
                _blocks = msg.get("blocks")
                webhook_instance.send_message(text=_text, blocks=_blocks)
                return True
        return False


class webhookClient:

    def __init__(self, name: str, url: str):
        if name and url:
            self.name = name
            self.hookClient = WebhookClient(url)
        else:
            raise ValueError("이름과 url 값을 입력하시오.")

    def __str__(self):
        return self.name

    def send_message(self, text: str | None = None, blocks: list | None = None):
        if text == "":
            text = None
        elif blocks is not None:
            if len(blocks) < 1:
                blocks = None
        response = self.hookClient.send(
            text=text,
            blocks=blocks
        )
        if response.status_code == 200 and response.body == "ok":
            return True
        else:
            print(response.status_code, response.body)
            return False
