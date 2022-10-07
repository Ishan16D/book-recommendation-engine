from operator import index
import pandas as pd

corr = pd.read_csv('data/correlations.csv', index_col=0)

series = input('Please enter a series: ')

for i in list(range(1, 6)):
    print(
        f'The number {i} series is {corr[series].sort_values(ascending=False).index[i]}. The similarity score is {corr[series].sort_values(ascending=False)[i]}')
