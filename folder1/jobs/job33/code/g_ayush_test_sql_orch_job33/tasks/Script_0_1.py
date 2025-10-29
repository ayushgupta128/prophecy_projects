from g_ayush_test_sql_orch_job33.utils import *

def Script_0_1():
    from airflow.operators.bash import BashOperator

    return BashOperator(task_id = "Script_0_1", bash_command = "print(\"qwe\")", )
