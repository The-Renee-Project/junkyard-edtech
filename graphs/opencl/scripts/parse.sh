#!/bin/bash

# Remove the first line and the Experiment ID column
tail -n +2 | cut -d',' -f2- |

# Process the input and split into separate files
awk -F, '
{
    # Single precision
    print $1","$2","$3","$4 > "../data/single.csv"
    
    # Double precision
    print $5","$6","$7","$8 > "../data/double.csv"
    
    # Half precision
    print $9","$10","$11","$12 > "../data/half.csv"
    
    # Integer operations
    print $13","$14","$15","$16 > "../data/integer.csv"
}
'
