import numpy as np
from scipy import stats as st

class column:
    def __init__(self, name, N):
        self.name = name
        self.data = np.empty(N)
        self.mean = 0
        self.mode = 0
        self.median = 0
        self.stdev = 0

    def statistics(self):
        self.mean = np.average(self.data)
        self.mode = st.mode(self.data)
        self.median = np.median(self.data)
        self.stdev = np.std(self.data)


