# Spark Execution Model — Learning Plan

A 2-week, chat-driven learning sprint for PySpark / Spark SQL on Databricks.

## Week 1 — Architecture, DAGs, and Data Movement

### Day 1: Core Architecture & Py4J Bridge
- [ ] Driver process and SparkSession
- [ ] Executors and task slots
- [ ] Cluster manager role (standalone, YARN, Databricks)
- [ ] How PySpark talks to the JVM via Py4J
- [ ] Lab: create a session, run spark.range(), inspect partitions

### Day 2: The DAG and Scheduling
- [ ] Logical plan → optimised logical plan → physical plan
- [ ] DAGScheduler: stages and shuffle boundaries
- [ ] TaskScheduler: task assignment to executors
- [ ] Lab: run a multi-step query, call explain(True), identify stages

### Day 3: RDD vs DataFrame Internals
- [ ] RDD lineage and narrow vs wide dependencies
- [ ] DataFrame API and how it compiles to RDD operations
- [ ] When transformations materialise into stages
- [ ] Catalyst optimiser overview (high level)
- [ ] Lab: compare RDD vs DataFrame for the same operation

### Day 4: Shuffle Fundamentals
- [ ] What triggers a shuffle (groupBy, join, repartition)
- [ ] Shuffle write and shuffle read
- [ ] Exchange operator in physical plans
- [ ] Cost of shuffle: disk, network, serialisation
- [ ] Lab: force a shuffle, observe in explain() and Spark UI

### Day 5: Joins and Partitioning
- [ ] Broadcast join vs sort-merge join vs shuffle-hash join
- [ ] Join selection heuristics and thresholds
- [ ] Data skew: symptoms and mitigation (salting, AQE skew join)
- [ ] Partition strategy: hash, range, round-robin
- [ ] Lab: compare broadcast vs sort-merge join plans

### Day 6: Hands-On Lab
- [ ] End-to-end PySpark job: read CSV, filter, aggregate, join, write
- [ ] Inspect explain(True) at each step
- [ ] Walk through the Spark UI: jobs, stages, tasks, storage
- [ ] Identify shuffle boundaries and partition counts

### Day 7: Week 1 Wrap-Up
- [ ] Summarise the execution path for a simple pipeline
- [ ] Review questions and gaps
- [ ] Capture notes in docs/

## Week 2 — Optimisation, Internals, and Tuning

### Day 8: Catalyst Optimiser
- [ ] Rule-based optimisations (predicate pushdown, column pruning, constant folding)
- [ ] Cost-based optimisation (CBO) and statistics
- [ ] How Catalyst rewrites PySpark/SQL queries
- [ ] Lab: observe predicate pushdown in explain()

### Day 9: Tungsten and Memory Model
- [ ] Off-heap memory management
- [ ] Binary row format and cache-friendly layouts
- [ ] Python ↔ JVM data transfer overhead
- [ ] Apache Arrow and Pandas UDFs
- [ ] Lab: compare a Python UDF vs a Pandas UDF on performance

### Day 10: Physical Plans and Operators
- [ ] Whole-stage code generation (WholeStageCodegen)
- [ ] Operator fusion: what gets fused and what breaks fusion
- [ ] Common operators: Scan, Filter, Project, HashAggregate, SortMergeJoin
- [ ] Lab: read a physical plan and identify fused stages

### Day 11: Shuffle Tuning and Memory Knobs
- [ ] spark.sql.shuffle.partitions and spark.default.parallelism
- [ ] Executor memory: heap, off-heap, overhead
- [ ] spark.sql.autoBroadcastJoinThreshold
- [ ] AQE: coalescing partitions, skew join handling
- [ ] Lab: tune shuffle partitions and observe effect on a groupBy

### Day 12: Monitoring and Observability
- [ ] Spark UI deep dive: SQL tab, DAG visualisation, task metrics
- [ ] Key metrics: shuffle bytes, spill, GC time, task duration
- [ ] Databricks-specific: Ganglia, cluster metrics, driver logs
- [ ] Lab: identify a bottleneck in a slow query using the UI

### Day 13: Micro-Benchmarks
- [ ] Run a SQL workload with AQE on vs off
- [ ] Compare physical plans and execution times
- [ ] Observe partition coalescing and skew handling
- [ ] Lab: benchmark and document findings

### Day 14: Review and Next Steps
- [ ] Capture key takeaways
- [ ] Identify areas for deeper study
- [ ] Outline a follow-up plan if desired

## Delta Lake Considerations (Woven In)

- [ ] Delta transaction log basics and how Spark reads it
- [ ] File compaction (OPTIMIZE) and its effect on scan plans
- [ ] Z-ordering and data skipping: how predicates interact with file-level stats
- [ ] Optimistic concurrency and write conflicts
