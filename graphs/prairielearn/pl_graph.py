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
    # Creaet line plo of cpu utilization
    pyplot.plot(MEM)

    pyplot.title('Pixel Fold Prairie Learn Test Memory Utilization')
    pyplot.xlabel('Time Elapsed (sec)')
    pyplot.ylabel('Memory Utilization %')

    pyplot.show()
