#Programa que calcule los pagos hechos en un restaurante y en caso de exceder los 130k el descuento será de 15%

print("-- Bienvenido al contador de pagos --")
print("Ingrese los pagos y cuando no hayan mas, digite la palabra 'salir'")
lim = 130000
pagos = []


def descuento():
  cont = 0
  while True:
    pago = (input("Digite el valor del pago: "))
    if pago == "salir":
      for i in pagos:
        cont += i
      print(cont)
      if cont > lim:
        porc = cont*0.15
        desc = cont-porc
        return(desc)
      break
    else:
      pago = int(pago)
      pagos.append(pago)

print(descuento())