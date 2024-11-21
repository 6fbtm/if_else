#Programa que muestre signo zodiacal

print("--- Bienvenido al calculador de signos zodiacals ---")


mes = (input("Porfavor, ingrese su mes de nacimiento: "))
dia = int(input("Porfavor, ingrese su dia de nacimiento: "))

mes = mes.lower()

if mes == "enero":
  if dia <= 19:
    print("Según tu fecha de nacimiento eres: Capricornio")
  else:
    print("Según tu fecha de nacimiento eres: Acuario")

elif mes == "febrero":
  if dia <= 18:
    print("Según tu fecha de nacimiento eres: Acuario")
  else:
    print("Según tu fecha de nacimiento eres: Piscis")

elif mes == "marzo":
  if dia <= 20:
    print("Según tu fecha de nacimiento eres: Piscis")
  else:
    print("Según tu fecha de nacimiento eres: Aries")

elif mes == "abril":
  if dia <= 19:
    print("Según tu fecha de nacimiento eres: Aries")
  else:
    print("Según tu fecha de nacimiento eres: Tauro")

elif mes == "mayo":
  if dia <= 20:
    print("Según tu fecha de nacimiento eres: Tauro")
  else:
    print("Según tu fecha de nacimiento eres: Géminis")

elif mes == "junio":
  if dia <= 20:
    print("Según tu fecha de nacimiento eres: Géminis")
  else:
    print("Según tu fecha de nacimiento eres: Cáncer")

elif mes == "julio":
  if dia <= 22:
    print("Según tu fecha de nacimiento eres: Cáncer")
  else:
    print("Según tu fecha de nacimiento eres: Leo")

elif mes == "agosto":
  if dia <= 22:
    print("Según tu fecha de nacimiento eres: Leo")
  else:
    print("Según tu fecha de nacimiento eres: Virgo")

elif mes == "septiembre":
  if dia <= 22:
    print("Según tu fecha de nacimiento eres: Virgo")
  else:
    print("Según tu fecha de nacimiento eres: Libra")

elif mes == "octubre":
  if dia <= 22:
    print("Según tu fecha de nacimiento eres: Libra")
  else:
    print("Según tu fecha de nacimiento eres: Escorpio")

elif mes == "noviembre":
  if dia <= 21:
    print("Según tu fecha de nacimiento eres: Escorpio")
  else:
    print("Según tu fecha de nacimiento eres: Sagitario")

elif mes == "diciembre":
  if dia <= 21:
    print("Según tu fecha de nacimiento eres: Sagitario")
  else:
    print("Según tu fecha de nacimiento eres: Capricornio")
