import asyncio
from core.src.internal_log import Log


class PeriodicHandler(object):

    @staticmethod
    async def _periodic_action(periodic_function, loop_time, log_message):
        while True:
            periodic_function()
            Log.console_simple_action_log(log_message)
            await asyncio.sleep(loop_time)  # time in seconds to send the command

    def start_periodic_event(self, periodic_function, loop_time, log_message=None):
        try:
            loop = asyncio.get_event_loop()
            task = loop.create_task(self._periodic_action(periodic_function, loop_time, log_message))
            loop.run_until_complete(task)
        except asyncio.CancelledError:
            pass
