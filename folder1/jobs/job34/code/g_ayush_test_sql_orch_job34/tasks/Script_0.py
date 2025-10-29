from g_ayush_test_sql_orch_job34.utils import *

def Script_0():
    from airflow.operators.bash import BashOperator

    return BashOperator(task_id = "Script_0", bash_command = "print(\"abc\")", )
