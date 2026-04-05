from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("lab1").getOrCreate()
df = spark.range(10).toDF("n"); df.show()
print("Partitions:", df.rdd.getNumPartitions())
spark.stop()
