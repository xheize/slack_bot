import multiprocessing
import os

from slack_modules.main import slack_instance
from server_modules.main import server


if __name__ == "__main__":
    proc_manager = []
    slack_proc = multiprocessing.Process(slack_instance.run, args=())
    proc_manager.append(slack_proc)
    if os.environ.get("MODE") == "CONSUMER":
        http_proc = multiprocessing.Process(server.run, args=())
        proc_manager.append(http_proc)


