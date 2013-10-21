Using Pandas and XlsxWriter to create Excel charts
==================================================

An introduction to the creation of Excel files with charts using [Pandas](<http://pandas.pydata.org) and [XlsxWriter](http://xlsxwriter.readthedocs.org).

```python

    import pandas as pd

    ...

    writer = pd.ExcelWriter('farm_data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    chart = workbook.add_chart({'type': 'column'})

    ...
```

![Chart image](https://raw.github.com/jmcnamara/pandas_xlsxwriter_charts/master/docs/source/_images/chart_grouped_column_farms.png)

See the full document at [ReadTheDocs](http://pandas-xlsxwriter-charts.readthedocs.org/en/latest/).


