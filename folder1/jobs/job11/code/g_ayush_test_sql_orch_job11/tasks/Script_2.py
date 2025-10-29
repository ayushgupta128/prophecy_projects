from g_ayush_test_sql_orch_job11.utils import *

def Script_2():
    from airflow.operators.bash import BashOperator

    return BashOperator(task_id = "Script_2", bash_command = "print(\"def\")", )
