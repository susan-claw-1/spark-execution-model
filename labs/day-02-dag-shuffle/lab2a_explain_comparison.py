"""
Lab 2a: Explain output comparison — before vs after repartition

Goal: See how repartition changes the physical plan by introducing
a ShuffleExchange / Exchange node.

Run each cell separately in a Databricks notebook or local PySpark shell.
"""
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("lab2a-explain-comparison").getOrCreate()

# --- Step 1: Create a DataFrame ---
df = spark.range(0, 2_000_000).toDF("id")

# --- Step 2: Explain WITHOUT repartition ---
# You should see a simple plan: Range -> HashAggregate
# No explicit Exchange/ShuffleExchange from your code
print("=" * 60)
print("PLAN A: groupBy().count() WITHOUT repartition")
print("=" * 60)
df.groupBy().count().explain(True)

# --- Step 3: Explain WITH repartition(8) ---
# You should now see an Exchange node (RoundRobinPartitioning or HashPartitioning)
# injected between the Range scan and the HashAggregate
print("\n" + "=" * 60)
print("PLAN B: groupBy().count() WITH repartition(8)")
print("=" * 60)
df.repartition(8).groupBy().count().explain(True)

# --- Step 4: Compare ---
# Key things to look for in the output:
# - Plan A: likely has an Exchange for the aggregation shuffle, but no
#   explicit repartition operator from your code.
# - Plan B: has an additional Exchange (RoundRobinPartitioning, 8) that
#   YOU forced with .repartition(8). This means an extra shuffle stage.
#
# Questions to answer:
# - How many Exchange nodes appear in Plan A vs Plan B?
# - What partitioning scheme does each Exchange use?
# - Which plan would be more expensive and why?

spark.stop()
