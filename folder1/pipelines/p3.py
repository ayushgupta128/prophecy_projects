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
    p3__undefined_format_no_fields = Task(
        task_id = "p3__undefined_format_no_fields", 
        component = "Model", 
        modelName = "p3__undefined_format_no_fields"
    )
    p3__Reformat_1 = Task(task_id = "p3__Reformat_1", component = "Model", modelName = "p3__Reformat_1")
    read_parquet_file = Task(
        task_id = "read_parquet_file", 
        component = "Script", 
        ports = None, 
        scriptMethodHeader = "def Script(spark: SparkSession) -> DataFrame:", 
        scriptMethodFooter = "return out0", 
        script = "# out0 = spark.read.parquet('/Volumes/ayush_demos/demos/prophecy_orchestrator_volume/parts/part-00000-f11c21ce-30d0-4490-8074-b8f74bc4e1ee-c000.snappy.parquet')

#out0 = spark.sql(\"select * from ayush_demos.demos.boletin_ssf_santander_situacion\")
out0 = spark.sql(\"select * from ayush_demos.demos.debug_panic_table\")"
    )
    list_databricks_files = Task(
        task_id = "list_databricks_files", 
        component = "Directory", 
        integration = "databricks", 
        path = "cewcew", 
        connector = Connection(kind = "databricks", id = "databricks_orchestrate"), 
        pattern = "cewc"
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        isNew = True, 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          header = True
        )
    )
    list_databricks_files.out0 >> empty_output.in0
    empty_output.out >> p3__Reformat_1.in_0
