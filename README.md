# Simulación de la Máquina de Galton

## Descripción del proyecto

Este proyecto consiste en una simulación de la Máquina de Galton usando Python.

La Máquina de Galton es un experimento que permite observar cómo varios resultados aleatorios pueden formar una distribución parecida a una campana. En este programa se simula la caída de varias canicas a través de distintos niveles de obstáculos.

Cada canica puede moverse hacia la izquierda o hacia la derecha en cada nivel. Al final, dependiendo de cuántas veces se movió hacia la derecha, cae en un contenedor diferente.

## Objetivo del proyecto

El objetivo principal es simular una Máquina de Galton con:

- 3000 canicas
- 12 niveles de obstáculos
- 13 contenedores finales
- Un histograma para mostrar los resultados

## Herramientas utilizadas

- Python
- Librería `random`
- Librería `matplotlib`

## ¿Cómo funciona el programa?

El programa utiliza dos funciones principales.

### Función `galton(canicas, niveles)`

Esta función se encarga de simular la caída de las canicas.

Primero se crea una lista vacía llamada `resultados`. Después, cada canica empieza en la posición 0 y pasa por 12 niveles.

En cada nivel se usa `random.random()` para generar una decisión aleatoria. Si el número generado es menor a 0.5, la canica se mueve hacia la derecha y su posición aumenta en 1. Si no, se considera que la canica va hacia la izquierda y su posición no cambia.

Cuando la canica termina de pasar por todos los niveles, se guarda su posición final en la lista de resultados.

### Función `grafico_resultados(resultados, niveles)`

Esta función recibe la lista con los resultados finales de las canicas y genera un histograma usando `matplotlib`.

El histograma muestra cuántas canicas cayeron en cada contenedor. También incluye título, nombre del eje X y nombre del eje Y.

## Resultado esperado

El resultado esperado es una gráfica con forma parecida a una campana.

Esto sucede porque es más probable que las canicas caigan en los contenedores centrales. Para caer en los extremos, una canica tendría que irse muchas veces hacia el mismo lado, lo cual es menos probable.

## Cómo ejecutar el programa

Para ejecutar el programa se necesita tener Python instalado.

También se necesita instalar la librería `matplotlib` con el siguiente comando:

```bash
pip install matplotlib
```

Después se ejecuta el archivo de Python:

```bash
python Martin_Medina_proyectoM3.py
```

## Aprendizajes

Con este proyecto practiqué el uso de ciclos, condicionales, listas, funciones y números aleatorios en Python.

También aprendí a separar el programa en funciones para que el código sea más ordenado. Una función se encarga de calcular los resultados de la simulación y otra función se encarga de graficarlos.

Además, entendí cómo un proceso aleatorio puede generar un patrón cuando se repite muchas veces.

## Reflexión del bootcamp

Hasta este punto del bootcamp he aprendido a resolver problemas usando lógica de programación. Al principio puede parecer complicado, pero al dividir el problema en pasos más pequeños es más fácil entender qué debe hacer cada parte del programa.

Este proyecto me ayudó a reforzar mi comprensión sobre funciones, ciclos y el uso de librerías externas en Python. También aprendí la importancia de documentar mi proyecto en GitHub para que otras personas puedan entender cómo funciona.

## Autor

Martin Medina