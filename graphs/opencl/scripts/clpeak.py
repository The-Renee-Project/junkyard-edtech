import matplotlib.pyplot as plt
import numpy as np

# Data extraction
global_mem_bandwidth = {
    'float': 33.41,
    'float2': 33.96,
    'float4': 32.72,
    'float8': 31.53,
    'float16': 18.49
}

transfer_bandwidth = {
    'Write': 8.90,
    'Read': 10.73,
    'Write (NB)': 8.71,
    'Read (NB)': 10.56,
    'Map Read': 48.30,
    'Memcpy From': 13.73,
    'Unmap Write': 52.99,
    'Memcpy To': 14.14
}

# Convert bandwidth to latency (ms/GB)
transfer_latency = {k: 1000 / v for k, v in transfer_bandwidth.items()}

# Global Memory Bandwidth plot
plt.figure(figsize=(12, 7), dpi=300)
bandwidths = list(global_mem_bandwidth.values())
x_pos = np.arange(len(global_mem_bandwidth))

plt.bar(x_pos, bandwidths, color='#4682B4')  # Steel Blue
plt.title('Global Memory Bandwidth')
plt.xlabel('Data Type')
plt.ylabel('Bandwidth (GB/s)')
plt.xticks(x_pos, global_mem_bandwidth.keys(), rotation=45)

# Add bandwidth values on top of each bar
for i, v in enumerate(bandwidths):
    plt.text(i, v, f' {v:.2f}', ha='center', va='bottom')

plt.ylim(0, max(bandwidths) * 1.1)  # Increase y-axis limit by 10%
plt.tight_layout()
plt.savefig('global_memory_bandwidth.png')
plt.close()

# Transfer Latency plot
plt.figure(figsize=(13, 7), dpi=300)
y_pos = np.arange(len(transfer_latency))
latencies = list(transfer_latency.values())

plt.barh(y_pos, latencies, color='#66CDAA')  # Medium Aquamarine
plt.yticks(y_pos, list(transfer_latency.keys()))
plt.title('Transfer Latency')
plt.xlabel('Latency (ms/GB)')
plt.ylabel('Operation')

# Add latency values at the end of each bar
for i, v in enumerate(latencies):
    plt.text(v, i, f' {v:.2f}', va='center')

plt.xlim(0, max(latencies) * 1.1)  # Increase x-axis limit by 10%
plt.tight_layout()
plt.savefig('transfer_latency.png')
plt.close()

print("Plots have been saved as 'global_memory_bandwidth.png' and 'transfer_latency.png'")
