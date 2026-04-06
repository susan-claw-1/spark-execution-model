# Day 2 Diagram — Shuffle Read and Two-Stage Plan

Mermaid diagram:

```mermaid
graph TD
  subgraph Stage_1
    A[Input Data] --> B[Shuffle Write into 8 partitions]
  end
  subgraph Stage_2
    C[Shuffle Read: fetch from Stage_1 outputs] --> D[Aggregation / Count]
  end
  B --> C
  D --> E[Output]
```

Notes:
- This diagram illustrates the canonical two-stage pattern when you do df.repartition(8).groupBy().count(): Stage 1 writes shuffled data across 8 partitions; Stage 2 reads that shuffled data to perform the final aggregation.