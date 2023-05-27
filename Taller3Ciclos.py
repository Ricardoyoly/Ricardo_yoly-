Ejercicio 1

print("Multiplos de 3 de 1 a 100:")
#este codigo muestra todos los Multiplos de 3 entre 1 y 100

#ouputs, process and inputs

for i in range (3, 100, 3):
  print("_",i)

Ejercicio 2 
print("Numeros imapres de 1 a 100:")
#este codigo muestra todos los números impares entre 1 y 100
#inputs, process and outputs

for i in range(1,100,2):
  print("•",i)


Ejercicio 3
print("Numeros pares de 1 a 100:")
#este codigo muestra todos los números pares entre 1 y 100
#inputs process and outputs

for i in range(2,101,2):
  print("•", i)

Ejercicio 4
print("Numeros de 1 a 3:")

#este codigo muestra los números de 1 a 3
#inputs process and outputs

for i in range(1,4,1):
  print("•",i)

Ejercicio 5
print("Numeros de 10 a 1:")

#este codigo muestra todos los números del 10 al 1 
#inputs process and outputs

for i in range(10,0,-1):
 print("•",i)

Ejercicio 6
print("Suma de los numeros al cuadrado del 1 al 100:")
#este codigo hace que todos los numeros al cuadrado de 1 a 100 se sumen automaticamente
#inputs
suma = 0 
#process and outputs
for i in range(1, 101):
  suma += i ** 2

print("el resultado es:" , suma)
Ejercicio 7
print("Suma de numeros al cuadrado de 1 a 100:")

#este codigo suma todos los números al cuadrado de 1 a 100
#inputs process and outputs

for i in range (1,101):
  print("•",)
Ejercicio 8
print("Suma de los siguientes 100 numeros:")

#este codigo hace que se sumen los siguientes 100 numeros al numero que ingrese el usuario
#inputs
number = int(input("Ingrese el numero: "))

suma = 0

#process and outputs
for i in range(number, number + 100):
  suma += i

print("El resultado es:", suma)
Ejercicio 9
print("Hallar numero factorial:")
#este codigo halla la factorial de un numero ingresado por un usuario
#inputs
number = int(input("Ingrese el numero: "))

factorial = 1

#process 
if number < 0:
    print("El factorial no está definido para números negativos.")
elif number == 0:
    print("El factorial de 0 es 1.")
for i in range(1, number + 1):
  factorial *= i
#outputs
print("La factorial es:",factorial)
Ejercicio 10
print("Temperatura de grados fahrebheit a grados celsius")

#este codigo pasa temperatura de grados fahrebheit a grados celosías

#inputs
while True:
    temperatura_fahrenheit = float(input("Ingrese una temperatura en grados Fahrenheit (999 para finalizar): "))

    if temperatura_fahrenheit == 999:
        print("Programa finalizado.")
        break
#process
    temperatura_celsius = (5 / 9) * (temperatura_fahrenheit - 32)

#outputs
    print("La temperatura equivalente en grados Celsius es:", temperatura_celsius)
Ejercicio 11
print("Numeros primos")

#este codigo muestra todos los números primos que hay hasta el número que el usuario ingrese

#inputs 
number_limit = int(input("Ingrese un número: "))

print(f"Números primos hasta {number_limit}:")
#process and outputs
for i in range(2, number_limit + 1):
    es_primo = True
    for divisor in range(2, int(i ** 0.5) + 1):
        if i % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(i)
Ejercicio 12
print("Tabla de múltiplicar")

#este codigo muestra cualquier tabla de multiplicar que el usuario desee 
#inputs
number = int(input("Ingrese un número para ver su tabla de multiplicar: "))

#proceso and outputs
print(f"Tabla de multiplicar del número {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
Ejercicio 13
print("Números acedentes")

#este codigo muestra los números en términos acedentes entre los números que ingrese el usuario 
#inputs
number_inicial = int(input("Ingrese el primer número natural: "))
number_final = int(input("Ingrese el segundo número natural: "))

#process and outputs
if number_inicial >= number_final:
    print("El primer número debe ser menor que el segundo.")
else:
    
    print("Números en secuencia ascendente:")
    for numero in range(number_inicial, number_final):
        print(numero, end=" ")
    print(number_final)  
Ejercicio 14 
print("Piezas de dominó")

#este codigo muestra todas las fichas de nominó en su orden
#inputs process and outputs 

def mostrar_piezas_dominó():
    for i in range(7):
        for j in range(i, 7):
            print(f"{i}-{j}")

mostrar_piezas_dominó()