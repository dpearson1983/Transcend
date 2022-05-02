import numpy as np
from src.transColumn import column

class sheet:
    def __init__(self, columns=2, rows = 1000000, names = ['x','y']):
        self.table = []
        for i in range(0,columns):
            col = column(names[i], rows)
            self.table.append(col)
