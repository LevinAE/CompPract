import math
#Метод Дихотомии
def example(x):
    return x*math.exp(x)-x-1
def metod_dihotomii(f, a, b, epsilon):
    if f(a) * f(b) > 0:
        return None
    iter = 0
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        iter +=1
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"Количество итераций: {iter}")
    return (a + b) / 2

a=0 #левый край
b=3 #правый край
epsilon=10**(-6) #точность
root = metod_dihotomii(example, a, b, epsilon)
print(f"Решение уравнения: x = {root}")
lol=example(root)
print(f"Значение функции: f({root})=",lol)

