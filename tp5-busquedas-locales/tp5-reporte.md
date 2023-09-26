# TP5: Búsquedas Locales
- Hecho por: Agustín Yornet
- Legajo: 13921

## ¿En qué porcentaje los algoritmos llegaron a una solución óptima?
|Soluciones Óptimas  |4x4  |8x8|10x10|
|--|--|--|--|
|Hill Climbing  |40,00%|13,33%|0,00%  |
|Simulated Anealing|100,00%|100,00%|93,33%|
|Genetic Algorithm|100,00%|56,67%|23,33%|

## Promedio y Desviación Estándar de los tiempos de ejecución en segundos
### Promedio
|Tiempo Promedio|	4x4|	8x8|	10x10|
|--|--|--|--|
|Hill Climbing|	0.0346|	0.1273|	0.1810|
|Simulated Anealing|	0.0017|	0.0190|	0.0401
|Genetic Algorithm|	0.2029|	0.5238|	0.7339|

### Desviación Estándar
Desviación Estándar|	4x4|	8x8|	10x10
-|-|-|-
Hill Climbing|	0.0288|	0.2856|	0.2558
Simulated Anealing|	0.0014|	0.0172|	0.0454
Genetic Algorithm	|0.0267	|0.0718	|0.0125

## Promedio y Desviación Estándar de los estados explorados para llegar a una solución
### Promedio
Tiempo Promedio|	4x4|	8x8|	10x10
-|-|-|-
Hill Climbing|	6009|	8682|	10000
Simulated Anealing|	209|	1524|	2298
Genetic Algorithm|	1000|	1000|	1000

### Desviación Estándar
Desviación Estándar|	4x4|	8x8|	10x10
-|-|-|-
Hill Climbing	|4971|	3417|	5042
Simulated Anealing	|168	|1413	|2649
Genetic Algorithm	|0	|0	|0

## Boxplots de Tiempos de Ejecución

![4queens](https://i.ibb.co/0rCFyZV/queens4.png)

![8queens](https://i.ibb.co/zf56ynL/queens8.png)

![enter image description here](https://i.ibb.co/bXSD26X/queens10.png)

## Detalles del Algoritmo Genético Utilizado
### Definición de los individuos de la población
En este problema, un individuo representa una disposición de las reinas en el tablero de ajedrez. Cada individuo es una lista de longitud $N$, donde cada elemento $i$ en la lista representa la fila en la que se encuentra la reina en la columna $i$ del tablero. 

Por ejemplo, si $N = 8$, un individuo válido podría ser $[0, 4, 7, 5, 2, 6, 1, 3]$, lo que significa que hay una reina en la fila $0$ de la columna $0$, una reina en la fila $4$ de la columna $1$, y así sucesivamente.

### Estrategia de selección
En este algoritmo, se utilizará la **selección por torneo**. Se seleccionarán dos individuos al azar de la población y se compararán sus valores de adaptación (en este caso, la cantidad de conflictos entre reinas). El individuo con un valor de adaptación menor tendrá una mayor probabilidad de ser seleccionado para la reproducción.

### Estrategia de reemplazo
Se utilizará una estrategia de **reemplazo generacional**. En cada generación, se reemplazará toda la población anterior por una nueva generación de descendientes. Los individuos más aptos tendrán una mayor probabilidad de ser seleccionados como padres y, por lo tanto, de transmitir sus genes a la próxima generación.

### Operadores

- **Cruce**: Se utilizará el cruce de un solo punto para crear descendientes. Dos padres se seleccionarán mediante el método de selección por torneo, y se elegirá un punto de corte aleatorio. Los descendientes se crearán combinando las partes izquierda de un padre con las partes derecha del otro.
- **Mutación**: Se aplicará una mutación a cada descendiente con una cierta probabilidad. La mutación cambiará aleatoriamente la posición de una reina en el tablero.
### Parámetros Utilizados
Dado el algoritmo genético definido como sigue:

    genetic_algorithm(N, population_size, max_generations, mutation_rate, tournament_size)

Se utilizaron los siguientes parámetros:
- `N = [4,8,10]`
- `population_size = 5`
- `max_generations = 1000`
- `mutation_rate = 0.1`
- `tournament_size = 4`

## ¿Cuál de los tres algoritmos implementados resulta más adecuado para la solución del problema?

En el caso del problema de las N reinas, la elección entre los algoritmos depende de factores como la disponibilidad de recursos computacionales y el tiempo disponible. 

En general, los algoritmos Simulated Annealing y Genéticos tienen una mayor probabilidad de encontrar soluciones globales, pero también pueden ser más intensivos en recursos. 

Hill Climbing no es una elección adecuada porque encuentra, en su mayoría, soluciones subóptimas. Por otro lado, los algoritmos genéticos demandan mucho tiempo a pesar de obtener una gran cantidad de resultados óptimos, y la configuración de parámetros se vuelve difícil a medida que $n$ crece. 

En este caso, Simulated Anealing se comporta mucho mejor que los otros algoritmos en cuanto a cantidad de iteraciones necesarias para llegar a una solución óptima, en menor cantidad de tiempo, y con un porcentaje muy alto de soluciones óptimas encontradas en cada llamada al algoritmo. Los parámetros a elegir son más sencillos que en el caso de los algoritmos genéticos, por lo cual **Simulated Anealing resulta ser el más adecuado para este problema**. 



