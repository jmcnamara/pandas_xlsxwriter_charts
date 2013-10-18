
Using Pandas and XlsxWriter to create Excel charts
==================================================

This is an introduction on how to create Excel files with beautiful charts
using `Pandas <http://pandas.pydata.org>`_ and
`XlsxWriter <http://xlsxwriter.readthedocs.org>`_.

.. code-block:: python

    import pandas as pd
    
    ... 
    
    excel_file = 'grouped_column_farms.xlsx'
    sheet_name = 'Sheet1'
   
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name, index=True)

    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
   
    chart = workbook.add_chart({'type': 'column'})
    
    ...

.. image:: _images/chart_grouped_column_farms.png

The charts in these examples are heavily influenced by the output of
`Vincent <http://vincent.readthedocs.org>`_, a data visualisation tool that
also integrates with Pandas.


Contents:

.. toctree::
   :maxdepth: 2

   introduction.rst
   chart_examples.rst
   code_examples.rst
   learn_more.rst



