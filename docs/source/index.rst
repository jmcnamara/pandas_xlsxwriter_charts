
Using Pandas and XlsxWriter to create Excel charts
==================================================

An introduction to the creation of Excel files with charts using
`Pandas <http://pandas.pydata.org>`_ and
`XlsxWriter <http://xlsxwriter.readthedocs.org>`_.

.. code-block:: python

    import pandas as pd
    
    ... 
   
    writer = pd.ExcelWriter('farm_data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
   
    chart = workbook.add_chart({'type': 'column'})
    
    ...

.. image:: _images/chart_grouped_column_farms.png

The charts in this document are heavily influenced by the output of
`Vincent <http://vincent.readthedocs.org>`_ a data visualisation tool that is
also integrated with Pandas.


Contents:

.. toctree::
   :maxdepth: 2

   introduction.rst
   pandas.rst
   chart_examples.rst
   code_examples.rst
   learn_more.rst



