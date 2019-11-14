def f_1(a, b, c):
    t = pow(b * b - 4 * a * c, 0.5)
    x1 = (-b + t) / (2 * a)
    x2 = (-b - t) / (2 * a)
    return x1, x2


def f_2(a, b, c):
    t = pow(b * b - 4 * a * c, 0.5)
    x1 = (-2 * c) / (b + t)
    x2 = (-2 * c) / (b - t)
    return x1, x2


l = [[1, 2, 1],
     [1, 2.000000001, 1],
     [1, 1000000.1, 1],
     [1, -1000000, 1]]

for k in l:
    if k[1]<0:
        print(f_2(k[0],k[1],k[2]))
    else:
        print(f_1(k[0], k[1], k[2]))
