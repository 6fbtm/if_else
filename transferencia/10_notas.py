#Programa que reciba n notas de alumnos de 100 a 1 y que muestre ntoa baja, alta y cuantos alumnos obtuvieron: A: 100> >=90 B: 90> >=80 C: 80> >= 70 D: 70> >=60

print("--- Bienvenido a la base de datos de notas ---")
print("Ingrese la nota del alumno. Para salir, digite 'salir'")


na = 0
nb = 0
nc = 0 
nd = 0
ds = 0

while True:
    nota = (input("Digite la nota del estudiante: "))
    
    if nota == "salir":
        break
    else:
        nota = float(nota)
        if nota >= 90:
            na += 1
        elif nota >= 80:
            nb += 1
        elif nota >= 70:
            nc += 1
        elif nota >= 60:
            nd += 1
        else:
            ds += 1

print(f"Los alumnos que sacaron nota A fueron: {na}, los que sacaron nota B fueron {nb}, los que sacaron nota C fueron {nb} y los que sacaron nota D fueron {nd}. {ds} alumno(s) reprobaron.")