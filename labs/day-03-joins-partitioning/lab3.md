# Day 3 Lab: Joins and Partitioning

Goal: Explore how different join strategies work in Spark SQL / PySpark and how partitioning affects performance (shuffle boundaries, broadcast vs shuffle joins, AQE).

Overview of join strategies (high level)
- Broadcast Hash Join: one side is small and broadcast to all executors.
- Shuffle Hash Join: both sides are large; data is shuffled by join key.
- Sort-Merge Join: keys are sorted or can be sorted efficiently; good for large sorted inputs.
- Broadcast Nested Loop: fallback in pathological cases.

What to observe during the lab
- How Spark chooses a join strategy (observe explain(True) output).
- The effect of partitioning the data on join performance.
- The effect of enabling broadcast joins (AQE behavior is optional for this lab).

Lab setup
- You’ll create two DataFrames:
  - A big fact-like table with 1e5-1e6 rows (configurable).
  - A smaller dimension-like table with a key column to join on.
- You’ll run both a regular inner join and a broadcast join and compare plans and outputs.

Lab steps
1) Create two DataFrames in PySpark:
   - big_df: range(0, big_n) with a key column (customer_id) derived from the id.
   - small_df: range(0, small_n) with a matching customer_id (mod-based key) and a small payload column.
2) Inner join on the key without explicit broadcast.
3) Call explain(True) to inspect the physical plan and identify the join strategy.
4) Repeat with an explicit broadcast join:
   - join(big_df, broadcast(small_df), on = 'customer_id')
5) Optional: do a left join as a surface of partitioning effects.
6) Observe: how AQE may adjust plans if enabled (optional).
7) Compare plans: which sections indicate Shuffle Hash Join, Broadcast Hash Join, or Sort-Merge Join?

What you’ll learn
- How data is partitioned before the join and how that affects the chosen strategy.
- When a broadcast join is feasible and how to enable/limit it via spark.sql.autoBroadcastJoinThreshold or AQE.
- The role of shuffle partitions in join performance.

Files associated with Day 3 (scaffold)
- labs/day-03-joins-partitioning/lab3.py (runnable PySpark script)
- labs/day-03-joins-partitioning/lab3.md (this write-up)
- docs/day3_diagram.md (Mermaid diagram for Day 3 joins/partitioning)

Next steps
- If you want, I can flesh this out into a full runnable lab script with command-line parameters for big_n/small_n and a couple of join scenarios. I can also add an explain-based comparison output to stdout.

Would you like me to proceed with creating lab3.py and the Day 3 diagrams and commit them as part of Day 3 scaffolding?