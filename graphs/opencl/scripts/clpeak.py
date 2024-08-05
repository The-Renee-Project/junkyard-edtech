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
    'Memcpy To': 14.14
}

# Convert bandwidth to latency (ms/GB)
transfer_latency = {k: 1000 / v for k, v in transfer_bandwidth.items()}

# Global Memory Bandwidth plot
plt.figure(figsize=(10, 6), dpi=300)
plt.bar(global_mem_bandwidth.keys(), global_mem_bandwidth.values(), color='#4682B4')  # Steel Blue
plt.title('Global Memory Bandwidth')
plt.xlabel('Data Type')
plt.ylabel('Bandwidth (GB/s)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('global_memory_bandwidth.png')
plt.close()

# Transfer Latency plot
plt.figure(figsize=(10, 6), dpi=300)
y_pos = np.arange(len(transfer_latency))
plt.barh(y_pos, list(transfer_latency.values()), color='#66CDAA')  # Medium Aquamarine
plt.yticks(y_pos, list(transfer_latency.keys()))
plt.title('Transfer Latency')
plt.xlabel('Latency (ms/GB)')
plt.ylabel('Operation')
plt.tight_layout()
plt.savefig('transfer_latency.png')
plt.close()

print("Plots have been saved as 'global_memory_bandwidth.png' and 'transfer_latency.png'")
