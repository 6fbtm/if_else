# Programa que le pida al usuario una vocal y si es una vocal que imprima vocal. Solo se debe poder ingresar un caracter

lt = input("Ingrese un caracter ")


if len(lt) == 1:
    if lt == "a" or lt == "e" or lt == "i" or lt == "o" or lt == "u":
        print("vocal")
else:
    print("Ingrese solo un caracter")