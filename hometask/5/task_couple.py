from mimesis import Person
from mimesis.enums import Gender
from random import randint

class Candidate:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def match(self, name, age):
        return abs(self.age - age) <= 5 and len(set(list(self.name)) & set(list(name))) >= 2

    def __str__(self):
       return f"name: {self.name}\n age: {self.age}"

class Generator:
    GENDERS = [Gender.MALE, Gender.FEMALE]
    @staticmethod
    def create():
        person = Person('en')
        random_people = []
        for _ in range(0, 10):
            random_number = randint(1, 10)
            sex = Generator.GENDERS[random_number % 2]
            new_candidate = Candidate(person.full_name(sex), sex, person.age())
            random_people.append(new_candidate)
        return random_people

list_random = Generator.create()
for i in list_random:
    print(i)
name_user = input('\nTo find a couple, enter your name ')
desired_age = int(input('enter desired age '))
contact_found = None
for i in list_random:
    if i.match(name_user, desired_age):
        contact_found = i
        break
if contact_found is None:
    print('Sorry, no match!')
else:
    print(f'Congrats there is a matching pair {name_user} + {contact_found.name}!')




