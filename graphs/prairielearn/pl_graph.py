"""
pl_graph
-----------------------------------------------------------
Create a line graph of memory/cpu utilization from results 
of docker stats for prairie learn
-----------------------------------------------------------
INPUTS
  csv file with results
-----------------------------------------------------------
OUTPUTS
  line graph
----------------------------------------------------------
USAGE: python3 pl_graph.py
"""
import pandas
from matplotlib import pyplot

if __name__ == '__main__':
    CSV = 'stats.csv'
    DATA = pandas.read_csv(CSV)
    DATAFRAME = pandas.DataFrame(DATA)
    MEM = DATAFRAME['MEM%']
    CPU = DATAFRAME['CPU%']
    # Create side by side plot of memory and cpu utilization
    _, AXES = pyplot.subplots(nrows=2, ncols=1, figsize=(6, 4))
    AXES[0].plot(MEM, color='purple', label='Memory Utilization (%)')
    AXES[0].legend(loc='upper right')
    AXES[1].plot(CPU, label='CPU Utilization (%)')
    AXES[1].legend(loc='upper right')
    pyplot.xlabel('Time Elapsed (sec)')
    """
    pyplot.plot(MEM)

    pyplot.ylabel('Memory Utilization %')
"""
    pyplot.show()
