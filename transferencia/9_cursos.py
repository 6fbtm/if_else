#Programa que permita ingresar n cantidad de cursos,y si cursos < 6 entonces el valor es de 2M, pero si no, entonces es de 1,2M

print("-- Base de datos del LMS --")

print("Porfavor, ingrese la cantidad de cursos del usuario")

cursos = int(input())

if cursos < 6:
  valor = cursos*2000000
  print(f"El valor de la compra por los cursos es de: ${valor}")
else:
  valor = cursos*1200000
  print(f"El valor de la compra por los cursos es de: ${valor}")