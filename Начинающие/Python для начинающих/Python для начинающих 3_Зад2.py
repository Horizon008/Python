people = {
    "Egor": {"age": 23, "profession": "programmer", "hobbies": ["films", "driving", "traveling"], "address": {"city": "Syktyvkar", "street": "Kuratov", "house number": 10}},
    "Anna": {"age": 30, "profession": "teacher", "hobbies": ["reading", "painting", "hiking"], "address": {"city": "Moscow", "street": "Lenina", "house number": 5}},
    "Maxim": {"age": 25, "profession": "engineer", "hobbies": ["gaming", "gardening", "cooking"], "address": {"city": "St. Petersburg", "street": "Pushkin", "house number": 20}},
    "Olga": {"age": 28, "profession": "doctor", "hobbies": ["yoga", "dancing", "skiing"], "address": {"city": "Novosibirsk", "street": "Gogol", "house number": 15}},
    "Darya": {"age": 67, "profession": "journalist", "hobbies": ["writing", "photography", "travelling"], "address": {"city": "Kazan", "street": "Tolstoy", "house number": 8}},
    "Vladimir": {"age": 35, "profession": "architect", "hobbies": ["drawing", "sculpting", "sailing"], "address": {"city": "Vladivostok", "street": "Suvorov", "house number": 12}}
}
while True:
    input_text = input("Введите имя человека")
    if input_text.lower() == 'выход':
        print("Программа завершена.")
        break
    if input_text in people:
        person = people[input_text]
        print(f"Имя: {input_text}")
        print(f"Возраст: {person['age']}")
        print(f"Профессия: {person['profession']}")
        print(f"Адрес: {person['address']['city']}, улица {person['address']['street']}, дом {person['address']['house number']}")
        print(f"Хобби: {', '.join(person['hobbies'])}")
    else:
        print("Такого человека в списке нет.")