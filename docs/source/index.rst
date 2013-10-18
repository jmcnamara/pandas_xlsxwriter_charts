
Using Pandas and XlsxWriter to create Excel charts
==================================================

Contents:

.. toctree::
   :maxdepth: 2


.. code-block:: python

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    excel_file = 'grouped_column_farms.xlsx'
    sheet_name = 'Sheet1'
   
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name, index=True)


.. image:: _images/chart_grouped_column_farms.png
   :scale: 75 %



