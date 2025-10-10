Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    customer = Task(
        task_id = "customer", 
        component = "Dataset", 
        table = {"name" : "customer", "sourceType" : "Source", "sourceName" : "ayush_demos.demos", "alias" : ""}
    )
