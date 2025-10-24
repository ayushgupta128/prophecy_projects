Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    demographics_unknown_format = Task(
        task_id = "demographics_unknown_format", 
        component = "Dataset", 
        table = {"name" : "s1", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    p1__customer = Task(task_id = "p1__customer", component = "Model", modelName = "p1__customer")
    demographics_unknown_format.out >> p1__customer.in_0
