"""
spec_graph
-----------------------------------------------------------
Create a bar graph of rates from results of running intrate
test using runcpu2017
-----------------------------------------------------------
INPUTS
  csv file with results
-----------------------------------------------------------
OUTPUTS
  Bar graph
----------------------------------------------------------
USAGE: python3 spec_graph.py
"""
import pandas
from matplotlib import pyplot

if __name__ == "__main__":
    CSV = 'spec_intrate.csv'
    DATA = pandas.read_csv(CSV)
    DATAFRAME = pandas.DataFrame(DATA)

    BENCHMARK = DATAFRAME['Benchmark']
    BASE_RATE = DATAFRAME['Base Rate']

    _, AXES = pyplot.subplots(figsize=(6, 4))
    AXES.barh(BENCHMARK, BASE_RATE)
    AXES.set_xlabel('Base Rate')
    AXES.set_title('Pixel Fold SPEC Intrate Test')
    pyplot.tight_layout()
    pyplot.show()
