#Programa que calcule el mayor de 3 numeros

n1 = int(input("Ingrese un digito: "))
n2 = int(input("Ingrese un digito: "))
n3 = int(input("Ingrese un digito: "))

if n1 > n2 and n1 > n3:
  print(f"{n1} es mas grande")
elif n2 > n1 and n2 > n3:
  print(f"{n2} es mas grande")
elif n3 > n1 and n3 > n2:
  print(f"{n3} es mas grande")
else:
  print(f"Los numeros son iguales")