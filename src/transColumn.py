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

    def set_cell(i, val):
        self.data[i] = val

    def fill_uniform_rand(self, a = 0, b = 1):
        self.data = np.random.uniform(a,b,len(self.data))

    def fill_normal_rand(self, mu = 0, sigma = 1):
        self.data = np.random.normal(mu, sigma, len(self.data))

    def fill_linear(a, b):
        step = (b - a)/len(self.data)
        self.data = np.linspace(a, b, step)