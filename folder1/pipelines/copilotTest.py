Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    customer = Task(
        task_id = "customer", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {
          "name": "customer", 
          "sourceType": "Table", 
          "sourceName": "ayush_demos.demos", 
          "alias": "", 
          "additionalProperties": None
        }
    )
