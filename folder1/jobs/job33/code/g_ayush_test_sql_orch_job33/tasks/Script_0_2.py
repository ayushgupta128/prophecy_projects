from g_ayush_test_sql_orch_job33.utils import *

def Script_0_2():
    from airflow.operators.bash import BashOperator

    return BashOperator(task_id = "Script_0_2", bash_command = "print(\"qwe\")", )
