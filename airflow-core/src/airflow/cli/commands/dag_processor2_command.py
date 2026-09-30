from __future__ import annotations

import asyncio

from airflow.dag_processing2.manager import DagProcessorManager
from airflow.utils import cli as cli_utils


async def _run():
    manager = DagProcessorManager()
    await manager.run()


@cli_utils.action_cli
def dag_processor2(args):
    asyncio.run(_run())
