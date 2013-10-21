##############################################################################
#
# An example of creating a chart with Pandas and XlsxWriter.
#
# Copyright 2013, John McNamara, jmcnamara@cpan.org
#

import random
import pandas as pd
from vincent.colors import brews

# Some sample data to plot.
cat_2 = ['y' + str(x) for x in range(1, 9)]
index_2 = range(1, 21, 1)
multi_iter2 = {'index': index_2}
for cat in cat_2:
    multi_iter2[cat] = [random.randint(10, 100) for x in index_2]

# Create a Pandas dataframe from the data.
index_2 = multi_iter2.pop('index')
df = pd.DataFrame(multi_iter2, index=index_2)
df = df.reindex(columns=sorted(df.columns))

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'stacked_area2.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'area', 'subtype': 'stacked'})

# Configure the series of the chart from the dataframe data.
max_row = len(df)
for i in range(len(cat_2)):
    col = i + 1
    chart.add_series({
        'name':       ['Sheet1', 0, col],
        'categories': ['Sheet1', 1, 0, max_row, 0],
        'values':     ['Sheet1', 1, col, max_row, col],
        'fill':       {'color': brews['Spectral'][i]},
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Index'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})

# Insert the chart into the worksheet.
worksheet.insert_chart('K2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
