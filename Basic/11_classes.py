### Classess ###

class MyEmptyPerson:
    pass


# print(MyEmptyPerson)
# print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} Esta Caminando")


my_person = Person("Victor", "Veliz")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Victor", "Veliz", "vveliz")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Victor Veliz (victor-jvp)"
print(my_other_person.full_name)


print("string".upper())
print("string"[])