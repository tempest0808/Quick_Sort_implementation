# Quicksort: Implementation, Analysis, and Randomization
 
A Python implementation of standard (deterministic) Quicksort and randomized Quicksort, along with a written report covering the time and space complexity of each, and an empirical benchmark comparing them across different input distributions.
 
## Files
 
| File | Description |
|---|---|
| `quicksort.py` | Both Quicksort implementations: `deterministic_quicksort` (last element as pivot) and `randomized_quicksort` (random pivot selection). Shared Lomuto partition logic. |
| `benchmark.py` | Times both implementations on random, sorted, and reverse-sorted inputs at several sizes, and prints a results table. |
| `Assignment_5_Report.docx` | Same report content as a Word document. |
 
## Running it
 
Requires Python 3. No third-party packages are needed.
 
```bash
# Run the demo in quicksort.py
python3 quicksort.py
 
# Run the full benchmark (takes a few seconds, prints a results table)
python3 benchmark.py
```
 
## Quick summary
 
Both implementations use the same Lomuto partition scheme, the only difference is how the pivot is chosen:
 
- **Deterministic:** always the last element of the current subarray.
- **Randomized:** a uniformly random element of the current subarray, swapped into the last position before partitioning.
On random input, the two perform about the same. On already-sorted or reverse-sorted input, the deterministic version degrades to O(n²), while the randomized version stays close to O(n log n) regardless of input order. Full reasoning and the benchmark numbers are in `quicksort_report.md`.
