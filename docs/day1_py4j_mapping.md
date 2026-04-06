# Day 1 Py4J Mapping Card

A compact mapping of Day 1 steps to Py4J-driven interactions between Python (PySpark) and the JVM Spark engine.

Day 1 overview
- Focus: Core architecture and Py4J bridge: driver (Python) ↔ JVM (Spark) → Executors
- Lab: PySpark notebook steps (Step 0–3) described in Day 1 lab

Step 0 — Print environment info
- Python side:
  - Code: print("Spark version:", spark.version); print("Python version:", sys.version)
- Py4J mapping:
  - Python calls SparkSession.version through a Python proxy to the JVM; the JVM returns the version string back via Py4J.
- JVM action: read Spark version property; result flows back to Python.

Step 1 — Create tiny DataFrame and inspect plan
- Python side:
  - Code: df = spark.range(10).toDF("n"); df.show(); df.printSchema()
- Py4J mapping:
  - Python invokes DataFrame-derived methods on the Java proxies; the actual work of range/Project happens in JVM; Python gets a small preview of results.
- JVM action: Range generation and DataFrame creation occur in Spark (JVM); Python receives the tabular output for display and the schema.

Step 2 — Inspect the execution plan
- Python side:
  - Code: df.explain(True)
- Py4J mapping:
  - Python asks JVM to generate the full plan and return it; Plan text is produced on the JVM and streamed back to Python.
- JVM action: Build logical/physical plan; render explain text; Python prints it.

Step 3 — Optional quick check
- Python side:
  - Code: print("Partitions:", df.rdd.getNumPartitions())
- Py4J mapping:
  - Accessing df.rdd causes a bridge call to the JVM to fetch the partition count for the DataFrame.
- JVM action: Compute partitioning information; return to Python via Py4J.

Key Py4J vocab mapped to Day 1
- Py4J bridge / gateway: The channel enabling Python↔JVM calls
- GatewayServer (on JVM) and JavaGateway (Python): The endpoints and client object
- JavaObject / Py4J proxy: Python objects that proxy JVM objects
- SparkSession / DataFrame proxies: Python side references to JVM-side Spark constructs
- Driver (Python) vs Executors (JVM)
- Actions trigger compute vs Transformations lazily build the plan

If you want, I can also create a tiny one-page printable quick reference with the above mappings. Would you like that?