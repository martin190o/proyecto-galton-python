# Proyecto de Galton
# Simulación de una máquina de Galton usando Python

import random
import matplotlib.pyplot as plt


# Cantidad de canicas y niveles pedidos en el proyecto
canicas = 3000
niveles = 12


def galton(canicas, niveles):
    """
    Esta función simula la caída de las canicas en la máquina de Galton.

    Cada canica pasa por varios niveles.
    En cada nivel puede ir a la izquierda o a la derecha.
    Si va a la derecha, se suma 1 a su posición final.

    La función regresa una lista con la posición final de cada canica.
    """

    # Aquí se guardará la posición final de cada canica
    resultados = []

    # Repetimos el proceso por cada canica
    for _ in range(canicas):

        # Cada canica empieza en la posición 0
        posicion = 0

        # La canica pasa por todos los niveles
        for _ in range(niveles):

            # random.random() genera un número entre 0 y 1
            # Si el número es menor a 0.5, la canica se va a la derecha
            # Si no, se queda igual, como si fuera a la izquierda
            if random.random() < 0.5:
                posicion += 1

        # Guardamos la posición final donde cayó la canica
        resultados.append(posicion)

    return resultados


def grafico_resultados(resultados, niveles):
    """
    Esta función recibe los resultados de la simulación
    y crea un histograma para mostrar cuántas canicas
    cayeron en cada contenedor.
    """

    # Creamos los límites de los contenedores para que el histograma
    # muestre correctamente las posiciones de 0 a 12
    contenedores = [i - 0.5 for i in range(niveles + 2)]

    # Crear histograma
    plt.hist(resultados, bins=contenedores, edgecolor="black")

    # Título y nombres de los ejes
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Contenedor final")
    plt.ylabel("Cantidad de canicas")

    # Mostrar los números de los contenedores en el eje X
    plt.xticks(range(niveles + 1))

    # Mostrar gráfico
    plt.show()


# Programa principal
resultados = galton(canicas, niveles)
grafico_resultados(resultados, niveles)