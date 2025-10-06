from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipe1.config.ConfigStore import *
from pipe1.functions import *

def age_transformation(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("name"), 
        col("id"), 
        col("age"), 
        (col("age").cast(IntegerType()) + lit(100)).alias("age_100"), 
        (col("age").cast(IntegerType()) + lit(101)).alias("age_101")
    )
