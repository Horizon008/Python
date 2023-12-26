my_list = []

while True:
    new_element = int(input("Введите число: "))
    if new_element in my_list:
        print("Этот элемент уже присутствует в списке. Пожалуйста, введите другое число.")
    else:
        my_list.append(new_element)

print("Итоговый список с уникальными элементами:", my_list)
