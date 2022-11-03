import pandas as pd 

slp_csv = pd.read_csv('MyQualtricsDownload/SLP Satisfaction Survey.csv')
slp_csv

slp_csv.columns

slp_csv.Q9.value_counts()

small_slp_csv = slp_csv.drop([])