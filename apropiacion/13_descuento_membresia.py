#Programa que calcule descuento respecto a la membresía del cliente
# tipo A: 10% descuento
# tipo B: 15% descuento
# tipo c: 20% descuento

print("--- Bienvenido a la base de datos de los precios por helado ---")
print("--- Precio por helado: $5000 ---")
print("Nuestros miembros reciben descuento: \n Tipo A: 10% DESCUENTO \n Tipo B: 15% DESCUENTO \n Tipo C: 20% DESCUENTO")

helado = int((input("Cantidad de helados a vender: ")))
print("-- No olvide introducir SOLO la letra correspondiente a la membresía --")
memb = input("Ingrese el tipo de membresía del cliente: ")

stotal = helado*5000

#This way pretty okay dw :)

if memb == "A":
  desc = stotal - (stotal*0.1)
  print(f"El precio de la compra es de: {desc}")
elif memb == "B":
  desc = stotal - (stotal*0.15)
  print(f"El precio de la compra es de: {desc}")
elif memb == "C":
  desc = stotal - (stotal*0.2)
  print(f"El precio de la compra es de: {desc}")
else:
  print(f"El precio de la compra es de: {stotal}")
