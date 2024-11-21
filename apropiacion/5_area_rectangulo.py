#Programa que calcule el area de un rectangulo siempre y cuando los lados sean positivos

print("--- Bienvenido al calculador de areas (rectangulo)")
print("Asegurese que los numeros sean positivos")
l1 = int(input("Digite el primer lado: "))
l2 = int(input("Digite el segundo lado: "))


if l1 > 0 and l2> 0:
  area = l1*l2
  print(f"El area de su rectangulo es de {area}")
else:
  print("Numeros no positivos")