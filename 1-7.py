def f_11(a, b, c):
    t = pow(b * b - 4 * a * c, 0.5)
    x1 = (-b + t) / (2 * a)
    return x1

def f_12(a, b, c):
    t = pow(b * b - 4 * a * c, 0.5)
    x2 = (-b - t) / (2 * a)
    return x2


def f_21(a, b, c):
    t = pow(b * b - 4 * a * c, 0.5)
    x1 = (-2 * c) / (b + t)
    return x1

def f_22(a, b, c):
    t = pow(b * b - 4 * a * c, 0.5)
    x2 = (-2 * c) / (b - t)
    return x2



l = [[1, -1000.001, 1],
     [1, -10000.0001, 1],
     [1, -100000.00001, 1],
     [1, -1000000.000001, 1]]

for k in l:
    if k[1]<0:
        print(f_21(k[0],k[1],k[2]),f_12(k[0],k[1],k[2]))
    else:
        print(f_11(k[0], k[1], k[2]), f_22(k[0], k[1], k[2]))

