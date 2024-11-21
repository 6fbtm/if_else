#Programa que lea N numeros, calcule y escriba suma de pares y producto de los impares.


lista=[]

suma = 0
mult = 1

while True:
  n = input("Agregue un numero: ")
  if n == "salir":
    for i in lista:
      if i%2 == 0:
        suma += i
      else:
        print(f"Numero elegido {i}")
        mult *= i
    break
  else:
    n = int(n)
    lista.append(n)

    
print(f"La suma de los pares de {suma}")
print(f"El producto de los impares es de {mult}")