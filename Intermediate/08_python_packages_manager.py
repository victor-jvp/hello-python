### Python Packages ###

# pip https://pypi.org

import requests
import pandas  # pip install pandas
import numpy  # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)


# pip list
# pip uninstall pandas


# response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
# print(response)
# print(response.status_code)
# print(response.json())

# Aritmethics Package

from mypackage.arithmetics import suma

print(suma(1, 4))
