from __future__ import division, print_function
import numpy as np
import pandas as pd
data = pd.read_csv('2016-first-quarter-citations.csv')
data = data.dropna(how='any')
data.shape
data['DateTime Issued'] = data.apply(lambda row: datetime.strptime(row['Date Issued'] + ':' + row['Time Issued'], '%m/%d/%y:%I:%M %p'), axis=1)
data['Day of Week Issued'] = data.apply(lambda row: datetime.strftime(row['DateTime Issued'], '%A'), axis=1)
ages = data['Cited Person Age']
bin_size = (np.max(ages) - np.min(ages))/100
age_list = []
for i in range(100):
    if i == 99:
        age_list.append((len(ages[(ages >= i+16) & (ages <= i+17)]), i+16 , i+17))
    else:
        age_list.append((len(ages[(ages >= i + 16) & (ages < i + 17)]), i + 16, i + 17))

age_list
import pygal as pg
hist = pg.Histogram()
hist.add('Age Histogram',age_list)
hist.render_to_file('hist_chart.svg')

