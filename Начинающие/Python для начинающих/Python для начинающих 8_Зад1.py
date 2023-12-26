class Person: 
    def __init__(self,name,wealth):# должны быть пробелы вокруг знака равно после запятой
        self.name=name 
        self.wealth=wealth
people=[ # должны быть разделены 2 строками
    Person("Bob", 1500),
    Person("Charlie", 3200),
    Person("Diana", 2800)
]

def richest_people(people_list):
    max_wealth=max(person.wealth for person in people_list) # 1) пробелы вокруг знака равно; 2) переменные должны быть в snake_case
    richest=[p for p in people_list if p.wealth==max_wealth] # пробелы вокруг == и =
    return richest

wealthiest=richest_people(people)
for w in wealthiest:
    print(f"{w.name} is one of the richest with a wealth of ${w.wealth}.")
