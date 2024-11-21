#Programa que lea 3 valores e indique cual es el mayor de ellos, el menor o si son iguales

n1 = int(input("Ingrese un digito: "))
n2 = int(input("Ingrese un digito: "))
n3 = int(input("Ingrese un digito: "))

lista = [n1,n2,n3]

mayor=[]
menor=[]
igual=[]

for i in range(len(lista)):
  for j in range(i+1,len(lista)):
    if lista[i] > lista[j]:
      mayor.append(lista[i])
      menor.append(lista[j])
    elif lista[i] < lista[j]:
      mayor.append(lista[j])
      menor.append(lista[i])
    else:
      print(f"{lista[i]} está repetido")
      igual.append(lista[i])
  

mayor.sort(reverse=True)
menor.sort(reverse=False)
igual.sort(reverse=True)


print(f"El numero mayor es {mayor[0]}")
print(f"El numero menor es {menor[0]}")
if igual:
  print(f"El numero {igual[0]} se repite")

