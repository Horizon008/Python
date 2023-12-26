
class Person:
    def __init__(self, name, age, profession, hobbies, address):
        self.name = name
        self.age = age
        self.profession = profession
        self.hobbies = hobbies
        self.address = address

    def __str__(self):
        return f"{self.name} - age: {self.age}, profession: {self.profession}, hobbies: {', '.join(self.hobbies)}, address: {self.address}"

    def get_older(self, years):
        self.age += years
        return f"{self.name} is {self.age} years old."

    def change_profession(self, new_profession):
        previous_profession = self.profession
        self.profession = new_profession
        return f"{self.name} changed profession from {previous_profession} to {self.profession}."


egor = Person("Egor", 23, "programmer", ["films", "driving", "traveling"], {"city": "Syktyvkar", "street": "Kuratov", "house number": 10})
anna = Person("Anna", 30, "teacher", ["reading", "painting", "hiking"], {"city": "Moscow", "street": "Lenina", "house number": 5})
maxim = Person("Maxim", 23, "engineer", ["gaming", "gardening", "cooking"], {"city": "St. Petersburg", "street": "Pushkin", "house number": 20})
olga = Person("Olga", 28, "doctor", ["yoga", "dancing", "skiing"], {"city": "Novosibirsk", "street": "Gogol", "house number": 15})
darya = Person("Darya", 67, "journalist", ["writing", "photography", "travelling"], {"city": "Kazan", "street": "Tolstoy", "house number": 8})
vladimir = Person("Vladimir", 35, "architect", ["drawing", "sculpting", "sailing"], {"city": "Vladivostok", "street": "Suvorov", "house number": 12})

print(egor.get_older(1))
print(anna.change_profession("professor"))
print(maxim.get_older(2))
print(olga.change_profession("surgeon"))
print(darya.get_older(3))
print(vladimir.change_profession("landscape architect"))
