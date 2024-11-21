#Programa que calcule el total de 5 productos, IVA y subtotal. Visualizar: iva, subtotal y total

print("--- Bienvenido a la base de datos de los productos ---")
print("Por favor, digite los datos pedidos a continuación:")

pro1 = int(input("Por favor, digite el valor del producto 1: "))
pro2 = int(input("Por favor, digite el valor del producto 2: "))
pro3 = int(input("Por favor, digite el valor del producto 3: "))
pro4 = int(input("Por favor, digite el valor del producto 4: "))
pro5 = int(input("Por favor, digite el valor del producto 5: "))

print("-- Estimado cliente, se le recuerda que el valor del iva está al 20% --")

stotal = pro1+pro2+pro3+pro4+pro5
iva = stotal*0.2
total = iva+stotal

print(f"El subtotal de su producto está en: {stotal}")
print(f"El IVA aplicado a su producto fue de {iva}")
print(f"El total de su compra fue de {total}")