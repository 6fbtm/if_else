#Programa que solicite dos nombres y que imprima coincidencia si los dos nombres comienzan o terminan con una misma letra

print("Ingrese dos nombres")

n1 = input("nombre 1: ")
n2 = input("nombre 2: ")

if n1[0] == n2[0]:
    print("coincidencia")
elif n1[-1] == n2[-1]:
    print("coincidencia")
else:
    print("no coinciden")