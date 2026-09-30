from __future__ import annotations

import asyncio

from airflow.utils.log.logging_mixin import LoggingMixin


class DagProcessorManager(LoggingMixin):
    """Manage process for parsing DAGS."""

    def __init__(self):
        pass

    async def run(self):
        while True:
            self.log.info("Looping")
            await asyncio.sleep(10)
