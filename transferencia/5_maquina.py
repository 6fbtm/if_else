#Programa de maquina que recibe monedas a cambio de dulces. Dulce $2000 Cuando la maquina reciba una moneda de $5000 o $10000 debe dar el cambio

print("-- Bienvenido a la maquina expendedora --")
print("Insértele una moneda a la maquina. Cada dulce es a $2000")
print("1. Insertar moneda de $2000\n2. Insertar moneda de $5000\n3. Insertar moneda de $10000")



mon = int(input("Elija la opción: "))

if mon == 1:
  print("Dulce entregado.")
elif mon == 2:
  print("Dulce entregado. Cambio: $3000")
else:
  print("Dulce entregado. Cambio: $8000")