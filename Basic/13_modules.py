### Modules ###

import my_module

my_module.sumValue(1, 4, 6)
my_module.printValue("Hola mundo")

from my_module import sumValue, printValue

sumValue(1, 4, 6)
printValue("Hola mundo")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)