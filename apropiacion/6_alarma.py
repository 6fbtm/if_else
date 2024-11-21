#Programa que registre si la temperatura es mayor a 200 o si la presion es mayor, en caso de ser así que imprima "alarma" y de no, que imprima "normal" 

print("--Bienvenido al detector de anomalias--")

temp = int(input("Grados de temperatura: "))
pres = int(input("Grado de presión: "))

if temp > 100 or pres > 200:
  print("Alarma")
else:
  print("Normal")