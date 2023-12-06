import math

a = float(input('Введите значение a '))
b = float(input('Введите значение b '))
c = float(input('Введите значение c '))
d = float(input('Введите значение d '))
r = float(input('Введите значение r '))
pi = math.pi
pi = float(round(pi,2))

def perimetr (a): #периметр квадрата со стороной а
    return a * 4

def squre (a): #площадь квадрата со стороной а
    return a ** 2

def circumference (d): #длина окружности диаметром d
    l = pi * d
    l = round(l,2)
    return l

def cub_volume (a): #объем куба со стороной а
    return a ** 3

def parallepiped_v (a,b,c): #объем параллепипеда
    return a * b * c

def parallepiped_s (a,b,c): #площадь параллепипеда
    return 2 * (a * b + b * c + a * c)

def circle_L (r): #длина окружности радиусом r
    l = 2 * pi * r
    l = round(l,2)
    return l

def circle_S (r): #площадь окружности радиусом r
    s = pi * (r ** 2)
    return s

def average (a,b): #среднее арифметическое а и b
    list_1 = {a , b}
    return sum(list_1)/len(list_1)

def root_of_a_number (a,b): #корень произведения а и b (среднее геометрическое)
    root_ab = a * b
    return math.sqrt(root_ab)

print (f'Периметр квадрата со стороной {a} = {perimetr(a)}')
print (f'Площадь квадрата со стороной {a} = {squre(a)}')
print (f'Длина окружности диаметром {d} = {circumference(d)}')
print (f'Объем куба со стороной {a} = {cub_volume(a)}')
print (f'Объем параллелипипеда со сторонами {a},{b},{c} = {parallepiped_v(a,b,c)}')
print (f'Площадь параллелипипеда со сторонами {a},{b},{c} = {parallepiped_s(a,b,c)}')
print (f'Длина окружности радиусом {r} = {circle_L(r)}')
print (f'Площадь окружности радиусом {r} = {circle_S(r)}')
print (f'Среднее арифметическое {a} и {b} = {average(a,b)}')
print (f'Среднее геометрическое {a} и {b} = {root_of_a_number(a,b)}')

num_1 = float(input('Введите неотрицательное число '))**2
num_2 = float(input('Введите еще неотрицательное число '))**2

print(f'сумма {num_1} и {num_2} = {num_1 + num_2}')
print(f'разность {num_1} и {num_2} = {num_1 - num_2}')
print(f'произведение {num_1} и {num_2} = {num_1 * num_2}')
print(f'частное {num_1} и {num_2} = {num_1 / num_2}')



