import numpy as np

class Combinatoric:
    def __init__(self):
        pass

    def multiplection(self, start, finish):
        mult = start
        for i in range(start + 1, finish + 1, 1):
            mult = mult * i
        return mult


    def combinations_without_repeats(self, n, m):
        if n == m:
            result = n
        else:
            arr = [m, n-m]
            maximum = max(arr)
            minimum = min(arr)
            result = self.multiplection(maximum + 1, n) // np.math.factorial(minimum)
        
        return result


    def combinations_with_repeats(self, n, m):
        n = n + m - 1
        result = self.combinations_without_repeats(n, m)
        return result


    def accommodation_with_repeats(self, n, m):
        return n**m

