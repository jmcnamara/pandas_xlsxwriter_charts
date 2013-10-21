##############################################################################
#
# An example of creating an Excel file with Pandas and XlsxWriter.
#
# Copyright 2013, John McNamara, jmcnamara@cpan.org
#

import pandas as pd


# Create a Pandas dataframe from the data.
df = pd.DataFrame([10, 20, 30, 20, 15, 30, 45])

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
