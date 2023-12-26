my_list = []

while len(my_list) < 10:
    new_element = int(input("Введите число: "))
    if len(my_list) == 10:
        print("Достигнуто максимальное количество элементов в списке (10).")
        break
    else:
        my_list.append(new_element)

print("Итоговый список:", my_list)
