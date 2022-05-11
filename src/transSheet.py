import numpy as np
from src.transColumn import column

class sheet:
    def __init__(self, columns=2, rows = 1000000, names = ['x','y']):
        self.table = []
        for i in range(0,columns):
            col = column(names[i], rows)
            self.table.append(col)

    def set_equation(col_name, eq_str):
        # Use the built in eval, but first parse column names used in equation
        # USe globals(), local(), or exec() to set variable names from the stored column names