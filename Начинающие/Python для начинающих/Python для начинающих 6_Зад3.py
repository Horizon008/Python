from fuzzywuzzy import process

class Person:
    def __init__(self, name, age, occupation, interests, city, street, number):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.interests = interests
        self.city = city
        self.street = street
        self.number = number

people_data = {
    "Egor": Person("Egor", 28, "программист", ["кино", "автомобили", "путешествия"], "Сыктывкар", "Куратова", 10),
    "Anna": Person("Anna", 30, "учитель", ["чтение", "рисование", "походы"], "Москва", "Ленина", 5),
    "Max": Person("Max", 25, "инженер", ["игры", "садоводство", "готовка"], "Санкт-Петербург", "Пушкина", 20),
    "Olga": Person("Olga", 28, "врач", ["йога", "танцы", "лыжи"], "Новосибирск", "Гоголя", 15),
    "Darya": Person("Darya", 26, "журналист", ["писательство", "фотография", "путешествия"], "Казань", "Толстого", 8),
    "Vladimir": Person("Vladimir", 35, "архитектор", ["рисование", "скульптура", "парусный спорт"], "Владивосток", "Суворова", 12)
}

def find_person(name):
    if name in people_data:
        return people_data[name]
    else:
        matches = process.extractBests(name, people_data.keys(), score_cutoff=70)
        for match, score in matches:
            if score >= 70:
                return people_data[match]
    return None

input_name = input("Введите имя: ")
result_person = find_person(input_name)
if result_person:
    print(f"Найдена информация о {result_person.name}: возраст - {result_person.age}, профессия - {result_person.occupation}, интересы - {result_person.interests}, город - {result_person.city}, улица - {result_person.street}, номер - {result_person.number}")
else:
    print("Информация не найдена")