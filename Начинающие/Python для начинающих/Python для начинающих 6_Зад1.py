class Person:
    def __init__(self, name, age, profession, hobbies, city, street, house_number):
        self.name = name
        self.age = age
        self.profession = profession
        self.hobbies = hobbies
        self.address = {
            "city": city,
            "street": street,
            "house number": house_number
        }

people_data = {
    "Egor": Person("Egor", 23, "программист", ["кино", "автомобили", "путешествия"], "Сыктывкар", "Куратова", 10),
    "Anna": Person("Анна", 30, "учитель", ["чтение", "рисование", "походы"], "Москва", "Ленина", 5),
    "Maxim": Person("Максим", 25, "инженер", ["игры", "садоводство", "готовка"], "Санкт-Петербург", "Пушкина", 20),
    "Olga": Person("Ольга", 28, "врач", ["йога", "танцы", "лыжи"], "Новосибирск", "Гоголя", 15),
    "Darya": Person("Дарья", 67, "журналист", ["писательство", "фотография", "путешествия"], "Казань", "Толстого", 8),
    "Vladimir": Person("Владимир", 35, "архитектор", ["рисование", "скульптура", "парусный спорт"], "Владивосток", "Суворова", 12)
}
