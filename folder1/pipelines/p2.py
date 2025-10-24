Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    p2__Filter_0 = Task(task_id = "p2__Filter_0", component = "Model", modelName = "p2__Filter_0")
