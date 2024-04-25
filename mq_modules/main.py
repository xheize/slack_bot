import os
import pika
from slack_modules.slack_client import SlackBot

class MQClient:
    _instance = None
    _is_initalize = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MQClient, cls).__new__(cls)
        return cls._instance
    
    
    def __init__(self) -> None:
        self.status = "init"
        self.connection = self.init_config()
        self.channel = self.connection.channel()
        self.status = "running"

    def __del__(self) -> None:
        self.connection.close()

    def init_pika_connection(self):
        try:
            config = None
            if os.environ.get("MQ_HOST"):
                config = pika.ConnectionParameters(
                    host=os.environ.get("MQ_HOST"),
                    connection_attempts=5,
                    retry_delay=1
                )
                return pika.BlockingConnection(config)
            else:
                return pika.BlockingConnection()
        except:
            self.status = "stop"
            self.connection = None

    def start_consuming(self):
        try:
            if self.channel:
                self.channel.basic_consume('slackMQ', self.callback_msg())
                self.channel.start_consume()
            else:
                print("Not")
        # # Don't recover if connection was closed by broker
        # except pika.exceptions.ConnectionClosedByBroker:
        #     break
        # Don't recover on channel errors
        except pika.exceptions.AMQPChannelError as e :
            print(e)
        # Recover on all other connection errors
        except pika.exceptions.AMQPConnectionError as e:
            print(e)

    def callback_msg(self):
        SlackBot().send_message()
        
        

if __name__ == "__main__":
    print("It's MQ Main.py File\nStandAlone run not support\nplz Combine with fork or Process")