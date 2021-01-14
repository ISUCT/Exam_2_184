import numpy as np
import matplotlib.pyplot as plt
# import math

def calc(a, b, x):
    numerator = np.log((b**2 - x**2) ,a)
    denomerator = abs((x**2 - a**2))**(1/3.0)
    y = numerator/denomerator
    return y

def calc_np(a, b, x):
    numerator = np.log(b**2 - x**2)/np.log(a)
    denomerator = abs((x**2 - a**2))**(1/3.0)
    y = numerator/denomerator
    return y

def task_a_np(a, b, xn, xk, dx):
    x = np.arange(xn, xk, dx)
    y = calc_np(a, b, x)
    return x, y

def task_a(a, b, xn, xk, dx):
    i = xn
    
    res = []
    while i <= xk:
        y = calc(a, b, i)
        res.append((i, y))
        i += dx
    return res

def task_b(a, b, x_arr):
    y = []
    for x in x_arr:
        res = calc(a, b, x)
        y.append(res)
    return y

def draw(x, y):
    fig = plt.plot(x, y, 'rx')
    fig[0].figure.add_axes(xlabel="asdfasdf")
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("My graphics")
    plt.show()

if __name__ == "__main__":
    a = 2.0
    b = 4.1
    x = 0.77
    # y = calc(a, b, x)
    # print(f"x={x:.3f} y={y:.3f}")


    x, y = task_a_np(a, b, 0.77, 1.77, 0.2)
    draw(x, y)
    # print(a_res)

    # x_arr = [1.24, 1.38, 2.38, 3.21, 0.68]
    # b_res = task_b(a, b, x_arr)
    # print(b_res)
