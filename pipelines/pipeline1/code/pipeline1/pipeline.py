from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *
from prophecy.utils import *
from pipeline1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src1 = src1(spark)
    df_project_future_ages = project_future_ages(spark, df_src1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("pipeline1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
