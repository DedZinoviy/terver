import numpy as np

class Combinatoric:
    def __init__(self):
        pass


    def combinations_without_repeats(self, n, m):
        arr = [m, n-m]
        maximum = max(arr)
        minimum = min(arr)
        result = np.prod(np.arange(maximum + 1, n + 1, 1, dtype=np.object)) // np.math.factorial(minimum)     
        return result


    def combinations_with_repeats(self, n, m):
        n = n + m - 1
        result = self.combinations_without_repeats(n, m)
        return result


    def accommodation_with_repeats(self, n, m):
        return n**m

