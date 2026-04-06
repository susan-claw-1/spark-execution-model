# Day 2 Summary (offline, no Spark needed)

- Day 2 focused on DAGs, shuffles, partitioning, and explain output.
- Typical two-stage pattern for a repartition + groupBy:
  - Stage 1: shuffle write into N partitions
  - Stage 2: shuffle read + aggregation
- Data skew can cause OOM risk; strategies include AQE partition coalescing, repartitioning, and salting for extreme skew.
- AQE can help with dynamic repartitioning and coalescing; salting remains an option for extreme skew.
- Explain(True) reveals a multi-stage physical plan, showing explicit Shuffle boundaries when repartition is used.
- Day 2 artifacts: lab2.py, lab2.md, and the day2 cheat card (Mermaid diagram) for quick reference.
