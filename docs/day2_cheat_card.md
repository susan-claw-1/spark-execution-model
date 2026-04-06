# Day 2 Cheat Card – DAGs & Shuffle (offline reference)

Core idea: Spark builds a DAG, shuffles data between stages, and partitioning affects parallelism and performance.

Key concepts
- DAG/Stages/Tasks: Stage boundaries align with shuffle boundaries; tasks run in parallel within a stage.
- Shuffle: Data movement across partitions/executors caused by wide transformations (groupBy, repartition, joins).
- Narrow vs Wide dependencies: Narrow (map/filter) avoid shuffles; Wide typically trigger shuffles.
- Partitioning: Repartition/Coalesce controls number of partitions and shuffle behavior.
- Explain(True): shows logical → optimized plans → physical plan; includes ShuffleExchange when a shuffle is planned.
- Spark UI: observe jobs/stages, shuffle metrics, and storage; use explain() as a quick check.
- AQE: Adaptive query execution, can coalesce partitions and adjust shuffle behavior at runtime; may help with skew.

Common scenario: groupBy with repartition
- df.repartition(8).groupBy().count() will typically produce two stages:
  - Stage 1: shuffle write into 8 partitions (via Exchange/ShuffleWriter)
  - Stage 2: shuffle read and final aggregation

Tips for diagnosing skew and tuning
- If one partition is very large, consider: AQE repartition lookups, adjust spark.sql.shuffle.partitions, or apply salting for extreme skew.
- Look for large Shuffle Read bytes and many spills in the UI to identify bottlenecks.

Illustrative diagram (Mermaid)
```
graph TD
  A[Input] --> B[Partitioned DataFrame]
  B --> C[Wide Transform (shuffle/write)]
  C --> D[Shuffle Boundary]
  D --> E[Shuffle Read on next stage]
  E --> F[Aggregation]
  F --> G[Output]
```

Printable reference: Day 2 cheat card is intended for quick study offline and to accompany Day 2 lab notes.
"} }```)  فرمایا to=functions.write  (json)  { 