class Person: 
    def __init__(self,name,wealth):# ������ ���� ������� ������ ����� ����� ����� �������
        self.name=name 
        self.wealth=wealth
people=[ # ������ ���� ��������� 2 ��������
    Person("Bob", 1500),
    Person("Charlie", 3200),
    Person("Diana", 2800)
]

def richest_people(people_list):
    max_wealth=max(person.wealth for person in people_list) # 1) ������� ������ ����� �����; 2) ���������� ������ ���� � snake_case
    richest=[p for p in people_list if p.wealth==max_wealth] # ������� ������ == � =
    return richest

wealthiest=richest_people(people)
for w in wealthiest:
    print(f"{w.name} is one of the richest with a wealth of ${w.wealth}.")
