import math

from scipy import integrate


def f(x):
    t = 1 / pow(2 * math.pi, 0.5)
    return t * pow(math.e, (-0.5 * x * x))


truevalue, e = integrate.quad(f, 0, 1)

print(truevalue)

n1 = 1000
n2 = 1000


# n % 2 ==0
def Simpson(a=0, b=1, n=n1):
    h = (b - a) / n
    fx = []
    for i in range(n + 1):
        fx.append(f(a + h * i))
    res = 0
    for i in range(n + 1):
        if i == 0:
            res += fx[i]
            continue
        if i == n:
            res += fx[i]
            continue
        if i % 2 == 0:
            res += 2 * fx[i]
        if i % 2 == 1:
            res += 4 * fx[i]
    res = res * h / 3
    error = truevalue - res
    return res, error


def Compsite(a=0, b=1, n=n2):
    h = (b - a) / n
    fx = []
    for i in range(n + 1):
        fx.append(f(a + h * i))
    res = 0
    for i in range(n + 1):
        if i == 0:
            res += fx[i]
            continue
        if i == n:
            res += fx[i]
            continue
        res += 2 * fx[i]
    res = res * h / 2
    error = truevalue - res
    return res, error


print('SIMPSON', Simpson())
print('Compsite', Compsite())

error0 = 1e-4


def find1(a=0, b=1, error=error0):
    res = 0
    for i in range(10, 1000):
        v, e = Simpson(a=a, b=b, n=i)
        if abs(e) < error:
            res = i
            break
    h = (b - a) / res
    n = res
    return h, n


def find2(a=0, b=1, error=error0):
    res = 0
    for i in range(10, 1000):
        v, e = Compsite(a=a, b=b, n=i)
        if abs(e) < error:
            res = i
            break
    h = (b - a) / res
    n = res
    return h, n


print(find1())
print(find2())
