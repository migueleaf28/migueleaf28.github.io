## Tarea 2 - Ejercicios Unidad 1
# Reto 1
# Simulamos que la tortuga avanza 50 pasos, según el ejemplo del blog
pasos = 50
print("creando tortuga simulada que da...", pasos, "pasos")
print("-" * pasos + ">")

# Reto 2

# Simulamos que la tortuga baja 10 pasos, según el ejemplo del blog #2
pasos = 10
for i in range(pasos):
    print("|")   
print("V")

print("La tortuga bajo",pasos,"pasos.")

# Reto 3

# Simulamos que la tortuga avanza 10 pasos y baja 15 pasos
pasos_bajada = 15
pasos_adelante = 10

print("-" * pasos_adelante + ">")

for i in range(pasos_bajada):
    print(" " * pasos_adelante + "|")   

print(" " * pasos_adelante + "V")

pasos_totales = pasos_adelante + pasos_bajada

print("La tortuga avanzo", pasos_adelante,"pasos.")
print("La tortuga bajo", pasos_bajada, "pasos.")
print("La tortuga recorrió un total de", pasos_totales, "pasos.")

# Reto 4

# Creamos dos variables para pedir los pasos al usuario
pasos_adelante = int(input("¿Cuántos pasos avanza la tortuga? "))
pasos_abajo = int(input("¿Cuántos pasos baja la tortuga? "))

# Creamos dos funciones para avanzar y bajar y dibujamos el movimiento de la tortuga con print
def adelante(pasos):
    global pasos_adelante
    pasos_adelante = pasos
    print("-" * pasos + ">")


def abajo(pasos):
    for i in range(pasos):
        print(" " * pasos_adelante + "|")

    print(" " * pasos_adelante + "V")

adelante(pasos_adelante)
abajo(pasos_abajo)


# Reto 5
