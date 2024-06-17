import math
#Метод касательных
def example_function(x):
    return x**3 - 0.2*x*x + 0.5*x - 1

#Производная
def derivative_example_function(x):
    return 3 * x ** 2 - 0.4*x + 0.5

def tangent_method(f, df, x0, epsilon, max_iter):
    x = x0
    for i in range(max_iter):
        f_x = f(x)
        f_derivative = df(x)
        x_new = x - f_x / f_derivative

        if abs(x_new - x) < epsilon:
            return x_new, i + 1
        x = x_new

    return None, max_iter

x0 = 1  #начальное значение
epsilon = 10**(-6) #точность
max_iter=100 # число итераций
root, iterations = tangent_method(example_function, derivative_example_function, x0, epsilon, max_iter)

print(f"Корень уравнения: {root:.12f}")
print(f"Количество итераций: {iterations}")
lol=example_function(root)
print(f"Значение функции: f({root})=",lol)