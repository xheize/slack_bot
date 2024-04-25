from server_modules.main import APIServer
from slack_modules.main import SlackBot
# from mq_modules.main import MQClient

import asyncio
import signal


class ServiceManager:
    def __init__(self):
        self.services = [SlackBot(), APIServer()]
        self.loop = asyncio.get_event_loop()
        for svc in self.services:
            if svc.status == "init":
                self.loop.create_task(svc.run())
            else:
                self.services.remove(svc)

    async def stop_services(self):
        for service in self.services:
            await service.stop()

    def shutdown(self, sig):
        print(f"Received exit signal {sig.name}...")
        self.loop.create_task(self.stop_services())

    def run(self):
        for signame in {'SIGINT', 'SIGTERM'}:
            self.loop.add_signal_handler(getattr(signal, signame), lambda: self.shutdown(getattr(signal, signame)))
        try:
            self.loop.run_forever()
        finally:
            self.loop.close()
            print("Successfully shutdown the service manager.")


if __name__ == "__main__":
    tmp = ServiceManager()
    tmp.run()
