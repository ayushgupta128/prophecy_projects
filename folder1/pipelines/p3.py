Config = {"table" : "'students'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    run_pipeline_p1 = Task(
        task_id = "run_pipeline_p1", 
        component = "Pipeline", 
        maxTriggers = 10000, 
        triggerCondition = "Always", 
        enableMaxTriggers = False, 
        pipelineName = "p1", 
        parameters = {}
    )
