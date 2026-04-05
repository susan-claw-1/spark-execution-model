from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("lab2").getOrCreate()
df = spark.range(0,1000).repartition(4)
res = df.filter("id 