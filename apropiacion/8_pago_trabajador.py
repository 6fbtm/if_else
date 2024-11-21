#Programa que calcule el pago de un trabajador basado en su rango en la empresa y el total de las horas trabajadas

#Si es EMPLEADO es de 20000 y si es ADMINISTRATIVO es de 10000

print("-- Bienvenido a la base de datos de pagos del trabajador --")

print("Porfavor, ingrese los datos: ")

rango = input("Ingrese el rango del trabajador (Empleado o Administrativo): ").lower()

horas = int(input("Ingrese el numero de horas del trabajador: "))

def pago(rango,horas):
  if rango == "empleado":
    pago = horas*20000
    resultado = f"El pago del trabajador es de {pago}"
    return resultado
  elif rango == "administrativo":
    pago = horas*10000
    resultado = f"El pago del trabajador es de {pago}"
    return resultado
  else:
    return "Error en el sistema. Digite bien el rango"

print(pago(rango,horas))
