list = [1,2,3,4,5]
# 1. Используя операции индексирования и среза выведите на экран первый и третий элементы списка [1, 2, 3 ,4 ,5], а также срез списка из первых трех элементов.
print(f'{list[0]}  {list[2]}  {list[:3]}')

# 2.Дан список [«Ростов», «+», «на», «-», «Дону»]. Исправьте плюс на дефис и выведите название города на экран использовав доступ к элементам списка по индексам
city_list = ['Ростов','+','на','-','Дону']
city_list[1] = '-'

city = ''
for el in city_list:
    city += str(el)
print(city)

# 3. Дан список [«a», «s», «1», «a», «32», «23»]. Разбейте его на два списка: только с буквами и только с числами.
spisok = ['a','s','1','a','32','23']

l1 = [x for x in spisok if x.islower()]
print(l1)

only_digit = []
for item in spisok:
    if item.isdigit():
        only_digit.append(int(item))
print(only_digit)
