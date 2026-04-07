from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Lab: Parquet read with partition pruning / predicate pushdown
# This lab demonstrates reading a partitioned Parquet dataset and filtering on partitioned columns

spark = SparkSession.builder.appName("lab2-parquet-pruning").getOrCreate()

# Step 1: Create a small partitioned Parquet dataset in memory-backed path
# We'll generate synthetic data, annotate with year/month/day for partitioning, and write
N = 20000
base = spark.range(0, N).toDF("id")
import pyspark.sql.functions as SF
from pyspark.sql.functions import col, lit

data = base.withColumn("year", lit(2026)) \
           .withColumn("month", SF.expr("(id % 12) + 1")) \
           .withColumn("day", SF.expr("(id % 28) + 1"))

path = "/tmp/lab2_parquet_pruning"
# Remove existing data if present
try:
    import shutil, os
    if os.path.exists(path):
        import shutil
        shutil.rmtree(path)
except Exception:
    pass

data.write.partitionBy("year", "month", "day").mode("overwrite").parquet(path)

print("Wrote partitioned Parquet to", path)

# Step 2: Read back with a filter on a partition column to trigger pruning
read = spark.read.parquet(path)
filtered = read.filter((col("year") == 2026) & (col("month") == 1))
print("Partitions after pruning:", filtered.rdd.getNumPartitions())

# Step 3: Show a small result and print explain plan
filtered.show(5)
filtered.explain(True)

spark.stop()
