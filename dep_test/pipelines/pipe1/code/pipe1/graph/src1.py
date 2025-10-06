from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipe1.config.ConfigStore import *
from pipe1.functions import *

def src1(spark: SparkSession) -> DataFrame:
    schemaFields = StructType([
        StructField("name", StringType(), True), StructField("id", StringType(), True), StructField("age", StringType(), True)
    ])\
        .fields
    readSchema = StructType([StructField(f.name, StringType(), True) for f in schemaFields])

    return spark.createDataFrame([Row("ram", "1", "10"), Row("shyam", "2", "20"), Row("raghav", "3", "30")], readSchema)
