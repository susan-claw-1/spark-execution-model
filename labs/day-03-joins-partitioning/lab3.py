#!/usr/bin/env python3
"""
Day 3 Lab: Joins and Partitioning (partial runnable scaffold)

This is a starting point for a Day 3 lab to explore join strategies.
The script is intentionally simple and configurable via environment variables.
"""
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

# Config knobs (override via env):
BIG_N = int(os.getenv("BIG_N", "200000"))
SMALL_N = int(os.getenv("SMALL_N", "1000"))
USE_BROADCAST = os.getenv("USE_BROADCAST", "false").lower() in ("1", "true", "yes")

spark = SparkSession.builder.appName("lab3-joins-partitioning").getOrCreate()

# Create data
big_df = spark.range(0, BIG_N).withColumn("key", ("id" % SMALL_N).cast("int"))
small_df = spark.range(0, SMALL_N).withColumn("key", ("id" % SMALL_N).cast("int"))

# Simple inner join on key
print("=== Plan: INNER JOIN (no broadcast) ===")
(j1 := big_df.join(small_df, on="key", how="inner")).explain(True)
print("Result rows:", j1.count())

if USE_BROADCAST:
    print("=== Plan: INNER JOIN with BROADCAST ===")
    j2 = big_df.join(broadcast(small_df), on="key", how="inner")
    j2.explain(True)
    print("Result rows (broadcast):", j2.count())
else:
    print("Broadcast not enabled via env USE_BROADCAST.")

spark.stop()
