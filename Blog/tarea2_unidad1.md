# Tarea 2 - Ejercicios Unidad 1

## Reto 1 simula el comportamiento de la tortuga usando solo print() e input()

```python
def reto_uno(pasos):
    print("Creando tortuga simulada que da... 50 pasos")
    print("-" * pasos + ">")
    return

reto_uno(50)
```

# Reto 2 Tortuga bajando

```python
def reto_dos(pasos):
    # Dibujamos los pasos de bajada
    for i in range(pasos):
        print("|")
    
    # Colocamos la flecha hacia abajo al final
    print("V")

reto_dos(5)
```

# Reto 3 Girar y dibujar usando solo print() e input()

```python
import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)          # Gira 90 grados a la derecha
t.forward(100)
turtle.done()
```

# Reto 4 Encapsula los comportamientos anteriores usando funciones

```python
pasos_adelante = int(input("¿Cuántos pasos avanza la tortuga? "))
pasos_abajo = int(input("¿Cuántos pasos baja la tortuga? "))

def adelante(pasos):
    if pasos >= 50:
        print("No se permiten más de 50 pasos hacia adelante.")
    else:
        # Dibuja la flecha hacia adelante
        print("-" * pasos + ">")

def abajo(pasos, espacio_izquierdo):
    # Dibuja la bajada alineada con el final de la flecha
    for i in range(pasos):
        print(" " * espacio_izquierdo + "|")
    
    print(" " * espacio_izquierdo + "V")

adelante(pasos_adelante)
abajo(pasos_abajo, pasos_adelante)

pasos_totales = pasos_adelante + pasos_abajo
print("La tortuga recorrió un total de", pasos_totales, "pasos.")
```

# Reto 5 La tortuga baja las escalones

```python
pasos_adelante = int(input("¿Cuántos pasos avanza la tortuga? "))
pasos_abajo = int(input("¿Cuántos pasos baja la tortuga? "))

# Creamos una variable para saber cuántos escalones dibujar
cantidad_escalones = int(input("¿Cuántos escalones bajará la tortuga? "))

# Estas variables nos ayudan a llevar la cuenta de los espacios y pasos
espacios_acumulados = 0 
pasos_totales = 0

def adelante(pasos, espacios_al_inicio):
    # Hacemos una verificación para que no se pase de 50 pasos
    if pasos >= 50:
        print("No se permiten más de 50 pasos hacia adelante.")
        return
    else:
        # imprimimos los espacios y luego los guiones con la flecha
        espacios = " " * espacios_al_inicio
        flecha = "-" * pasos + ">"
        print(espacios + flecha)

def abajo(pasos, espacios_al_inicio):
    # Dibujamos los pasos de bajada
    for i in range(pasos):
        print(" " * espacios_al_inicio + "|")
    
    # Colocamos la flecha hacia abajo al final
    print(" " * espacios_al_inicio + "V")

# Repetimos el proceso para cada escalón
for i in range(cantidad_escalones):
    
    # 1. Avanzamos hacia adelante
    adelante(pasos_adelante, espacios_acumulados)
    
    # 2. Acumulamos los espacios para el próximo escalón
    espacios_acumulados = espacios_acumulados + pasos_adelante
    
    # 3. Bajamos hacia abajo
    abajo(pasos_abajo, espacios_acumulados)
    
    # Se suman los pasos al total
    pasos_totales += pasos_adelante + pasos_abajo

print("La tortuga recorrió un total de", pasos_totales, "pasos.")
```