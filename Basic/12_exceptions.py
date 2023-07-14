### Exceptions Handling ###

numberOne, numberTwo = 5, 1
numberTwo = "1"

# try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # se ejecuta si se produce una exception
    print("Se ha producido un error")


# try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # se ejecuta sino se produce una exception
    print("La ejecucion continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")

# Excepctions por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    # se ejecuta si se produce una exception
    print("Se ha producido un error")


# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
