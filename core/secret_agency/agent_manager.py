import asyncio
import threading
from time import sleep
from core.secret_agency.agent_discord import MyDiscordAgent
from core.secret_agency.temp import users_under_control


class Agency(object):
    def __init__(self):
        self.clients = []
        self.clients_loop = []
        self.clients_thread = []

    @staticmethod
    async def _start_agent_actions(client, token):
        await client.start(token, bot=False)

    @staticmethod
    def _run_it_forever(loop):
        loop.run_forever()

    def _log_agents(self, tokens):
        asyncio.get_child_watcher()
        i = 0
        for el in tokens:
            self.clients.append(MyDiscordAgent(users_under_control, log_en=True, human=False))
            self.clients_loop.append(asyncio.get_event_loop())
            self.clients_loop[i].create_task(self._start_agent_actions(self.clients[i], el))
            self.clients_thread.append(threading.Thread(target=self._run_it_forever, args=(self.clients_loop[i],)))
            self.clients_thread[i].start()
            i += 1
            sleep(0.2)

    def run(self, tokens_list):
        self._log_agents(tokens_list)
