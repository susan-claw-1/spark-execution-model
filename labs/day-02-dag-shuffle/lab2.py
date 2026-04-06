from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("lab2-dag-shuffle").getOrCreate()

# Large DataFrame to exercise shuffle
df = spark.range(0, 2_000_000).toDF("id")

# Force a shuffle by repartitioning
df_repart = df.repartition(8)

# A wide operation that triggers a shuffle
agg = df_repart.groupBy().count()

# Trigger execution and show a tiny sample
agg.show(5)

spark.stop()
