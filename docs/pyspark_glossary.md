# PySpark & Spark Glossary (Day 1 Reference)

A compact glossary to help you recall core terms when working with PySpark and the JVM-based Spark runtime.

- Py4J bridge: Cross-language bridge between Python and the JVM-backed Spark engine. It provides gateway servers and proxies so Python code can call Java/Spark methods.
- GatewayServer (JVM): The server on the JVM side that exposes Java objects to Py4J.
- JavaGateway (Python): The Py4J client that connects to the JVM gateway and obtains proxies to Java objects.
- JavaObject / Py4J proxy: Python representations of Java objects; Python calls on these proxies are forwarded to the JVM.
- SparkSession: Entry point for Spark with the DataFrame/Dataset APIs; holds configuration and context for a Spark app.
- DataFrame / Dataset: Distributed, structured data. DataFrame is the Dataset[Row] API; operations are optimized by Spark.
- RDD: Resilient Distributed Dataset, the older, low-level distributed data abstraction. Still present for fine-grained control.
- Driver: The Python process that orchestrates the Spark application and issues work to the cluster.
- Executors: JVM processes on the cluster that perform the actual data processing tasks.
- Cluster Manager: Component that allocates resources to Spark apps (e.g., Standalone, YARN, Kubernetes, Databricks).
- DAG (Directed Acyclic Graph): Graph of operations showing data dependencies and transformation flow.
- DAGScheduler: Builds stages and manages shuffle boundaries based on logical plan.
- TaskScheduler: Assigns launched tasks to executors across the cluster.
- Transformations vs Actions: Transformations build the plan (lazy); Actions trigger computation and return results.
- Lazy evaluation: Spark defers execution until an action is called.
- Shuffle: Data movement between partitions across the network/disk caused by wide transformations like groupBy or join.
- Joins: Different strategies (Broadcast Join, Shuffle Hash Join, Sort-Merge Join) chosen by the optimizer.
- Partitioning / Repartition / Coalesce: How data is divided into partitions; affects parallelism and shuffle behavior.
- Catalyst Optimizer: The rule-based and cost-based optimization layer for DataFrame/Spark SQL. Rewrites queries for efficiency.
- Tungsten: The memory model and execution engine optimizing memory, binary formats, and code generation.
- Whole-Stage Codegen: Code generation that fuses multiple operators to reduce interpretation overhead.
- AQE (Adaptive Query Execution): Runtime optimization that adapts the plan based on observed stats during execution.
- UDF / Pandas UDF / Arrow: User-Defined Functions; Arrow speeds data transfer for Python UDFs and Pandas UDFs.
- Delta Lake: Lakehouse storage with a transaction log (Delta log). Concepts include OPTIMIZE, Z-Ordering, VACUUM, and data skipping.
- Delta log: The transaction log that records schema, data changes, and commits for Delta tables.
- Spark UI: Web UI to inspect jobs, stages, tasks, storage, and metrics.
- SparkContext: Older entry point (pre-SparkSession) to Spark; largely replaced by SparkSession in modern APIs.
- DBR: Databricks Runtime, the execution environment optimized for Databricks.
- Explain / explain(True): Commands to print the logical and physical plans of a job; helps diagnose performance.
- Broadcast Join: A join strategy where the smaller table is broadcast to all workers to avoid shuffles.
- Data Skipping: Delta Lake optimization using statistics to skip irrelevant data.

> Quick Day 1 mapping: Day 1 uses Py4J to connect Python to JVM Spark; Python issues commands via proxies to SparkSession/DataFrame; the JVM executes the heavy lifting on executors while Python handles orchestration.