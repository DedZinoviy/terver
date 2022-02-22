import numpy as np

class Combinatoric:
    """Класс для работы с основными формулми комбинаторики"""
    def __init__(self):
        pass

     
    def combinations_without_repeats(n, m):
        '''Вычислить число сочетаний без повторений'''
        arr = [m, n-m]     # определить основания факториалов в знаменателе
        maximum = max(arr) # определить максимум из оснований факториалов знаменателя
        minimum = min(arr) # определить минимум из оснований факториалов знаменателя

        # Определить число сочетаний. В числителе n!, сокращенный на факториал максимума, в знаменателе факториал минимума 
        result = np.prod(np.arange(maximum + 1, n + 1, 1, dtype=np.object)) // np.math.factorial(minimum)     
        return result


    def combinations_with_repeats(n, m):
        '''Вычислить число сочетаний с повторениями'''
        n = n + m - 1                                            # переопределить n для перехода к формуле сочетаний
        result = Combinatoric.combinations_without_repeats(n, m) # определить число сочетаний для нового значения n
        return result


    def accommodation_with_repeats(n, m):
        '''Вычислить число размещений с повторениями'''
        return n**m

    def accomodation_without_repeats(n, m):
        '''Вычислить число размещений без повторений'''
        denominator = n - m
        result = np.prod(np.arange(denominator + 1, n + 1, 1, dtype=np.object))
        return result
