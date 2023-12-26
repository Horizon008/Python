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
    "Egor": Person("Egor", 23, "�����������", ["����", "����������", "�����������"], "���������", "��������", 10),
    "Anna": Person("����", 30, "�������", ["������", "���������", "������"], "������", "������", 5),
    "Maxim": Person("������", 25, "�������", ["����", "�����������", "�������"], "�����-���������", "�������", 20),
    "Olga": Person("�����", 28, "����", ["����", "�����", "����"], "�����������", "������", 15),
    "Darya": Person("�����", 67, "���������", ["������������", "����������", "�����������"], "������", "��������", 8),
    "Vladimir": Person("��������", 35, "����������", ["���������", "����������", "�������� �����"], "�����������", "��������", 12)
}
