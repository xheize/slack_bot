import os
import json

from slack_sdk import WebClient
from slack_sdk import errors


class SlackBot:
    def __init__(self, config_path="./config.json"):
        self.bot: WebClient = self.init_slack(config_path)

    def get_status(self):
        tmp = self.bot.bots_info()

    def init_slack(self, config_path):
        token = self.get_slack_app_token(config_path=config_path)
        try:
            app = WebClient(token)
            return app
        except errors.SlackClientConfigurationError:
            ConnectionError("Cannot connect SLACK Server check token Value")

    def send_static_msg(self, channel_id: str, msg_string: str, threading: str = "", reply_broadcast: bool = False):
        if threading == "":
            self.bot.chat_postMessage(
                channel=channel_id,
                text=msg_string
            )
        else:
            self.bot.chat_postMessage(
                channel=channel_id,
                text=msg_string,
                thread_ts=threading,
                reply_broadcast=reply_broadcast
            )

    def send_interactive_msg(self, channel_id: str, msg_block: dict, alert_msg: str = "Something happened"):
        self.bot.chat_postMessage(
            channel=channel_id,
            text=alert_msg,
            attachments=msg_block,
        )

    # def send_ephemeral_msg(self, ):

    @staticmethod
    def get_slack_app_token(config_path="./config.json"):
        token = os.environ.get("SLACK_APP_TOKEN")
        if token is None:
            try:
                with open(config_path, "r") as json_data:
                    data = json.loads(json_data.read())
                    token = data['SLACK_APP_TOKEN']
                    return token
            except FileExistsError:
                ValueError("Cannot Find SLACK APP TOKEN\nAdd environ SLACK_APP_TOKEN or write config.json File.")
        return token
