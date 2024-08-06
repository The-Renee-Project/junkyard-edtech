import sys
import pandas as pd
import matplotlib.pyplot as plt

DEFAULT_DPI = 300  # Default DPI value

def read_data(filename):
    """Read and process data from a CSV file."""
    try:
        df = pd.read_csv(filename, sep=',', skipinitialspace=True)
        return df['Iops/byte'], df['GIOPS']
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Required column {e} not found in '{filename}'.")
        sys.exit(1)

def plot_data(data_list, output_file, dpi):
    """Create a plot from the given data and save it to the specified file."""
    plt.figure(figsize=(8, 5))  # Reduced figure size
    colors = ['#00A86B', '#8A2BE2']
    labels = ["Pixel Fold", "1080 Ti"]
    
    for i, (x, y, _) in enumerate(data_list):
        plt.plot(x, y, color=colors[i], linestyle='-', label=labels[i])
    
    plt.xlabel('Arithmetic Intensity (Iops/byte)')
    plt.ylabel('GIOPS')
    plt.title('GIOPS vs Arithmetic Intensity')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis to logarithmic scale
    plt.yscale('log')
    
    # Reduce whitespace
    plt.tight_layout()
    
    try:
        plt.savefig(output_file, dpi=dpi, bbox_inches='tight')
        print(f"Plot saved to {output_file} with DPI {dpi}")
    except Exception as e:
        print(f"Error saving plot to {output_file}: {e}")
    
    plt.close()

def main():
    """Main function to handle command-line arguments and orchestrate the program."""
    if len(sys.argv) not in [4, 5]:
        print("Usage: python script.py <pixel_fold_file> <1080ti_file> <output_file> [dpi]")
        sys.exit(1)
    
    pixel_fold_file = sys.argv[1]
    ti_1080_file = sys.argv[2]
    output_file = sys.argv[3]
    
    # Use the provided DPI if available, otherwise use the default
    dpi = DEFAULT_DPI
    if len(sys.argv) == 5:
        try:
            dpi = int(sys.argv[4])
        except ValueError:
            print(f"Error: Invalid DPI value. Using default DPI of {DEFAULT_DPI}")
    
    data_list = []
    for filename in [pixel_fold_file, ti_1080_file]:
        x, y = read_data(filename)
        data_list.append((x, y, filename))
    
    plot_data(data_list, output_file, dpi)

if __name__ == "__main__":
    main()
