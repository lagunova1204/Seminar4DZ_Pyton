# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12


n = int(input("Введите количество N элементов: "))
num_list_1 = [0]*n
for i in range (len(num_list_1)):
    num_list_1[i] = int(input(f"Введите {i} элемент списка: "))

m = int(input("Введите количество M элементов: "))
num_list_2 = [0]*m
for i in range (len(num_list_2)):
    num_list_2[i] = int(input(f"Введите {i} элемент списка: "))   

num_list3 = []
for item in num_list_1:
    if item in num_list_2 and item not in num_list3:
        num_list3.append(item)
for item in num_list3:
    if num_list_1.count(item) > num_list3.count(item) and num_list_2.count(item) > num_list3.count(item):
        a = min(num_list_1.count(item), num_list_2.count(item))
        for i in range(a-1):
            num_list3.append(item)
print(sorted(num_list3))