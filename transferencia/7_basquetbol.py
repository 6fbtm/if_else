#Programa que imponga requisitos a postulantes. Menor o igual de 19, estatura mayor a 175cm y peso entre 80 y 75kg



def requisitos():

  print("-- Bienvenido, postulante --")
  print("Porfavor, ingrese sus datos: ")

  edad = int(input("Porfavor, ingrese su edad en numeros: "))

  est = int(input("Porfavor, ingrese su estatura en numeros (cm): "))

  peso = int(input("Porfavor, ingrese su peso en numeros (kg): "))



  if edad <= 19:
    if est > 175:
      if peso > 75 and peso < 80:
        print("Postulante aprobado")
        return True
      else:
        print("Desaprobado")
        return 2
    elif peso > 75 and peso < 80:
      print("Desaprobado")
      return 2
    else:
      print("Desaprobado")
      return False
  
  elif est > 175:
    if peso > 75 and peso < 80:
      return 2
  else:
    print("Desaprobado")
    return False