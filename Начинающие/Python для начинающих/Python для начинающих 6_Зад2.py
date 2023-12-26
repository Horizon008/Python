class Person:
    def __init__(self, name, age, profession, hobbies, city, street, house_number):
        self.name = name
        self.age = age
        self.profession = profession
        self.hobbies = hobbies
        self.address = {
            "city": city,
            "street": street,
            "house_number": house_number
        }

    @staticmethod
    def search_by_field(people, search_criteria):
        results = []
        for person in people.values():
            matches_criteria = False
            for key, value in person.__dict__.items():
                if str(value).lower() == search_criteria.lower():
                    results.append(person)
                    matches_criteria = True
                    break
            if not matches_criteria:
                for value in person.address.values():
                    if str(value).lower() == search_criteria.lower():
                        results.append(person)
                        break
        return results

people_data = {
    "Egor": Person("Egor", 23, "программист", ["кино", "автомили", "путешествия"], "Сыктывкар", "Куратова", 10),
    "Anna": Person("Анна", 30, "учитель", ["чтение", "рисование", "походы"], "Москва", "Ленина", 5),
    "Maxim": Person("Максим", 25, "инженер", ["игры", "садоводство", "готовка"], "Санкт-Петербург", "Пушкина", 20),
    "Olga": Person("Ольга", 28, "врач", ["йога", "танцы", "лыжи"], "Новосибирск", "Гоголя", 15),
    "Darya": Person("Дарья", 67, "журналист", ["писательство", "фотография", "путешествия"], "Казань", "Толстого", 8),
    "Vladimir": Person("Владимир", 35, "архитектор", ["рисование", "скульптура", "парусный спорт"], "Владивосток", "Суворова", 12)
}

search_criteria = input("Введите критерий поиска: ")
results = Person.search_by_field(people_data, search_criteria)
for person in results:
    print(person.name)
