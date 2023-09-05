# TP3: Búsquedas no Informadas
- Hecho por: Agustín Yornet
- Legajo: 13921

## PEAS del Agente Resuelve-Problemas por Objetivos
- Performance: Llegar al estado objetivo, utilizar la menor cantidad de movimientos posible.
- Entorno: Grilla de tamaño $n \times n$ con obstáculos que aparecen con una probabilidad $p$ entre $0 < p < 1$. 
- Acciones: Moverse arriba, abajo, izquierda y derecha.
- Sensores: Proximidad de obstáculos.

## Presentación de boxplots
Los parámetros que presentan las grillas de obstáculos son las siguientes:
- Tasa de obstáculos: $p = 0.08$
- Tamaño de la grilla: $100 \times 100$

Una grilla se visualiza de la siguiente forma:
![Grilla](https://i.ibb.co/47HQQQx/grid.png)

En nuestro set de datos, todas las grillas son solubles, pero no todos los algoritmos llegan a una solución para cada grilla.

Los resultados obtenidos por los algoritmos se presentan a continuación.

### Búsqueda por Anchura
![BFS Boxplot](https://i.ibb.co/g9rgg6D/BFS.png)
Los siguientes datos fueron obtenidos:
- Promedio: $\mu = 65$ .
- Desviación estándar: $\sigma = 29$.
- Más del 50% de las iteraciones requirieron entre 40 y 90 estados para encontrar una solución.
- No hay datos anómalos.
### Búsqueda por Profundidad
![DFS Boxplot](https://i.ibb.co/qJR5fKZ/DFS.png)
Los siguientes datos fueron obtenidos:
- Promedio: $\mu = 941$ .
- Desviación estándar: $\sigma = 792$.
- Más del 50% de las iteraciones requirieron entre 600 y 1800 estados para encontrar una solución.
- No hay datos anómalos.

### Búsqueda por Profundidad Ilimitada
![LDFS Boxplot](https://i.ibb.co/F0GPGTN/LDFS.png)

Con un límite igual al promedio del DFS, los siguientes datos fueron obtenidos:
- Promedio: $\mu = 971$ .
- Desviación estándar: $\sigma = 344$.
- Seis iteraciones pudieron encontrar una solución, pero las veinticuatro iteraciones restantes, que representan la mayor parte de la muestra, llegaron al límite de estados posibles y, por consecuente, no encontraron una solución.
- Hay datos anómalos, siendo los mismos los valores absolutos de los estados requeridos para llegar a una solución.

### Búsqueda Uniforme
![UCS Boxplot](https://i.ibb.co/g9rgg6D/UCS.png)
Los siguientes datos fueron obtenidos:
- Promedio: $\mu = 65$ .
- Desviación estándar: $\sigma = 29$.
- Más del 50% de las iteraciones requirieron entre 40 y 90 estados para encontrar una solución.
- No hay datos anómalos.

## ¿Cuál es el algoritmo más adecuado para resolver el problema?

Según los resultados que se han obtenido, los mejores algoritmos para resolver este problema son:
- Búsqueda por Anchura (BFS)
- Búsqueda Uniforme (UCS)

Como se consideran costos iguales al pasar de estado a estado, la Búsqueda por Anchura es el más adecuado por ser completo (si existe la solución, siempre la encuentra), y óptimo por minimizar la cantidad de pasos que se requieren para llegar del estado inicial al estado objetivo.

- No se elige UCS porque, bajo costos iguales, el desempeño es idéntico al BFS.
- No se eligen DFS ni DFS Limitado porque no buscan minimizar la cantidad de pasos, por lo cual no se consideran óptimos para este problema.
