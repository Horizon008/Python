
person = [
    ["Egor", 23, "programmer", ["films", "driving", "traveling"], {"city": "Syktyvkar", "street": "Kuratov", "house number": 10}],
    ["Anna", 30, "teacher", ["reading", "painting", "hiking"], {"city": "Moscow", "street": "Lenina", "house number": 5}],
    ["Maxim", 25, "engineer", ["gaming", "gardening", "cooking"], {"city": "St. Petersburg", "street": "Pushkin", "house number": 20}],
    ["Olga", 28, "doctor", ["yoga", "dancing", "skiing"], {"city": "Novosibirsk", "street": "Gogol", "house number": 15}],
    ["Darya", 27, "journalist", ["writing", "photography", "travelling"], {"city": "Kazan", "street": "Tolstoy", "house number": 8}],
    ["Vladimir", 35, "architect", ["drawing", "sculpting", "sailing"], {"city": "Vladivostok", "street": "Suvorov", "house number": 12}]
]

oldest_person = ["", 0, "", [], {"city": "", "street": "", "house number": 0}] 

for person in person:
    if person[1] > oldest_person[1]:  
        oldest_person = person  

print("Самый старший человек:", oldest_person[0])

people = {
    "Egor": {"age": 23, "profession": "programmer", "hobbies": ["films", "driving", "traveling"], "address": {"city": "Syktyvkar", "street": "Kuratov", "house number": 10}},
    "Anna": {"age": 30, "profession": "teacher", "hobbies": ["reading", "painting", "hiking"], "address": {"city": "Moscow", "street": "Lenina", "house number": 5}},
    "Maxim": {"age": 25, "profession": "engineer", "hobbies": ["gaming", "gardening", "cooking"], "address": {"city": "St. Petersburg", "street": "Pushkin", "house number": 20}},
    "Olga": {"age": 28, "profession": "doctor", "hobbies": ["yoga", "dancing", "skiing"], "address": {"city": "Novosibirsk", "street": "Gogol", "house number": 15}},
    "Darya": {"age": 67, "profession": "journalist", "hobbies": ["writing", "photography", "travelling"], "address": {"city": "Kazan", "street": "Tolstoy", "house number": 8}},
    "Vladimir": {"age": 35, "profession": "architect", "hobbies": ["drawing", "sculpting", "sailing"], "address": {"city": "Vladivostok", "street": "Suvorov", "house number": 12}}
}

oldest_person_name = ""
oldest_age = 0

for person_name, person_info in people.items():
    if person_info["age"] > oldest_age:  
        oldest_person_name = person_name  
        oldest_age = person_info["age"]  

print("Самый старший человек:", oldest_person_name)
