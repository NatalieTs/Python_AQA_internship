from mimesis import Person
from random import randint

# Write a program that will create a list of people with name, age, height, and weight
# Sort the list of people by age


class Someone:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"name: {self.name}\n age: {self.age}\n height: {self.height}\n weight: {self.weight}"

class PeopleList:
    @staticmethod
    def create():
        person = Person('en')
        list_people = []
        for _ in range(0, 10):
            random_weight = randint(30, 100)
            new_people = Someone(person.name(), person.age(), person.height(), random_weight)
            list_people.append(new_people)
        return list_people

list_result = PeopleList.create()
list_result.sort(key=lambda x: x.age)
for i in list_result:
    print(i)





