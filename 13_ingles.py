#Programa que solicite al usuario el dia de la semana, que indique si ese dia se realizaron pruebas y que indique cuantos alumnos aprobaron y cuantos no. Si se trata de un dia que no existe, el programa debe finalizar. Los examenes solo son lunes a miercoles


print("-- Bienvenido a la plataforma de inglés --")
print("Para registrar su clase, ingrese los datos:")

dia = (input("Ingrese el día de la semana: "))
dia = dia.lower()

semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]


if dia in semana:
    if dia in semana[:3]:
        exa = input("¿Hubo examen?").lower()
        if exa == "si":
            apro = int(input("¿Cuantos alumnos aprobaron? "))
            repro = int(input("¿Cuantos alumnos reprobaron?"))
            print("Registro actualizado.")
            porc = ((apro+repro)*apro)/100
            print(f"El {porc}% de los alumnos aprobaron el examen.")
        elif exa == "no":
            print("Registro actualizado.")
        else:
            print("ERROR: No se recibió un si/no.")
    else:
            print("Registro actualizado.")
else:
        print("ERROR: No se recibió un dia existente de la semana")


