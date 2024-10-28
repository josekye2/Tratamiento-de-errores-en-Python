num1 = 20
num2 = 0

try:
    print("La division de {0} entre {1}".format(num1, num2,(num1/num2)))
    result = num1/num2

except ZeroDivisionError:
    print("Error en la ejecución del programa")


print("Hasta aqui va el programa")