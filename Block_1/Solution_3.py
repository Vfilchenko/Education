A = int(input('Введите число А '))
B = int(input('Введите число B '))
C = int(input('Введите число C '))

# 1.Дано целое число A. Проверить истинность высказывания: «Число A является положительным».
print(f'Число {A} является положительным? {A>0}')

# 2. Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
print(f'Число {A} является нечетным? {A % 2 != 0}')

# 3. Дано целое число A. Проверить истинность высказывания: «Число A является четным».
print(f'Число {A} является четным? {A % 2 == 0}')

# 4. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3».
print(f'Справедливы неравенства {A}>2 и {B}≤3? {A > 2 and B <= 3}')

# 5. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥ 0 или B < −2».
print(f'Справедливы неравенства {A}≥0 или {B}<−2? {(A >= 0) or (B < -2)}')

# 6. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < _C_».
print(f'Справедливо двойное неравенство {A}<{B}<{C}? {A < B < C}')

# 7. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и _C_».
print(f'Число {B} находится между числами {A} и {C}? {A < B < C}')

# 8. Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».
print(f'Каждое из чисел {A} и {B} нечетное? {A % 2 != 0 and B % 2 != 0}')

# 9. Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».
print(f'Хотя бы одно из чисел {A} и {B} нечетное? {A % 2 != 0 or B % 2 != 0}')

# 10. Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное»
print(f'Ровно одно из чисел {A} и {B} нечетное? {A % 2 != 0 ^ B % 2 != 0}')
