from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipe1.config.ConfigStore import *
from pipe1.functions import *
from prophecy.utils import *
from pipe1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src1 = src1(spark)
    df_age_transformation = age_transformation(spark, df_src1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("pipe1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipe1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipe1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
