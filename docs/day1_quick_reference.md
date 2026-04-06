# Day 1 Quick Reference (Printable)

Py4J and Day 1 flow at a glance

- Py4J is the bridge between Python (driver) and the JVM Spark engine (driver/executors).
- The Python driver talks to the JVM gateway (GatewayServer) to obtain proxies for SparkSession and DataFrame.
- JVM executes all heavy work (Spark tasks) on executors; Python primarily orchestrates.
- Data moves across Py4J when you call methods or transfer small results; bulk data is moved via Spark’s own mechanisms.

Key steps (Day 1 lab)
1) Print environment: Spark version, Python version
2) Create tiny DataFrame and show it
3) Explain plan (explain(True))
4) Optional: partitions via df.rdd.getNumPartitions()

Py4J quick vocab
- Python driver = control plane
- JVM Spark = compute plane
- Py4J bridge/gateway = two-way channel
- JavaObject/Proxy = Python-side handle to JVM objects
- Driver vs Executors = Python vs JVM workers

If you print this, you’ll have a handy cheat-sheet for Day 1. Keep as a printable card or a quick reference in your notes.