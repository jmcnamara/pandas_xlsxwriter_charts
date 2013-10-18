#
# Simple Makefile for the pandas_xlsxwriter_charts project.
#

.PHONY: docs

html: docs

docs:
	@make -C docs html

pdf:
	@make -C docs latexpdf

clean:
	@make -C docs clean
