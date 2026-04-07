#!/usr/bin/env python3
"""
Offline splits simulation for Day 2: how data splits might be formed from file sizes.
This is a purely conceptual helper to reason about partitions, not a Spark run.
"""
import math

def simulate_splits(file_sizes_mb, max_partition_mb=4):
    """Return a list of splits per file and total splits.

    - file_sizes_mb: list of file sizes in MB
    - max_partition_mb: max bytes per partition (MB here) used to compute splits
    """
    splits_per_file = [math.ceil(sz / max_partition_mb) for sz in file_sizes_mb]
    total_splits = sum(splits_per_file)
    print("Offline splits simulation")
    for i, s in enumerate(splits_per_file, start=1):
        print(f"File {i}: {file_sizes_mb[i-1]} MB -> {s} split(s)")
    print(f"Total splits (across all files): {total_splits}")
    return splits_per_file, total_splits

if __name__ == "__main__":
    # Example layout: you can edit these values to mirror your data footprint
    file_sizes_mb = [12, 6, 5, 18]  # total 41 MB
    simulate_splits(file_sizes_mb, max_partition_mb=4)
