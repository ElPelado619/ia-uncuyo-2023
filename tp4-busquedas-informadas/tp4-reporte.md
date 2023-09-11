# TP4: Búsquedas Informadas
- Hecho por: Agustín Yornet
- Legajo: 13921

## Presentación de boxplots
Los parámetros que presentan las grillas de obstáculos son las siguientes:
- Tasa de obstáculos: $p = 0.08$
- Tamaño de la grilla: $100 \times 100$

Una grilla se visualiza de la siguiente forma:
![Grilla](https://i.ibb.co/47HQQQx/grid.png)

En nuestro set de datos, todas las grillas son solubles.

Los resultados obtenidos por el alogritmo de Búsqueda A* se presentan a continuación.

### Resultados del Algoritmo

Se eligió como heurística a la siguiente:
$h(n) = \sqrt{(x_f-x_n)^2 + (y_f-y_n)^2}$

Se utiliza la distancia euclidiana entre el nodo actual (n) y el nodo objetivo (f), que va a ser el el mismo en cada iteración, como la heurística $h(n)$ en A*, ya que proporciona una estimación razonable del costo restante para llegar al objetivo, y A* seguirá siendo eficiente en su búsqueda, ya que es completamente observable y determinista.

![A* Boxplot](https://i.ibb.co/kHH3ZTM/ASTAR.png)

Los siguientes datos fueron obtenidos:
- Promedio: $\mu = 63$ .
- Desviación estándar: $\sigma = 24$.
- Más del 50% de las iteraciones requirieron entre 50 y 80 estados para encontrar una solución.
- Hay un sólo dato atípico.
