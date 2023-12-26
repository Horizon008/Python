from pprint import pprint
from itertools import product


ADDRESS_WORDS = {'дом', 'улица', 'живет'}
NAME_WORDS = {'имя', 'зовут'}
AGE_WORDS = {'старше', 'младше', 'возраст'}
   
class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)
    
    def fuzzy_compare(self, query):
        q = set(query.split())
        score = 0
        for m, f in zip(
            [ADDRESS_WORDS, NAME_WORDS, AGE_WORDS],
            [self.by_address, self.by_name, self.by_age]
        ):
            if m & q:
                score += f(q)
 
        return score > 0.51
 
    def by_address(self, Q):
        Q = Q - ADDRESS_WORDS
        W = set(self.address.split())
        rez = []
        for a, b in product(Q, W):
            rez.append((self.compare(a, b), a, b))
 
        return max(rez)[0]
 
    def by_age(self, Q):
        q_age = max([self.int_val(q) for q in Q])
        if 'старше' in Q:
            return q_age < self.age
        if 'младше' in Q:
            return q_age > self.age
 
        return q_age + 5 >= self.age >= q_age - 5 
    
    def by_name(self, Q):
        Q = Q - NAME_WORDS
        W = set(self.name.split())
        rez = []
        for a, b in product(Q, W):
            rez.append((self.compare(a, b), a, b))
 
        return max(rez)[0]

    @staticmethod
    def compare(a, b):
        return len(a) / (len(a) + len(b))
    
    @staticmethod
    def int_val(num_str):
        try:
            return int(num_str)
        except ValueError:
            return 0
    
    def __eq__(self, obj):
        if isinstance(obj, Person):
            return self.fuzzy_compare(obj.name) and self.fuzzy_compare(obj.address) and self.fuzzy_compare(str(obj.age))
        elif isinstance(obj, str):
            return self.fuzzy_compare(obj)
        else:
            return False
     
    def __repr__(self):
        return "Person('%s', %s, '%s')" % (self.name, self.age, self.address)
    
if __name__ == '__main__':
    lena = Person("Лена", 19, "Пушкина, 14, 115")
    oleg = Person("Олег", 34, "Ленского, 10, 11")
    olga = Person("Ольга", 28, "Онегина, 11, 12")
    nata = Person("Наташа", 17, "Ростова, 16, 15")
 
    queries = [
            'имя Ольга',
            'возраст 30',
            'старше 20',
            'младше 20',
            'живет на Пушкина',
            'дом 10',
            'фамилия Ростова',
            'зовут нташа',
    ]
 
    people = {
            lena.key: lena,
            oleg.key: oleg,
            olga.key: olga,
            nata.key: nata
    }

    matching_queries = []
    non_matching_queries = []

    for query, person in product(queries, people.values()):
        if person == query:
            matching_queries.append((query, person))
        else:
            non_matching_queries.append((query, person))
            
    print("соответствующие запросы:")
    pprint(matching_queries)
    print("не соответствующие запросы:")
    pprint(non_matching_queries)
