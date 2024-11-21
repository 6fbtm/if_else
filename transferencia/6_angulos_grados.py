#Programa que convierta grados a radianes y viceversa

print("--- Bienvenido al conversor de angulos ---")
print("1. Grados\n2. Radianes")

tipo = int(input("Elija la opción: "))

if tipo == 1:
  ang = float(input("Digite el angulo en grados: "))
  rad = ang*(3.1416/180)
  rad = round(rad,2)
  print(f"El angulo de grados a radianes es de {rad} radianes")
else:
  ang = float(input("Digite el angulo en radianes: "))
  grad = ang*(180/3.1416)
  grad = round(grad,2)
  print(f"El angulo de radianes a grados es de {grad}° grados sexagesimales")