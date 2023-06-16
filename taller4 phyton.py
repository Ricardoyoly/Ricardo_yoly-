Listas 
1 ejercicio:
print("Suma en lista")

#este codigo suma unos numeros predeterminados 
#inputs and process
def list(numbers):
  suma = 0
  for number in numbers:
      suma += number
  return suma  
numbers = [1,2,3,4,5,6,7,8,]
result = list(numbers)
#outputs
print(result)

2 ejercicio:
print("Promedio en lista")

#este codigo saca el promedio de unos numeros predeterminados y lo muestra en pantalla
#inputs and process
def promedio(numbers):
    total = sum(numbers)
    amount = len(numbers)
    promedio = total / amount
    return promedio

#outputs
numbers = [1,2,3,4,5]
promedio = promedio(numbers)
print(promedio)

3 ejercicio:
print(" Eliminar numeros duplicados")

#este codigo elimina todos los numeros que esten duplicados 
#inputs and process
def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados


mi_lista = [1, 1, 2, 2, 3, 3, 4 ,5]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
#outputs
print(lista_sin_duplicados)

4 ejercicio:
print("Ordenar de menor a mayor")

#este codigo ordena los numeros ingresados previamente de menor a mayor
#inputs and process
def order_list (list):
    for a in range(len(list)):
        for s in range(a+1, len(list)):
            if list[s] < list[a]:
                list[a], list[s] = list[s], list[a]
    return list

numbers = [1,3,5,2,4]
list_order = order_list(numbers)
#outputs
print(list_order)

5 ejercicio:
print("Palabras largas en listas")

#este codigo muestra las palabra mas larga entre un grupo de palabras ya escritas previamente
#inputs and process
def words_long(list):
     word = max(list,key=len)
     return  word

word_list = ["Hola", "phyton", "Programacion"]
word = words_long(word_list)
#outputs
print("La palabra mas larga es:", word)

Tuplas
1 ejercicio:
print("Producto de elementos")

#este codigo multiplica todos los numeros previamente escritos en la tupla
#inputs and process
def cal_produc(tupla):
    produc = 1
    for number in tupla:
        produc *= number
    return produc


my_tupla = (1,2,3,4,5)
result = cal_produc(my_tupla) 
#outputs
print(result)

2 ejercicio:
print("Numero mayor y numero menor")

#este codigo muestra el numero mayor y el numero menor de una cierta lista escrita previamente
#inputs and process
def num_mayor_minor(tupla):
    mayor = max(tupla)
    minor = min(tupla)
    return mayor , minor

tupla_numbers = (3,2,5,7,9,1,4)
mayor, minor =  num_mayor_minor(tupla_numbers)
#outputs
print("El numero mayor es:",mayor)
print("El numero menor es:",minor)

3 ejercicio:
print("Contador")

#este codigo mustra cuantas veces hay un numero en la lista 
#inputs and process
def contador(tupla):
    diccionario = {}
    for element in tupla:
        if element in diccionario:
            diccionario[element] += 1

        else:
          diccionario[element] = 1
    return diccionario 

tupla_elements = (2,3,9,7,5,9,2,3,5,3)
result = contador(tupla_elements)
#outputs
print(result)

4 ejrcicio:
print("Índices")

#este codigo busca un elemto en la lista y lo muestra en pantalla
#inputs and process
def buscar_indices(tupla, elemento):
    indices = [index for index, value in enumerate(tupla) if value == elemento]
    return indices

tupla_elementos = (1, 3, 6, 2, 4, 5)
elemento_buscado = 2
indices = buscar_indices(tupla_elementos, elemento_buscado)
#outputs
print(indices)
  
5 ejercicio:
print("Separar elementos")

#este codigo muestra las palabras que empiezan con vocales y las que no empiezan 
#inputs and process
def separar_por_vocal(tupla):
    vocales = ('a', 'e', 'i', 'o', 'u')
    empiezan_con_vocales = tuple(filter(lambda x: x.lower().startswith(vocales), tupla))
    no_empiezan_con_vocales = tuple(filter(lambda x: not x.lower().startswith(vocales), tupla))
    return empiezan_con_vocales, no_empiezan_con_vocales

tupla = ('Manzana', 'Naranja', 'Plátano', 'Perro', 'Gato', 'Elefante')
empiezan, no_empiezan = separar_por_vocal(tupla)
#outputs
print("Cadenas que empiezan con vocal:", empiezan)
print("Cadenas que no empiezan con vocal:", no_empiezan)

Diccionarios
1 ejercicio:
print("Contar palabras")

#este codigo cuenta cuantas veces hay una palabra en la lista
#inputs and process
def contar_palabras(lista_palabas):
    contador = {}
    for palabra in lista_palabas:
         if palabra in contador:
              contador[palabra] +=1
         else:
           contador[palabra] = 1
    return contador

lista = ["hola", "adios", "bienvenido", "hola" ]
result = contar_palabras(lista)
#outputs
print(result)

2 ejercicio:
print("Calcular promedio de calificaciones")

#este codigo calcula el promedio de las notas de unos estudiantes de un colegio 
#inputs and process
def calcular_promedio(diccionario_estudiantes):
    total_calificaciones = 0
    cantidad_estudiantes = len(diccionario_estudiantes)

    if cantidad_estudiantes == 0:
       return 0

    for estudiante, calificacion in diccionario_estudiantes.items():
        total_calificaciones += calificacion

    promedio = total_calificaciones / cantidad_estudiantes
    return promedio

estudiantes = {"Pedro": 85, "Juan": 92, "Pablo": 78, "Marcos": 90}
promedio = calcular_promedio(estudiantes)
#outputs
print(promedio)
    
3 ejercicio:
print("Valor")

#este codigo muestra las letras que tienen respectivo numero 
#inputs and process
def filtrar_valor(diccionario, valor):
    resultado = {}
    for clave, val in diccionario.items():
        if val == valor:
            resultado[clave] = val

    return resultado

diccionario = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
valor_a_dar = 1
resultado = filtrar_valor(diccionario, valor_a_dar)
#outputs
print(resultado)

4 ejercicio:
print("Combinar diccionario")

#este codigo combina datos de dos diccionario diferentes a uno solo
#inputs and process
def combinar_diciionario(diccionario1, diccionario2):
    diccionario_combinado = diccionario1.copy()

    for clave, valor in diccionario2.items():
        if clave in diccionario_combinado:
          diccionario_combinado[clave] += valor

        else:
          diccionario_combinado[clave] = valor

    return diccionario_combinado

diccionario1 = {"a": 10, "b": 20, "c": 30}
diccionario2 = {"b": 15, "c": 25, "d": 40}

diccionario_combinado = combinar_diciionario(diccionario1, diccionario2)
#outputs
print(diccionario_combinado)

5 ejercicio:
print("Palabras frecuentes")

#este codigo cuenta cuantas palabras hay en un diccionario y las muestra en pantalla
#inputs and process
def palabras_frecuentes(texto):
    texto = texto.lower()
    palabras = texto.split()
    contador = {}

    for palabra in palabras:
      if palabra in contador:
         contador[palabra] +=1

      else:
        contador[palabra] =1

    return contador

texto = "las palabras pueden ser largas. hay varias palabras y algunas palabras se repiten"
resultado = palabras_frecuentes(texto)
#outputs
print(resultado)
