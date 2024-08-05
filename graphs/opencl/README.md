# OpenCL Benchmark

### Structure
There are 2 subdirectories:
- `clpeak_res`
- `mixbench_res`
- `candidate_graphs`

The first two correspond to the `clpeak` and `mixbench` benchmarks respectively. The last one contains the finalised graphs to be used in the paper.

Here are the graphs:
<table>
  <tr>
    <td><img src="candidate_graphs/global_memory_bandwidth.png" width="400"></td>
    <td><img src="candidate_graphs/transfer_latency.png" width="400"></td>
  </tr>
  <tr>
    <td><img src="candidate_graphs/cand_single_precision_execution_time.png" width="400"></td>
    <td><img src="candidate_graphs/cand_single_precision_performance.png" width="400"></td>
  </tr>
  <tr>
    <td><img src="candidate_graphs/cand_half_precision_execution_time.png" width="400"></td>
    <td><img src="candidate_graphs/cand_half_precision_performance.png" width="400"></td>
  </tr>
  <tr>
    <td><img src="candidate_graphs/cand_integer_operations_execution_time.png" width="400"></td>
    <td><img src="candidate_graphs/cand_integer_operations_performance.png" width="400"></td>
  </tr>
</table>

These were run on the Google Pixel Fold.

### Benchmark References

#### clpeak
> https://github.com/krrishnarraj/clpeak

#### mixbench
> https://github.com/ekondis/mixbench

> [Paper](https://doi.org/10.1016/j.jpdc.2017.04.002)
