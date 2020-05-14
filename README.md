# Add-Columns-to-CSVs
A Python script that add new columns to csv files

This python script could be run in terminal together with the xargs command line utility to add multiple numbers of columns to multiple csv files.

EXAMPLE (in the case below the python script is placed in the same folder as the CSV files):

``find *.csv | xargs python3 add_new_columns.py``
