#Programa que exprese una calificación de manera literaria de acuerdo con la calificacion numérica
print("--- Bienvenido a la plataforma de calificaciones ---")


cal = float(input("Ingrese la calificación: "))

if cal <= 10 and cal > 9:
  print("Excelente")
elif cal > 8:
  print("Muy bien")
elif cal > 7.4:
  print("Bien")
else:
  print("No aprobado")