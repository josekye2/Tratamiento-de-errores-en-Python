print("Sistema para calcular el promedio de notas de un estudiante")

name = input("digitar el nombre del estudiante ")

Nota1= float(input(name + " digita nota1: "))
Nota2= float(input(name + " digita nota2: "))
Nota3= float(input(name + " digita nota3: "))

prom = (Nota1+Nota2+Nota3)/3

if prom >= 3:
    print("felicitaciones " + name + ' Aprobaste y tu promedio es:', prom)
else:
    print("lo sentimos " + name + ' desaprobaste y tu promedio es:', prom)
print("fin")

#uso de elif

X = 2

if X == 5:
    print("El numnero es 5")
elif X == 6:
    print("El numero es 6")
elif X == 7:
    print("El numero es 7")
else:
    print("El numero no existe")

#CONVERSOR

num_1 = int(input("Cual es el numero que desea convertir?"))

if num_1 == 5:
    print("El numnero es 'CINCO'")
elif num_1 == 6:
    print("El numero es 'SEIS'")
elif num_1 == 7:
    print("El numero es 'SIETE'")
else:
    print("El numero no está registrado")

#MENU 1

menu = """Bienvenidos al registro de usuarios, llene los campos que usted prefiera
acontinuación selecciona la opción del 1 al 3:
[1] Digitar nombre
[2] Digitar edad
[3] Digitar email
"""
print(menu)
opcion = input("Digite una opción entre 1 y 3:")
if opcion == "1":
    pass
elif opcion == "2":
    pass
elif opcion == "3":
    pass
else:
    print("debe digitar un numero entre 1 y 3")

# convertir cadena a minus
cadena = "Hola Jose"
print(cadena.lower())

# convertir cadena a mayus
cadena = "Hola Jose"
print(cadena.upper())

# convertir mayus a minus y viceversa
cadena = "Hola Jose"
print(cadena.swapcase())

# convertir cadena a formato de titulo
cadena = "Hola Jose"
print(cadena.title())


#Act 3.
print("=================")
print("=== Conversor ===")
print("=================\n")

print("Menú de opciones: \n")
menu = '''
print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número.")\n
'''
print(menu)
opcion = int(input("¿cuál es la opción deseada:  ?"))
if opcion == 1:
    print("\n Conversor de número a palabra. \n")
    opcion_uno = int(input("¿Cuál es el número que deseas convertir a palabra?: "))
    if opcion_uno == 1:
        print("El número es  'UNO' ")
    elif opcion_uno == 2:
        print("El número es  'DOS' ")
    elif opcion_uno == 3:
        print("El número es  'TRES' ")
    elif opcion_uno == 4:
        print("El número es  'CUATRO' ")
    elif opcion_uno == 5:
        print("El número es  'CINCO' ")
    else:
        print("El número seleccionado no está registrado.")

elif opcion == 2:
    print("\n Conversor de palabra a número. \n")
    opcion_dos = input("¿Cuál es la palabra que deseas convertir a número?:")
    opcion_dos = opcion_dos.lower() #Metodo .lower() convertir cadena de caracteres en minúsculas

    if opcion_dos == "uno":
        print ("El número es ' 1 '")
    elif opcion_dos == "dos":
        print ("El número es ' 2 '")
    elif opcion_dos == "tres":
        print ("El número es ' 3 '")
    elif opcion_dos == "cuatro":
        print ("El número es ' 4 '")
    elif opcion_dos == "cinco":
        print ("El número es ' 5 '")
    else:
        print("El número seleccionado no está registrado.")
else:
    print("\n Opción no valida")
print("fin.")

#MENU 2

menu = """ 
Bienvenidos al registro de usuarios, llene los campos que usted 
prefiera a continuación seleccionando un número del 1 al 3: 
[1] Digitar su Nombre 
[2] Digitar su edad 
[3] Digitar su correo electrónico 
"""
print(menu)
opcion = input('Digita una opción entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digita tu nombre: ')
    edad = input('digitar edad')
    print("tu nombre es:" + nombre)
    print("tu nombre es:", nombre)
    print('Tu nombre es {}'.format(nombre), 'tu edad es{}.'.format(edad))
elif opcion == '2':
    edad = input('Digita tu edad: ')
    print('Tu edad es:' + edad)
    print('Tu edad es:', edad)
    print('Tu edad es {}'.format(edad))
elif opcion == '3':
    email = input('Digita tu email: ')
    print('tu email es: ' + email)
    print('tu email es: ', email)
    print(f'tu email es: {email}')
else:
    print('Debes digitar un numero entre 1 y 3')
    print('=-='*20)
print("****** Gracias por usar nuestro servicio ******")


#MENU 3 


menu = """ Bienvenidos al registro de usuarios, llene los campos que usted
prefiera a continuación seleccionando un número del 1 al 3: 
[1] Digitar su Nombre 
[2] Digitar su edad 
[3] Digitar su correo electrónico 
"""
print(menu)
opcion = input('Digita una opción entre 1 y 3: ')
if opcion == '1':
    nombre = input('Digita tu nombre: ')
    if nombre.isalpha():#el metodo isalpha, es para str, y evalua si es una cadena de caracteres
        print('Tu nombre es {}'.format(nombre))
        print(f'Tu nombre es: {nombre}')
    else:
        print('Has digitado un nombre no valido...')
elif opcion == '2':
    edad = input('Digita tu edad: ')
    if edad.isnumeric(): #el metodo inumeric, es para datos numéricos,
        # y permite evaluar si edad es totalmente numérico
        edad = int(edad)  # Convierte la entrada a un entero
        if 0 <= edad <= 110:  # Verifica que la edad esté en el rango permitido
            print('Tu edad es {}'.format(edad))
            print(f'Tu edad es: {edad}')
        else:
            print('Has digitado una edad no valida...')
    else:
        print('Has digitado una edad no válida...')
elif opcion == '3':
    email = input('Digita tu email: ')
    if email.find('@')>=0 and email.find('.')>=0:#el metodo find que es buscar dentro de str 
        # una oracion o un caracter, y evalua si tiene caracteres especiales 
        print('Tu e-mail es {}'.format(email))
        print(f'tu email es: {email}')
    else:
        print('Has digitado un email no valido...')
else:
   print('Debes digitar un numero entre 1 y 3')
   print('=-='*20)
print('****'*10)


#Listas

list = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print(list[4])

#DICCIONARIO

diccionario = {"azul":"blue","a":"A"}
print(diccionario["azul"])

del(diccionario["a"])
print(diccionario)

diccionario = {"Pedro":{"edad":22, "estatura":"165cm"}, "Ana":{"edad":40, "estatura":"150cm", "Jorge":{"edad":56, "estatura":"180cm"}}}
print(diccionario["Pedro"])

#FOR IN


nums = [4, 74, 93, 102]
for n in nums : 
    print(n)

for i in range (0, 5):
    print(i)
    if i == 2:
        print("Listo")


#Escribir un programa que pida al usuario una palabra y la muestre 10 veces

palabra = input("Digite una palabra ")

for i in range(10):
    print(palabra)

#Crear un programa que pregunte al usuario la edad y muestre en pantalla de manera ascendente hasta la años que tiene

edad = int(input("Digite su edad "))

for i in range(1, edad + 1):
    print(i)

#While
x = 1
while x < 10:
    x += 1
    print(x)


#Realizar un ciclo que permita evaluar los valores menores a 100 y que los incremente de 2 en 2 y que haga un break imprimiendo el bicle ha finalizado

#FUNCIONES

def num_por_5(num):
    print(f'{num} * 5 = {num * 5}')
print("Inicio de la multiplicación x 5")

num_por_5(1)
print("siguiente")
num_por_5(2)
print("Fin.")


def suma(a=3, b=4):
    return a + b
#llamar a la función sin argumentos para usar los valores por defecto

results = suma()
print(results)

#suma de valores
results_con_parametros= suma(5,6)
print(results_con_parametros)

#if_else_return ppara saber el numero mayor

def numMayor(n1,n2):
    if n1>n2:
        max= n1
    else: 
        max = n2
    return max

print("realizar calculo para determinar cual es el numero mayor ")

n1 = int(input("Digitar numero 1: "))
n2 = int(input("Digitar numero 2: "))

mayor = numMayor(n1,n2)
print(f'El numero mayor es: {mayor}')

#clases y objetos

#__init__ es un metodo que permite inicializar atributos de un objeto
#importante tener Def
class nombreDeLaClase(object):  #viene heredado del objeto
    def __init__(self, parametros):
        self.nombre = nombre

class Persona(object): #declarar la clase persona  (heredada de objeto)
    def __init__(self, nombre, edad): #constructor de la clase
        self.nombre = nombre # Inicializamos el atributo nombre
        self.edad = edad # Inicializamos el atributo edad
        
    def presentarse(self): #funcion para presentar a la persona
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años') 

#crear objeto 
persona1 = Persona("Juan", 30) # Creando un objeto con nombre y edad
persona1.presentarse() # llamar al metodo para presentar la persona