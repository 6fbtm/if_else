print("--- Bienvenido al calculador de areas ---")
print("Por ahora contamos con triangulo y circulo")
print("Por favor, digite la figura que quiere (sin tildes)")

fig = input("La figura que quiero es... ")

fig = fig.lower()

if fig == "triangulo":
  base = int(input("Por favor, digite la base del triangulo: "))
  alt = int(input("Por favor, digite la  altura del triangulo: "))
  area = (base*alt)/2
  print(f"El area del triangulo es de {area}")

elif fig == "circulo":
  rad =  int(input("Por favor, digite el radio de su circulo: "))
  area = 3.1416*(rad**2)
  print(f"El area es de {area}")

else:
  print("Por favor, digite la figura correctamente")