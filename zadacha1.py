a = input('Введите число a: ')
b = input('Введите число b: ')
c = input('Введите число c: ')
a = float(a)
b = float(b)
c = float(c)
D = b**2 - 4*a*c
if D < 0:
    print('Корней нет')
elif D == 0:
    x = -b/2*a1
    print(x)
else:
    x1 = (-b + D**0.5)/2*a
    x2 = (-b - D**0.5)/2*a
    print(x1, x2)
