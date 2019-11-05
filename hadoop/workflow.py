from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 4),
    'end_date': datetime(2020, 11, 4),
    'email': ['a@b.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('pricing', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='import_pricing_data',
    bash_command='sqoop job --exec myjob',
    retries=3,
    dag=dag)
