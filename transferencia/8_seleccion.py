#Programa que pide cantidad de alumnos que pasaron, desaprobaron, y que pasaron de dos requisitos
import importlib

basquetbol = importlib.import_module("7_basquetbol")

print("-- Bienvenido a la base de datos de postulantes --")

print("A continuación se recibirá información de los postulantes. Después de llenar la información de uno, escribe 'siguiente' para continuar y 'salir' para terminar el proceso.")



def postulantes():

  aprobado = 0
  desaprobado = 0
  semidesaprobado = 0

  comenzar = input("Digite 'comenzar'")

  if comenzar == "comenzar":
    while True:
      resultado = basquetbol.requisitos()
      if resultado == True:
        aprobado += 1
      elif resultado == 2:
        desaprobado += 1
        semidesaprobado +=1
      else:
        desaprobado += 1
      proc = input("Siguiente o salir?")
      if proc == "salir":
        break

postulantes()

