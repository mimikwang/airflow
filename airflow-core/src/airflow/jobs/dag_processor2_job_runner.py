from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

from airflow._shared.observability.metrics import stats
from airflow.jobs.base_job_runner import BaseJobRunner
from airflow.jobs.job import Job, perform_heartbeat
from airflow.utils.log.logging_mixin import LoggingMixin

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from airflow.dag_processing2.manager import DagProcessorManager


class DagProcessor2JobRunner(BaseJobRunner, LoggingMixin):
    """Job runner that runs the dag processor2 process."""

    job_type = "DagProcessor2Job"

    def __init__(self, job: Job, processor: DagProcessorManager):
        super().__init__(job)
        self.processor = processor
        self.processor.set_heartbeat(
            lambda: perform_heartbeat(
                job=self.job, heartbeat_callback=self.heartbeat_callback, only_if_necessary=True
            )
        )

    def _execute(self) -> int | None:
        self.log.info("Starting the Dag Processor2 Job")
        try:
            asyncio.run(self.processor.run())
        except Exception:
            self.log.exception("Exception when executing DagProcessor2Job")
            raise

        return None

    def heartbeat_callback(self, session: Session | None = None):
        stats.incr("dag_processor2_heartbeat", 1, 1)
