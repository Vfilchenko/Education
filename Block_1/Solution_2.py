# 1. Дано расстояние L в сантиметрах. Используя операцию деления нацело, найти количество полных метров в нем (1 метр = 100 см).
# 2.Дана масса M в килограммах. Используя операцию деления нацело, найти количество полных тонн в ней (1 тонна = 1000 кг).
# 3. Дан размер файла в байтах. Используя операцию деления нацело, найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).
L = int(input('Введите расстояние L в см '))
M = int(input('Введите массу M в кг '))
size_b = int(input('Введите размер файла в байтах '))

print (f'В {L} см {L // 100} м')
print (f'В {M} кг {M // 1000} т')
print(f'В {size_b} байтах {size_b // 1024} кб')

# 4. Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.
# 5. Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.
A = int(input('Введите положительное число А '))
if A > 0 :
    B = int(input('Введите число B < А '))
    if A > B:
        print(f'На участке длиной {A} размещено {A // B} участков длиной {B}')
        print(f'оставшааяся незанятая длина участка {A} составляет {A % B}')
    else:
        print(f'Число В слишком велико')
else:
    print(f'необходимо положительное число')

num_2 = int(input('Введите двузначное число '))
# 6. Вывести вначале его левую цифру, а затем правую
print(f'Левая цифра {num_2 // 10} правая цифра {num_2 % 10}')

# 7. Найти сумму и произведение цифр
print(f'Сумма цифр {(num_2 % 10)+(num_2 // 10)} произведение цифр {(num_2 % 10)*(num_2 // 10)}')

# 8. Вывести число, полученное при перестановке цифр
print(f'Число при перестановке цифр {num_2 % 10}{num_2 // 10}')

num_3 = int(input('Введите трехзначное число '))
# 9. Вывести первую цифру данного трехзначного числа
print(f'Первая цифра {num_3 // 100}')

# 10. Вывести вначале его последнюю цифру, а затем - среднюю
print(f'Последняя цифра {num_3 % 10} средняя цифра {(num_3 // 10)%10}')





