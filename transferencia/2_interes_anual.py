#Programa que añada interes de acuerdo con el valor del saldo

print("--- Bienvenido a la base de saldos ---")
print("Porfavor, ingrese los datos pedidos")

saldo = int(input("Ingrese el valor del saldo: $"))

if saldo > 100000:
  pago = (saldo*0.03) + saldo
  print(pago)
else:
  pago = (saldo*0.4) + saldo
  print(pago)