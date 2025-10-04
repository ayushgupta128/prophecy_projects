from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *

def project_future_ages(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        (col("age").cast(IntegerType()) + lit(10)).alias("age_after_10_years"), 
        (col("age").cast(IntegerType()) + lit(20)).alias("age_after_20_years")
    )
