from __future__ import annotations

import time

from airflow.utils import cli as cli_utils


@cli_utils.action_cli
def dag_processor2(args):
    while True:
        print("hello")
        time.sleep(10)
