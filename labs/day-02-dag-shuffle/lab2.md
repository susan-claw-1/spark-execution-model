Day 2 Lab: DAGs and Shuffle

Goal: Understand how Spark builds a DAG, where shuffles occur, and how partitioning influences performance.

Lab steps:
- Create a large DataFrame (2M rows)
- Repartition to multiple partitions to trigger shuffle boundaries
- Perform a wide operation (groupBy count) to force a shuffle
- Observe Spark UI for stages and shuffle read/write
- Print a small result to confirm execution

Optional: explain(True) to view the plan

Expected outcomes:
- DAG with at least one Shuffle Exchange stage
- Visible partitions and shuffle statistics in UI
