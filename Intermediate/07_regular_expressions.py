### Regular Expressions ###

import re

# match

my_string = "Esta es la leccion numero 7: Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de Ficheros"

match = re.match("Esta es la leccion", my_string)
if not match == None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

# split

print(re.split(" ", my_string))

# sub

print(re.sub("[E|e]xpresiones", "expresiones", my_string))
