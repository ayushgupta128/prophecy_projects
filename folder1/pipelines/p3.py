Config = {"table" : "'students'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    p3__student_records = Task(task_id = "p3__student_records", component = "Model", modelName = "p3__student_records")
    p3__dummytable_data = Task(task_id = "p3__dummytable_data", component = "Model", modelName = "p3__dummytable_data")
    run_pipeline_p1 = Task(
        task_id = "run_pipeline_p1", 
        component = "Pipeline", 
        maxTriggers = 10000, 
        triggerCondition = "Always", 
        enableMaxTriggers = False, 
        pipelineName = "p1", 
        parameters = {}
    )
