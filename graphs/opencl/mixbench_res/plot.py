import csv
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

def read_csv_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # Skip the header rows
        next(reader)
        next(reader)
        data = list(reader)
    return data

def extract_data(data, columns):
    return [[float(row[i]) for i in columns] for row in data if row]

def create_csv_string(data, header):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(header)
    writer.writerows(data)
    return output.getvalue()

def plot_performance(data, x_label, y_label, title, filename, upper_limit=None):
    intensity = [row[0] for row in data]
    performance = [row[1] for row in data]

    x_smooth = np.linspace(min(intensity), max(intensity), 200)
    y_smooth = np.interp(x_smooth, intensity, performance)

    plt.figure(figsize=(10, 6))
    plt.plot(x_smooth, y_smooth, 'b-', linewidth=2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True, linestyle='--', alpha=0.7)

    max_perf_index = performance.index(max(performance))
    max_intensity = intensity[max_perf_index]
    max_perf = performance[max_perf_index]
    plt.annotate(f'Max: ({max_intensity:.2f}, {max_perf:.2f})', 
                 (max_intensity, max_perf),
                 textcoords="offset points", 
                 xytext=(0,10), ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="b", alpha=0.3),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    if upper_limit:
        plt.axhline(y=upper_limit, color='r', linestyle='--', linewidth=2)
        plt.annotate(f'Approx. Max Perf. {upper_limit/1000} TFLOPS', 
                     (min(intensity), upper_limit),
                     textcoords="offset points", 
                     xytext=(10, 5), ha='left', va='bottom',
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="r", alpha=0.3))
        plt.ylim(0, upper_limit * 1.1)  # Set y-axis limit to 110% of upper limit

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

def process_data(input_file):
    raw_data = read_csv_data(input_file)

    # Extract data for each precision
    single_data = extract_data(raw_data, [1, 3, 4])
    half_data = extract_data(raw_data, [9, 11, 12])
    integer_data = extract_data(raw_data, [13, 15, 16])

    # Create CSV strings (in memory)
    single_csv = create_csv_string(single_data, ['Flops/byte', 'GFLOPS', 'GB/sec'])
    half_csv = create_csv_string(half_data, ['Flops/byte', 'GFLOPS', 'GB/sec'])
    integer_csv = create_csv_string(integer_data, ['Iops/byte', 'GIOPS', 'GB/sec'])

    # Create plots
    plot_performance(single_data, 'Arithmetic Intensity (Flops/byte)', 'Performance (GFLOPS)', 
                     'Performance vs Arithmetic Intensity for Single Precision', 
                     'single_precision_performance.png', upper_limit=700)
    
    plot_performance(half_data, 'Arithmetic Intensity (Flops/byte)', 'Performance (GFLOPS)', 
                     'Performance vs Arithmetic Intensity for Half Precision', 
                     'half_precision_performance.png')
    
    plot_performance(integer_data, 'Arithmetic Intensity (Iops/byte)', 'Performance (GIOPS)', 
                     'Performance vs Arithmetic Intensity for Integer Operations', 
                     'integer_operations_performance.png')

    print("Processing complete. PNG files created for single precision, half precision, and integer operations.")

if __name__ == "__main__":
    input_file = 'unparsed.csv'
    process_data(input_file)
