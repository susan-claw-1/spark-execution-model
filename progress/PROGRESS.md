# Progress Tracker

## Week 1 — Architecture, DAGs, and Data Movement

- [ ] Day 1: Core architecture — driver, executors, cluster manager, Py4J bridge
- [ ] Day 2: DAG and scheduling — logical vs physical plans, DAGScheduler, TaskScheduler
- [ ] Day 3: RDD vs DataFrame internals — transformations, stages, Catalyst overview
- [ ] Day 4: Shuffle fundamentals — shuffle read/write, exchange operators
- [ ] Day 5: Joins and partitioning — broadcast vs hash joins, skew, partition strategy
- [ ] Day 6: Hands-on lab — run a PySpark job, inspect explain(), read the Spark UI
- [ ] Day 7: Week 1 wrap-up and review

## Week 2 — Optimisation, Internals, and Tuning

- [ ] Day 8: Catalyst optimiser — rule-based and cost-based optimisation
- [ ] Day 9: Tungsten and memory — off-heap memory, Arrow, Pandas UDFs
- [ ] Day 10: Physical plans and operators — whole-stage codegen, operator fusion
- [ ] Day 11: Shuffle tuning and memory knobs — partitions, parallelism, executor memory
- [ ] Day 12: Monitoring and observability — Spark UI, metrics, GC, tuning loops
- [ ] Day 13: Micro-benchmarks — AQE on vs off, plan comparison
- [ ] Day 14: Review and next steps

## Delta Lake Considerations

- [ ] Delta transaction log and how it interacts with Spark's execution model
- [ ] Optimistic concurrency, file compaction, and Z-ordering effects on query plans
