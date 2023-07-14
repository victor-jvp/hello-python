### File Handling ###

import csv
import json
import os

# .txt file
txt_file = open("Intermediate/myfile.txt", "w+")  # Leer y Escribir
txt_file.write(
    "Mi nombre es Victor\nMi apellido es Veliz\nMi edad es 33 years\nMi lenguaje favorito es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque me gusta JS")
print(txt_file.readline())

txt_file.close()
# os.remove("Intermediate/myfile.txt")

# .json file


json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Victor",
    "surname": "Veliz",
    "age": 33,
    "language": [
        "Python", "JavaScript", "PHP", "C#"
    ],
    "website": "https://victor-jvp.github.io"
}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["language"])

# .csv file


csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file, delimiter=";")
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Victor", "Veliz", 35, "Python",
                    "https://victor-jvp.github.io"])
csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
