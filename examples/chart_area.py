##############################################################################
#
# An example of creating a chart with Pandas and XlsxWriter.
#
# Copyright 2013, John McNamara, jmcnamara@cpan.org
#

import pandas as pd

# Some sample data to plot.
list_data = [10, 20, 30, 20, 15, 30, 45]

# Create a Pandas dataframe from the data.
df = pd.DataFrame(list_data)

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'area.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'area'})

# Configure the series of the chart from the dataframe data.
chart.add_series({
    'categories': ['Sheet1', 1, 0, 7, 0],
    'values':     ['Sheet1', 1, 1, 7, 1],
})

# Configure the chart axes.
chart.set_x_axis({'name': 'Index', 'position_axis': 'on_tick'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})

# Turn off chart legend. It is on by default in Excel.
chart.set_legend({'position': 'none'})

# Insert the chart into the worksheet.
worksheet.insert_chart('D2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
