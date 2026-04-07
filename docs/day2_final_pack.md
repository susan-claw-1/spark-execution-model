# Day 2 Final Pack — DAGs, Shuffle, and Stage Boundaries

This is the consolidated Day 2 reference you can run through offline to cement what you’ve learned about DAGs, shuffle, and how stages relate to data movement.

Overview
- Day 2 focuses on DAG construction, shuffle boundaries, and how partitioning affects performance.
- Central pattern: read data, apply a wide transformation (shuffle), then aggregate reads from the shuffle and finish the computation.

The two-stage (typical) pattern
- Stage 1: Read data, perform narrow transforms, and write shuffle data (shuffle write).
- Stage 2: Read the shuffle data (shuffle read) and perform the final aggregation or downstream work.

First stage: data access, pruning, and chunking
- What a first-stage scan entails:
  - Discovering files/partitions and applying partition pruning if available.
  - Column pruning (project only needed columns).
  - Predicate pushdown to filter data during read when supported by the source (Parquet/ORC/Delta excel here).
  - Splits/partitions: the input is broken into splits, each processed by a Spark task. The number of splits determines initial parallelism.
- How filtering helps:
  - Filters reduce the data volume early (parquet stats, partition pruning, predicate pushdown).
  - Fewer bytes moved to later stages means less I/O and faster completion.

Stage boundaries and shuffles
- When a stage boundary occurs:
  - Stage 1 writes shuffled data to intermediate storage (memory/disk).
  - Stage 2 starts only after the Stage 1 shuffle data is available for the downstream tasks to read.
- Overlap reality (in UI):
  - The UI can show Stage 1 progressing while Stage 2 begins to fetch ready shuffle blocks that have already been written. In practice, the boundary is strict: Stage 2 cannot start until its required Shuffle data for all tasks exists. However, as data is produced, Stage 2 can begin consuming the data that is available.

Explain(True) and what you should look for
- Before repartition(8): Plan may show a HashAggregate with or without an Exchange, depending on how Spark decides to partition data for the aggregation.
- After repartition(8): You’ll see an explicit Shuffle/Exchange node introduced by the call to repartition, indicating Stage 1 will write data into 8 partitions before Stage 2 reads it.
- In the UI: look for Shuffle Write metrics in Stage 1 and Shuffle Read metrics in Stage 2; a clear shuffle boundary line between stages.

Skew, AQE, and pruning
- Data skew: Highly skewed keys can cause some tasks to run long; AQE can coalesce partitions or repartition adaptively and some strategies (salting) may help extreme cases.
- AQE: Adaptive Query Execution can adjust the plan at runtime, including partition coalescing and repartitioning decisions, to better handle real data distributions.
- Partition pruning (partition pruning) and predicate pushdown (downstream read): these are crucial levers to reduce data moved in Stage 1.

Practical labs you can run offline (or locally with PySpark)
- Lab recap (Day 2):
  - Lab 2a: Explain output comparison (Plan A vs Plan B) – see lab2a_explain_comparison.py
  - Lab 2b: Parquet pruning scenario – see lab2_parquet_pruning.py
  - Lab 2c: Local run prototype – see lab2_local_run.py
- Offline split simulation (optional): offline_split_sim.py to visualize the idea of splits given file sizes and max partition size.

Mermaid diagram (Day 2, two-stage pattern)
```mermaid
graph TD
  A[Input Data] --> B[Stage 1: Scan + Narrow Transforms]
  B --> C[ShuffleWrite: repartition(8)]
  C --> D[Stage 2: Shuffle Read & Aggregation]
  D --> E[Output]
```

Quick reference (cheat sheet)
- Stage boundary: a ShuffleExchange/Exchange marks boundaries between Stage N and Stage N+1.
- ShuffleWrite: data written by Stage N to support Stage N+1's shuffle read.
- ShuffleRead: Stage N+1 reads the relevant shuffle blocks from Stage N.
- Explain(True): reveals the plan levels (Parsed/Analyzed/Optimized/Physical).
- AQE: runtime adaptivity for partition coalescing, repartitioning, and dynamic plan tweaks.
- Data pruning: partition pruning and predicate pushdown reduce the amount of data read in Stage 1.

What to run next (offline steps you can do at any time)
- Compare Plan A vs Plan B with lab2a_explain_comparison.py to see the explicit shuffle introduced by repartition.
- Run lab2_local_run.py to compare a non-repartition vs repartition run locally.
- Use lab2_parquet_pruning.py to see how pushing predicates and partition pruning reduces read volume.
- Use offline_split_sim.py to practice estimating splits for a given file layout.

Would you like me to also generate a printable Day 2 cheat card (PDF/PNG) from this pack, or export the Mermaid diagram as PNG/SVG for embedding in your notes?