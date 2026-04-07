#!/usr/bin/env python3
"""
Day 2 Local Run Lab: DAGs & Shuffle (two variants)

This is a runnable PySpark script you can execute locally (master = local[*]).
It demonstrates two scenarios:
- Without repartition: rely on Spark's default partitioning
- With repartition: force a shuffle boundary by repartitioning to N partitions

You can compare explain(True) outputs to see the explicit ShuffleExchange.
"""

import argparse
from pyspark.sql import SparkSession


def run(n: int = 200000, repartition: int | None = None):
    spark = SparkSession.builder.appName("lab2-local-run")\
        .master("local[*]")\
        .getOrCreate()

    df = spark.range(0, n).toDF("id")
    if repartition is not None:
        df = df.repartition(repartition)
        print(f"Repartitioned to {repartition} partitions")
    else:
        print("Using default partitioning (no explicit repartition)")

    agg = df.groupby().count()
    agg.show(5)
    agg.explain(True)

    spark.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=200000, help="number of rows in the generated range")
    parser.add_argument("--repartition", type=int, default=None, help="force number of partitions (None to skip)")
    args = parser.parse_args()
    run(n=args.n, repartition=args.repartition)
