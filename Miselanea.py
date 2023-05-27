print("Miscelanea de ejercicios")

print("1:" "Área de un triángulo.")
print("2:" "Calculadora.")
print("3:" "Calculadora al cuadrado.")
print("4:" "Suma de 1234 y 532.")
print("5:" "Resta de 1234 y 532.")
print("6:" "Multiplicación de 1234 y 532.")
print("7:" "División de 1234 y 532.")
print("8:" "Porcentaje de 1234 y 532.")
print("9:" "Convertir euros a dólares.")
print("10:" "Carcular el area de un rectangulo.")
print("11:" "Calcular area y perimetro de un cuadrado.")
print("12:" "Area y voluen de un cilindro.")
print("13:" "Longitud y Area.")
print("14:" "Promedio entre 3 numeros.")

opcion = int(input("Ingrese el numero del ejercicio que desea hacer: "))
if opcion==1:
        print("Área de un triángulo")
        base = int(input("Ingrese la base del triángulo: "))
        altura = int(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print("El resultado del área es:", area)

elif opcion == 2:
        print("Calculadora")
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        suma = valor1 + valor2
        print("El resultado de la suma es:", suma)

elif opcion == 3:
        print("Calculadora al cuadrado")
        valor = int(input("Ingrese el valor que desea elevar: "))
        elevar = valor ** 2
        print("El resultado es:", elevar)
elif opcion == 4:
        print("Suma de 1234 y 532")
        num1 = 1234
        num2 = 532
        suma = num1 + num2
        print("El resultado de la suma es:", suma)
elif opcion == 5:
        print("Resta de 1234 y 532")
        num1 = 1234
        num2 = 532
        resta = num1 - num2
        print("El resultado de la resta es:", resta)

elif opcion == 6:
        print("Multiplicación de 1234 y 532")
        num1 = 1234
        num2 = 532
        multi = num1 * num2
        print("El resultado de la multiplicación es:", multi)
elif opcion == 7:
        print("División de 1234 y 532")
        num1 = 1234
        num2 = 532
        div = num1 / num2
        print("El resultado de la división es:", div)

elif opcion == 8:
        print("Porcentaje de 1234 y 532")
        num1 = 1234
        num2 = 532
        porcent = num1 % num2
        print("El resultado del porcentaje es:", porcent)
elif opcion == 9:
        print("Convertir euros a dólares")
        euros = float(input("Ingrese la cantidad que desea convertir: "))
        num = 1.10
        dolares = euros * num
        print("La conversión a dólares es:", dolares)
elif opcion == 10:
     print("Carcular el area de un rectangulo")

     largo = float(input("Ingrese el largo de la figura: "))
     ancho = float(input("Ingrese el archo de la figura: "))

     area = (largo * ancho)

     print("El area de tu figura es: ", area)

elif opcion == 11:
     print("Calcular area y perimetro de un cuadrado")

     lado = int(input("Ingrese el valor del lado de su cuadrado: "))

     area = (lado * lado)
     perim= (4 * lado)

     print("El resultado del area es: ", area)
     print("El resultado del perimetro es: ", perim)

elif opcion == 12:
     print("Area y voluen de un cilindro")

     altura = float(input("Ingrese el valor de la altura del cilindro: "))
     radio = float(input("Ingrese el valor del radio de su cilindro: "))

     area = (2 * 3.1416 * radio * (radio + altura))
     vol = (3.1416 * radio ** 2 * altura)

     print("El area del cilindro es: ", area)
     print("El volumen del cilindro es: ", vol)

elif opcion == 13:
     print("Longitud y Area")
 
     import math 
     radio = float(input("Ingrese la medida del radio: "))
  
     longitud = 2 * math.pi * radio
     area = math.pi * radio ** 2
 
     print(" El resultado de la longitud es: ", longitud)
     print(" El resultado del area es: ", area)


elif opcion == 14:
     print("Promedio entre 3 numeros")

     num1 = float(input("Ingrese el primer valor: "))
     num2 = float(input("Ingrese el segundo valor: "))
     num3 = float(input("Ingrese el tercer valor: "))
 
     promedio = (num1 + num2 + num3) / 3

     print("El promedio de los valores es: ", promedio)