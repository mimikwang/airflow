from __future__ import annotations

import asyncio

from airflow.utils.log.logging_mixin import LoggingMixin


class DagProcessorManager(LoggingMixin):
    """Manage process for parsing DAGS."""

    def __init__(self):
        self.heartbeat: callable[[], None] = lambda: None

    def set_heartbeat(self, heartbeat: callable[[], None]):
        self.heartbeat = heartbeat

    async def run(self):
        while True:
            self.log.info("Looping")
            self.heartbeat()
            await asyncio.sleep(10)
