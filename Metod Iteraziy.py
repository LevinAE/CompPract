from math import *
import math
#Метод итераций
def example_function(x):
    return x*math.exp(x) - x - 1
def simple_iteration_method(a,b):
    eps = 10**(-6)
    xm = (a+b) / 2
    count_iter = 0
    while (abs(example_function(xm)) > eps):
        if (example_function(a) * example_function(xm) < 0):
            b =xm
        if (example_function(xm) * example_function(b) < 0):
            a = xm
        xm = (a + b) / 2
        count_iter = count_iter + 1
    print('Kol-vo iteraziy:', count_iter)
    return round(xm, 8)

print('Reshenie: ', simple_iteration_method(0, 3))