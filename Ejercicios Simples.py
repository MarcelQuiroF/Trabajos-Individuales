#Ejercicio 1 (Suma de los numeros pares)
numero = int(input("Ingrese un numero entero positivo"))
inicio = 0
suma = 0
while inicio <= numero:
    if inicio % 2 == 0:
        suma += inicio
    inicio += 1
print(f"La suma de todos los numeros pares de {numero} es {suma}")

#Ejercicio 2 (Contador de numeros impares/pares)
numero = int(input("Ingrese un numero entero positivo"))
NumerosPares = 0
NumerosImpares = 0
while True:
    if numero % 2 == 0:
        NumerosPares += 1
    elif numero % 2 == 1:
        NumerosImpares += 1
    numero -= 1
    if numero == 0:
        break
print("Los numeros pares son ", NumerosPares)
print("Los numeros impares son ", NumerosImpares)

#Ejercicio 3 (Factorial de  un numero)
Numero = int(input("Introducir numero no negativo entero: "))
if Numero < 0:
   print("Ese no es un entero positivo")
else:
    Resultado = 1
    for i in range(1, Numero+1):
        Resultado *= i
    print(Resultado)


#Ejercicio 4 (Gestion de inventario)
import random
platano = random.randint(0, 150) 
manzana = random.randint(0, 150) 
durazno = random.randint(0, 150) 
papa = random.randint(0, 150) 
while True:
    Producto = (input("""Escriba el nombre del producto que desee
1. Platano
2. Manzana
3. Durazno
4. Papa
"""))
    if Producto == "1" or Producto == "Platano" or Producto == "platano":
        nombre_Usuario = input("Escriba su nombre: ")
        cantidad = int(input("Escriba la cantidad: "))
        if cantidad < platano or cantidad == platano:
            platano -= cantidad
            print("""Se ha realizado el pedido
""")
        else:
            print(f"""Contamos con {platano} platanos, lo sentimos
""")
            
    elif Producto == "2" or Producto == "Manzana" or Producto == "manzana":
        nombre_Usuario = input("Escriba su nombre: ")
        cantidad = int(input("Escriba la cantidad: "))
        if cantidad < manzana or cantidad == manzana:
            manzana -= cantidad
            print("""Se ha realizado el pedido
""")
        else:
            print(f"""Contamos con {manzana} manzana, lo sentimos
""")
            
    elif Producto == "3" or Producto == "Durazno" or Producto == "durazno":
        nombre_Usuario = input("Escriba su nombre: ")
        cantidad = int(input("Escriba la cantidad: "))
        if cantidad < durazno or cantidad == durazno:
            durazno -= cantidad
            print("""Se ha realizado el pedido
""")
        else:
            print(f"""Contamos con {durazno} duraznos, lo sentimos"
""")
    elif Producto == "4" or Producto == "Papa" or Producto == "papa":
        nombre_Usuario = input("Escriba su nombre: ")
        cantidad = int(input("Escriba la cantidad: "))
        if cantidad < papa or cantidad == papa:
            papa -= cantidad
            print("""Se ha realizado el pedido
""")
        else:
            print(f"""Contamos con {papa} papas, lo sentimos"
""")
            
    else:
        print("No contamos con ese producto ")


#Ejercicio 5 (Requisitos de contraseña)
requisito = 0

while requisito != 2:
    mayusculas = 0
    minusculas = 0
    digitos = 0
    
    contraseña = input("Escriba su contraseña: ")
    
    if len(contraseña) < 8:
        print("La contraseña debe tener almenos 8 caracteres")
    else:
        requisito += 1
        
    for caracteres in contraseña:
        if caracteres.isupper():
            mayusculas +=1
        elif caracteres.islower():
            minusculas +=1
        elif caracteres.isdigit():
            digitos +=1
            
    if len(contraseña) == mayusculas or len(contraseña) == minusculas or len(contraseña) == digitos:
        print("La contrañesa no puede tener solo mayusculas, minusculas o numeros")
    elif mayusculas == 0 or minusculas == 0 or digitos == 0:
        print("La contraseña debe contener almenos un numero, mayuscula y minuscula")
    else:
        requisito += 1
print("Contraseña establecida")


#Ejercicio 6 (Promedio de Estudiantes)
estudiantes = int(input("Ingrese el numero de la cantidad de estudiantes: "))
cantidad_Estudiantes = list(range(0, estudiantes))

materias = int(input("Ingrese el numero de la cantidad de Materias: "))
cantidad_Materias = list(range(0, materias))
notas_Materias = len(cantidad_Materias)

indice_Estudiantes = 0
indice_Materia = 0
cantidad_Aprobados = 0
cantidad_Desaprobados = 0
promedio_Total = 0

while indice_Materia != len(cantidad_Materias):
    cantidad_Materias[indice_Materia] = input(f"Ingrese el nombre de la materia numero {cantidad_Materias[indice_Materia]+1}: ")
    indice_Materia +=1

while indice_Estudiantes != len(cantidad_Estudiantes):
    cantidad_Estudiantes[indice_Estudiantes] = input(f"Ingrese el nombre del estudiante numero {cantidad_Estudiantes[indice_Estudiantes]+1}: ")
    indice_Estudiantes += 1

indice_Estudiantes = 0
indice_Materia = 0
promedio = 0

while indice_Estudiantes != len(cantidad_Estudiantes):
    promedio_Total += promedio
    promedio = 0
    indice_Materia = 0
    while True:
        promedio += int(input(f"""Ingrese la nota que saco {cantidad_Estudiantes[indice_Estudiantes]} en {cantidad_Materias[indice_Materia]}
"""))
        indice_Materia += 1
        if indice_Materia == len(cantidad_Materias):
            promedio = (promedio/indice_Materia)
            if promedio < 51:
                print(f"El estudiante {cantidad_Estudiantes[indice_Estudiantes]} desaprobo con {promedio} de promedio")
                cantidad_Desaprobados += 1
                break
            elif promedio >= 51:
                print(f"El estudiante {cantidad_Estudiantes[indice_Estudiantes]} aprobo con {promedio} de promedio")
                cantidad_Aprobados += 1
                break
    indice_Estudiantes += 1
    
promedio_Total += promedio
promedio_Total = (promedio_Total/len(cantidad_Estudiantes))
print(f"""El promedio total es de {promedio_Total}
La cantidad de aprobados es: {cantidad_Aprobados}
La cantidad de desaprobados es: {cantidad_Desaprobados}""")

