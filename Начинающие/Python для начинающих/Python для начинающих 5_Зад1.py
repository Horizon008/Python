people = {
    "Egor": {"age": 23, "profession": "programmer", "hobbies": ["films", "driving", "traveling"], "address": {"city": "Syktyvkar", "street": "Kuratov", "house number": 10}},
    "Anna": {"age": 30, "profession": "teacher", "hobbies": ["reading", "painting", "hiking"], "address": {"city": "Moscow", "street": "Lenina", "house number": 5}},
    "Maxim": {"age": 25, "profession": "engineer", "hobbies": ["gaming", "gardening", "cooking"], "address": {"city": "St. Petersburg", "street": "Pushkin", "house number": 20}},
    "Olga": {"age": 28, "profession": "doctor", "hobbies": ["yoga", "dancing", "skiing"], "address": {"city": "Novosibirsk", "street": "Gogol", "house number": 15}},
    "Darya": {"age": 67, "profession": "journalist", "hobbies": ["writing", "photography", "travelling"], "address": {"city": "Kazan", "street": "Tolstoy", "house number": 8}},
    "Vladimir": {"age": 35, "profession": "architect", "hobbies": ["drawing", "sculpting", "sailing"], "address": {"city": "Vladivostok", "street": "Suvorov", "house number": 12}}
}


def find_person_by_input(people_dict, input_data):
    found_people = []
    for person_name, person_info in people_dict.items():
        for key, value in person_info.items():
            if isinstance(value, list):
                if input_data in value:
                    found_people.append(person_name)
            elif isinstance(value, dict):
                if input_data in value.values():
                    found_people.append(person_name)
            elif str(value) == input_data:
                found_people.append(person_name)
    return found_people

input_data = input("Введите данные для поиска: ")
found_people = find_person_by_input(people, input_data)
if found_people:
    print("Найденные люди:", found_people)
else:
    print("Людей по данным не найдено.")
