1 ejercicio 
print("Numero positivo o negativo")

#inputs
#con este código se podrá saber si un número es positivo o negativo 

number = float(input("Ingrese el número: "))

#proceso & outputs
if number > 0:
    print("El número es positivo")

elif number == 0:
    print("El numero es cero")

else:
    print("El número es negativo")


2 ejercicio
print("Numero mayor y numero menor")

#inputs
#con este codigo se podra ver que numero es menor y cual numero es mayor,tras ingresar 3 numeros por teclado

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el tercer numero: "))

#process
if number1 >= number2 and number1 >= number3:
    mayor = number1
elif number2 >= number1 and number2 >= number3:
    mayor = number2
else:
    mayor = number3


if number1 <= number2 and number1 <= number3:
    minor = number1
elif number2 <= number1 and number2 <= number3:
    minor = number2
else:
    minor = number3
  
#outputs
print("El numero mayor es: ", mayor)
print("El numero menor es: ", minor)

3 ejercicio
print("Sueldo de los empleados")

#inputs
#con este codigo se calculara el sueldo de los empleados normalmente y su sueldo de horas extras

name = input("Digite su nombre: ")
normal_hours = int(input("Digite cuantas horas trabaja normalmente: "))
extra_hours = int(input("Digite cuantas horas extra trabaja: "))

#process
salary_hour = 4
salary_normal = normal_hours * salary_hour
salary_extra = extra_hours * (salary_hour * 2)

total_salary = salary_normal + salary_extra 

#outputs
print("El salario normal de", name, "es:", total_salary, "dolares")

4 ejercicio
print("Bienvenido")

#inputs
#con este codigo si el primer numero es menor se suma sino se restan
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

#process
if a < b:
  result = a + b
else:
  result = a - b

#outputs
print("El resultado es: ", result)


5 ejercicio
print("Cociente")

#inputs
#con este codigo se podra saber el cociente de una division

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

#process
if b == 0:
    print("No es posible dividir por cero")

elif a == b:
    print("El cociente de la division es: 1")
  
else:
    quotient = a / b

#outputs
print("El cociente de la division es: ", quotient)

6 ejercicio
print("Bienvenido")

#inputs
#con este codigo segun el numero que se ingrese se dira el dia de la semana que corresponde

numdia = int(input("Ingrese un numero del 1 al 7: "))

#process
if numdia ==1:
    print("Lunes")
elif numdia ==2:
    print("Martes")
elif numdia ==3:
    print("Miercoles")
elif numdia ==4:
    print("Jueves")
elif numdia ==5:
    print("Viernes")
elif numdia ==5:
    print("Viernes")
elif numdia ==6:
    print("Sabado")
elif numdia ==7:
    print("Domingo")

#outputs
else:
    print("El numero ingresado no es valido")

7 ejercicio
print("Triangulo equilatero")

#inputs
#con este codigo se mirara si un triangulo es equilatero o no

side1 = float(input("Ingrese la longitud del primer lado: "))
side2 = float(input("Ingrese la longitud del segundo lado: "))
side3 = float(input("Ingrese la longitud del tercer lado: "))
#process
if side1 == side2 and side2 == side3:
  print("El triangulo es equilatero")

#outputs
else:
  print("El triangulo no es equilatero")

8 ejercicio
print("Bienvenido")

#inputs
#con este codigo si un numero es negativo se sumara y si ambos son positivos se multiplicaran 

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

#process
if number1 < 0 or number2 < 0: 
  result = number1 + number2
  print("El resultado es: ", result)
  
  #outputs
else:
  result = number1 * number2
  print("El resultado es: ", result)

9 ejercicio
print("Bienvenido")

#inputs
#con este codigo se mirara el signo sodiacal

day = int(input("Introduce el día de nacimiento (1-31): "))
month = int(input("Introduce el mes de nacimiento (1-12): "))

#process
if day == 1:
    if day < 20:
        sign = "Capricornio"
    else:
        sign = "Acuario"
elif month == 2:
    if day < 19:
        sign = "Acuario"
    else:
        sign = "Piscis"
elif month == 3:
    if day < 21:
        sign = "Piscis"
    else:
        signo = "Aries"
elif month == 4:
    if day < 20:
        sign = "Aries"
    else:
        sign = "Tauro"
elif month == 5:
    if day < 21:
        sign = "Tauro"
    else:
        sign = "Géminis"
elif month == 6:
    if day < 21:
        sign = "Géminis"
    else:
        sign = "Cáncer"
elif month == 7:
    if day < 23:
        sign = "Cáncer"
    else:
        sign = "Leo"
elif month == 8:
    if day < 23:
        sign = "Leo"
    else:
        sign = "Virgo"
elif month == 9:
    if day < 23:
        sign = "Virgo"
    else:
        signo = "Libra"
elif month == 10:
    if day < 23:
        sign = "Libra"
    else:
        sign = "Escorpio"
elif month == 11:
    if day < 22:
        sign = "Escorpio"
    else:
        sign = "Sagitario"
elif month == 12:
    if day < 22:
        sign = "Sagitario"
    else:
        sign = "Capricornio"

#outputs
print("Tu signo es:", sign)

10 ejercicio
print("Bienvenido")

#inputs
#con este codigo se calculara si un cuadrilatero es cuadrado o rectangulo y dara el perimetro y la superficie 
base = int(input("Ingrese el valor de la base: "))
high = int(input("Ingrese el valor de la altura: "))

#process
if base == high:
  figure = "Cuadrado"

else:
  figure = "Rectangulo"

perimeter = 2 * (base * high)
surface = base * high

#outputs
print("El cuadrilatero es un: ", figure)
print("El perimetro es: ", perimeter)
print("La superficie es: ", surface)

11 ejercicio
print("Bienvenido")

#inputs
#con este codigo se mirara cuanto descuento tiene un objeto con un rango de precios especificos y al final dira el descuento realizado y el precio final  
selling_price = float(input("Ingrese el precio de venta: "))

#Process

if selling_price < 100:
    discount = selling_price * 0.05
elif selling_price < 200:
    discount = selling_price * 0.10
else:
    discount = selling_price * 0.15

final_price = selling_price - discount

#outputs
print("El descuento realizado es de $", discount)
print("El precio final con descuento es de $", final_price)

12 ejercicio
print("Bienvenido")

#inputs
#con este codigo miraremos si un año es bisiesto o no

year = int(input("Ingrese un año para determinar si es bisiesto o no: "))

#process
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "es un año bisiesto")

#outputs
else:
  print("no es un año bisiesto")