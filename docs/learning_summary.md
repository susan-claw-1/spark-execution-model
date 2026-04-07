# Spark Day 1-3 Learning Summary (offline reference)

This document distills core concepts from Days 1–3, focusing on how Spark reads data, builds the DAG, and executes across stages.

1) Core concepts
- Leaf scan / Data source read: The initial read from storage into Spark's internal row format. Includes predicate pushdown, column pruning, and partition pruning when possible.
- Partitions / Splits: Data is divided into partitions (splits). Each partition is processed by a Spark task; the number of splits affects initial parallelism.
- Stages: Groups of tasks bounded by shuffle boundaries. Stages run serially across shuffle boundaries: Stage 2 starts only after Stage 1 shuffle data is produced and ready for reading.
- Shuffles: Data movement between stages caused by wide transformations (groupBy, join, repartition). Stage N writes shuffle data; Stage N+1 reads it.
- Narrow vs wide transformations: Narrow (map, filter) do not cause shuffles within a stage; wide transformations trigger shuffles at stage boundaries.
- Explain(True): See the full plan (parsed, analyzed, optimized, physical) including ShuffleExchange boundaries.
- AQE (Adaptive Query Execution): runtime optimizations like coalescing partitions and adjusting shuffle strategies. Helps with skew and dynamic data.
- Data skew: When some keys are heavily skewed, causing uneven work; mitigations include AQE, salting, and partitioning strategies.

2) Importance of the first stage
- Early filtering (partition pruning, predicate pushdown, column pruning) drastically reduces the data read and processed in Stage 1.
- The smaller Stage 1 footprint, the less pressure on memory and the smaller the amount of data shuffled later.

3) A simple 3-stage pipeline example
- Order: Read Data -> Filter -> Repartition -> Aggregate -> Write
- Stage 1: Read + Filter + Column Pruning (produces initial partitions)
- Stage 2: Repartition (shuffle write into N partitions) and optional early aggregation
- Stage 3: Shuffle Read and Final Aggregation -> Write

4) Practical knobs and tips
- spark.sql.files.maxPartitionBytes: controls the maximum size of a partition read; smaller values create more splits (more parallelism), larger values reduce split count.
- spark.default.parallelism: default parallelism for RDD operations; affects initial task counts.
- spark.sql.shuffle.partitions: number of partitions created for shuffle ops; more partitions means more parallelism in downstream stages.
- AQE: enables dynamic re-planning during execution (e.g., coalescing, repartitioning) to adapt to runtime stats.
- Data layout: ensure Parquet/ORC row groups are sized well for efficient reading (to improve partition pruning and pushdown).

5) Quick references
- Stage boundary: the place where a ShuffleExchange/Exchange appears in the plan.
- ShuffleRead/ShuffleWrite metrics: used to diagnose shuffle costs in Spark UI.
- Explain(True): helps you preview what Spark will actually do across stages.

If you’d like, I can also add Day 1–3-focused cheats to this file (one-page printable version) and link to Mermaid diagrams for quick visual references.