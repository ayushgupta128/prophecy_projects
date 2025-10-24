Config = {"table" : "'students'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    empty_output = Task(
        task_id = "empty_output", 
        component = "Dataset", 
        table = {
          "name": "customer", 
          "sourceType": "Table", 
          "sourceName": "ayush_demos.demos", 
          "alias": "", 
          "additionalProperties": None
        }, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    list_databricks_files = Task(
        task_id = "list_databricks_files", 
        component = "Directory", 
        integration = "databricks", 
        path = "cewcew", 
        connector = Connection(kind = "databricks", id = "databricks_orchestrate"), 
        pattern = "cewc"
    )
    p3__Reformat_1 = Task(task_id = "p3__Reformat_1", component = "Model", modelName = "p3__Reformat_1")
    list_databricks_files.out0 >> empty_output.in0
    empty_output.out >> p3__Reformat_1.in_0
