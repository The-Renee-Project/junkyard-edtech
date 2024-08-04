import json
import matplotlib.pyplot as plt
import numpy as np

def create_roofline_plot(peak_performance, peak_bandwidth, data, title, filename):
    plt.figure(figsize=(12, 8))
    
    # Create the roofline
    x = np.logspace(-1, 4, 100)
    y_memory = peak_bandwidth * x
    y_compute = np.full_like(x, peak_performance)
    y_roofline = np.minimum(y_memory, y_compute)
    
    plt.loglog(x, y_roofline, 'k-', linewidth=2, label='Roofline')
    plt.loglog(x, y_memory, 'b--', linewidth=1, label='Memory Bound')
    plt.loglog(x, y_compute, 'r--', linewidth=1, label='Compute Bound')
    
    # Plot benchmark points
    for name, (perf, intensity) in data.items():
        plt.plot(intensity, perf, 'o', markersize=8, label=name)
    
    plt.xlabel('Operational Intensity (FLOPS/Byte)')
    plt.ylabel('Performance (GFLOPS)')
    plt.title(title)
    plt.legend(loc='lower right')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.ylim(0.1, peak_performance * 10)
    plt.xlim(0.1, 1000)
    
    plt.savefig(filename)
    plt.close()

def main():
    DATA_PATH = 'data.json'
    MAX_BANDWIDTH = 51.2
    MAX_TFLOPS = 0.7
    projphysx_data = None
    with open(DATA_PATH, 'r') as f:
        data = json.load(f)
        clpeak_data = data['clpeak_bench']
        projphysx_data = data['projectphysx_bench']
        global_mem_bw = [clpeak_data['global_memory_bandwidth']['float'], clpeak_data['global_memory_bandwidth']['float2'], clpeak_data['global_memory_bandwidth']['float4'], clpeak_data['global_memory_bandwidth']['float8'], clpeak_data['global_memory_bandwidth']['float16']]
        
        plt.bar(['Float', 'Float2', 'Float4', 'Float8', 'Float16'], global_mem_bw)
        plt.axhline(y=MAX_BANDWIDTH, color='r', linestyle='--')
        plt.text(0, MAX_BANDWIDTH, 'Max Bandwidth: 51.2 GB/s', va='center', ha='left', backgroundcolor='w')
        plt.ylabel('Bandwidth (GB/s)')
        plt.xlabel('Data Type')
        plt.title('clpeak: Global Memory Bandwidth')
        plt.savefig('global_memory_bandwidth.png')
        plt.close()
        
        # compute graph
        compute = [clpeak_data['single_precision_compute']['float']/1000, clpeak_data['single_precision_compute']['float2']/1000, clpeak_data['single_precision_compute']['float4']/1000, clpeak_data['single_precision_compute']['float8']/1000, clpeak_data['single_precision_compute']['float16']/1000]
        plt.bar(['Float', 'Float2', 'Float4', 'Float8', 'Float16'], compute)
        plt.axhline(y=MAX_TFLOPS, color='r', linestyle='--')
        plt.text(0, MAX_TFLOPS, 'Max TFLOPS: 0.7', va='center', ha='left', backgroundcolor='w')
        plt.ylabel('TFLOPS')
        plt.xlabel('Data Type')
        plt.title('clpeak: Single Precision Compute')
        plt.savefig('single_precision_compute.png')
        plt.close()
        
        # half precision compute graph
        half_precision_compute = [clpeak_data['half_precision_compute']['half']/1000, clpeak_data['half_precision_compute']['half2']/1000, clpeak_data['half_precision_compute']['half4']/1000, clpeak_data['half_precision_compute']['half8']/1000, clpeak_data['half_precision_compute']['half16']/1000]
        plt.bar(['Half', 'Half2', 'Half4', 'Half8', 'Half16'], half_precision_compute)
        plt.axhline(y=MAX_TFLOPS, color='r', linestyle='--')
        plt.text(0, MAX_TFLOPS, 'Approx. Max TFLOPS: 0.7', va='center', ha='left', backgroundcolor='w')
        plt.ylabel('TFLOPS')
        plt.xlabel('Data Type')
        plt.title('clpeak: Half Precision Compute')
        plt.savefig('half_precision_compute.png')
        plt.close()
        
        # integer compute
        integer_compute = [clpeak_data['integer_compute']['int']/1000, clpeak_data['integer_compute']['int2']/1000, clpeak_data['integer_compute']['int4']/1000, clpeak_data['integer_compute']['int8']/1000, clpeak_data['integer_compute']['int16']/1000]
        plt.bar(['Int', 'Int2', 'Int4', 'Int8', 'Int16'], integer_compute)
        plt.ylabel('TIOPS')
        plt.xlabel('Data Type')
        plt.title('clpeak: Integer Compute')
        plt.savefig('integer_compute.png')
        plt.close()
        
        # transfer bandwidth
        transfer_data = [clpeak_data['transfer_bandwidth']['enqueueWriteBuffer'], clpeak_data['transfer_bandwidth']['enqueueReadBuffer'], clpeak_data['transfer_bandwidth']['enqueueWriteBuffer_non_blocking'], clpeak_data['transfer_bandwidth']['enqueueReadBuffer_non_blocking'], clpeak_data['transfer_bandwidth']['enqueueMapBuffer_for_read'], clpeak_data['transfer_bandwidth']['memcpy_from_mapped_ptr'], clpeak_data['transfer_bandwidth']['memcpy_to_mapped_ptr']]
        titles = ['Enq. Write', 'Enq. Read', 'Enq. Write NB', 'Enq. Read NB', 'Enq. Map Read', 'Memcpy from Mapped', 'Memcpy to Mapped']
        plt.figure(figsize=(10, 8))
        plt.bar(titles, transfer_data)
        plt.ylabel('Bandwidth (GB/s)')
        plt.xlabel('Transfer Type')
        plt.title('clpeak: Transfer Bandwidth')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig('transfer_bandwidth.png')
        plt.close()
        
        compute_perf = projphysx_data['compute_performance']
        plt.figure(figsize=(10, 6))
        plt.bar(compute_perf.keys(), compute_perf.values())
        plt.axhline(y=MAX_TFLOPS, color='r', linestyle='--')
        plt.text(0, MAX_TFLOPS, f'Approx. Max TFLOPS: {MAX_TFLOPS}', va='center', ha='left', backgroundcolor='w')
        plt.ylabel('TFLOPS/TOPS')
        plt.xlabel('Data Type')
        plt.title('ProjectPhysX: Compute Performance')
        plt.xticks(rotation=45)
        plt.tight_layout()
#        plt.savefig('projphysx_res/compute_performance.png')
        plt.close()

        # Memory Bandwidth graph
        mem_bw = projphysx_data['memory_bandwidth']
        plt.figure(figsize=(10, 6))
        plt.bar(mem_bw.keys(), mem_bw.values())
        plt.axhline(y=MAX_BANDWIDTH, color='r', linestyle='--')
        plt.text(0, MAX_BANDWIDTH, f'Max Bandwidth: {MAX_BANDWIDTH} GB/s', va='center', ha='left', backgroundcolor='w')
        plt.ylabel('Bandwidth (GB/s)')
        plt.xlabel('Access Type')
        plt.title('ProjectPhysX: Memory Bandwidth')
        plt.xticks(rotation=45)
        plt.tight_layout()
#        plt.savefig('projphysx_res/memory_bandwidth.png')
        plt.close()

        # PCIe Bandwidth graph
        pcie_bw = projphysx_data['pcie_bandwidth']
        plt.figure(figsize=(10, 6))
        plt.bar(pcie_bw.keys(), pcie_bw.values())
        plt.axhline(y=MAX_BANDWIDTH, color='r', linestyle='--')
        plt.text(0, MAX_BANDWIDTH, f'Max Bandwidth: {MAX_BANDWIDTH} GB/s', va='center', ha='left', backgroundcolor='w')
        plt.ylabel('Bandwidth (GB/s)')
        plt.xlabel('Transfer Type')
        plt.title('ProjectPhysX: PCIe Bandwidth')
        plt.xticks(rotation=45)
        plt.tight_layout()
#        plt.savefig('projphysx_res/pcie_bandwidth.png')
        plt.close()

        # Roofline plots
        # Clpeak data (estimated operational intensities)
        clpeak_roofline_data = {
            'Float': (clpeak_data['single_precision_compute']['float'], clpeak_data['single_precision_compute']['float'] / clpeak_data['global_memory_bandwidth']['float']),
            'Float2': (clpeak_data['single_precision_compute']['float2'], clpeak_data['single_precision_compute']['float2'] / clpeak_data['global_memory_bandwidth']['float2']),
            'Float4': (clpeak_data['single_precision_compute']['float4'], clpeak_data['single_precision_compute']['float4'] / clpeak_data['global_memory_bandwidth']['float4']),
            'Float8': (clpeak_data['single_precision_compute']['float8'], clpeak_data['single_precision_compute']['float8'] / clpeak_data['global_memory_bandwidth']['float8']),
            'Float16': (clpeak_data['single_precision_compute']['float16'], clpeak_data['single_precision_compute']['float16'] / clpeak_data['global_memory_bandwidth']['float16'])
        }

        # ProjectPhysX data (estimated operational intensities)
        projphysx_roofline_data = {dtype: (perf, perf / projphysx_data['memory_bandwidth']['coalesced_read']) for dtype, perf in projphysx_data['compute_performance'].items()}
#        print(projphysx_roofline_data)
        # Create roofline plots
        create_roofline_plot(MAX_TFLOPS * 1000, MAX_BANDWIDTH, clpeak_roofline_data, 'Roofline Plot', 'clpeak_roofline.png')
#        create_roofline_plot(MAX_TFLOPS * 1000, MAX_BANDWIDTH, projphysx_roofline_data, 'ProjectPhysX Roofline Plot', 'projphysx_res/projphysx_roofline.png')

if __name__ == '__main__':
    main()
