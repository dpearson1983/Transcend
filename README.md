# Transcend
A data analysis tool for use in undergraduate laboratories.

## About
This tool was born out of necessity. After overseeing undergraduate physics laboratories for several years, and also asking undergraduate students in 
engineering physics classes to work with Mircrosoft Excel, Google Sheets, LibreOffice Calc, or other spreadsheet software of their choice, there were
far too many situations where that software was woefully inadequate. My biggest gripes: the inability to fit a sinusoidal function to data, the convoluted
nature of least-squares fitting when the data has error bars, the inability to plot a histogram with a probability distribution function curve on the same 
graph, and the difficulty of getting the data for the histogram in addition to the graph.

These are all things that are trivially easy to do in Python, and yet due to the courses I teach being introductory/first year student level, I cannot 
expect, or reasonably require, that they know how to use Python. Hence, the goal of this software is to provide a simple graphical user interface that
functions similarly to a spreadsheet program, but harnesses the data analysis abilities of Python (in the form of the NumPy and SciPy libraries) and the
plotting utilities (MatPlotLib). The GUI will be provided by the PyQt5 library and I hope to provide executables for Windows, MacOS and Linux. The name,
Transcend, is a bit of a jab at Excel, since transcend is a synonym for excel, but also implies going above and beyond, as I hope this program will, at 
least in the realm of scientific data analysis.

## To Do:
This is a running list of items to complete for this program. As of writing, everything still needs to be done, so this is more of an outline as far as
which things to work on first.

1. Decide on all functionality for initial release.
2. Write classes/functions for all functionality.
3. Implement GUI.
