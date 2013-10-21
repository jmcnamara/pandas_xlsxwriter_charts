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
cat_4 = ['Metric_' + str(x) for x in range(1, 9)]
index_4 = ['Data 1', 'Data 2', 'Data 3', 'Data 4']
data_3 = {}
for cat in cat_4:
    data_3[cat] = [random.randint(10, 100) for x in index_4]

# Create a Pandas dataframe from the data.
df = pd.DataFrame(data_3, index=index_4)

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'grouped_column.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name, index=True)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'column'})

# Configure the series of the chart from the dataframe data.
for col_num in range(1, len(cat_4) + 1):
    chart.add_series({
        'name':       ['Sheet1', 0, col_num],
        'categories': ['Sheet1', 1, 0, 4, 0],
        'values':     ['Sheet1', 1, col_num, 4, col_num],
        'fill':       {'color': brews['Spectral'][col_num - 1]},
        'gap':        300,
    })

# Configure the chart axes.
chart.set_y_axis({'major_gridlines': {'visible': False}})

# Insert the chart into the worksheet.
worksheet.insert_chart('K2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
