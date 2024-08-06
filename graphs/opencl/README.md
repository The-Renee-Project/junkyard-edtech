# OpenCL Benchmark

### Structure
- `data` contains the parsed csv data split into single precision, double, half, and integer for both the platforms
- `graphs` contains the finalised graphs
- `scripts` contains the script to parse the unparsed csv data and to generate the graphs
- `unparsed` unparsed raw csv data for both the platforms

And a `graphs` directory containing the finalised graphs to be used in the paper.

Here are the graphs:
<table>
  <tr>
    <td><img src="graphs/global_memory_bandwidth.png" width="400"></td>
    <td><img src="graphs/transfer_latency.png" width="400"></td>
  </tr>
  <tr>
    <td><img src="graphs/single_time.png" width="400"></td>
    <td><img src="graphs/single_perf.png" width="400"></td>
  </tr>
  <tr>
    <td><img src="graphs/integer_time.png" width="400"></td>
    <td><img src="graphs/integer_perf.png" width="400"></td>
  </tr>
</table>

These were run on the Google Pixel Fold and a server with an NVIDIA GTX 1080 Ti.

### Benchmark References

#### clpeak
> https://github.com/krrishnarraj/clpeak

#### mixbench
> https://github.com/ekondis/mixbench

> [Paper](https://doi.org/10.1016/j.jpdc.2017.04.002)

