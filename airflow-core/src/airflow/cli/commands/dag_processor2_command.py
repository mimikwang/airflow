from __future__ import annotations

from airflow.dag_processing2.manager import DagProcessorManager
from airflow.jobs.dag_processor2_job_runner import DagProcessor2JobRunner
from airflow.jobs.job import Job, run_job
from airflow.utils import cli as cli_utils


@cli_utils.action_cli
def dag_processor2(args):
    job = DagProcessor2JobRunner(processor=DagProcessorManager(), job=Job())
    run_job(job=job.job, execute_callable=job._execute)
