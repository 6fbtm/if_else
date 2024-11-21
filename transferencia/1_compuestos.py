#Programa que exprese un compuesto químico dado de manera literal 

comp = input("Digita el compuesto: ")

comp.lower()

if comp == "nacl":
  print("El compuesto es Cloruro de sodio")
elif comp == "h20":
  print("El compuesto es Agua")
elif comp == "hcl":
  print("El compuesto es Acido clorhídrico")
else:
  print("Digite alguno de los tres compuestos")
