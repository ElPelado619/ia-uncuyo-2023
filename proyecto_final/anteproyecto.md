# <a name="_vzai7sk315we"></a>“Buscaminas: Un enfoque en CSP y en Machine Learning”
#### <a name="_9n961f1qy8qz"></a>Code: MS-CSP-ML
## <a name="_gmp9n15xozyt"></a>Integrantes
- Mangione, Gabriel (13755)
- Yornet de Rosas, Agustín (13921)
## <a name="_60fw88x1nlg9"></a>Introducción
El juego Buscaminas, también conocido como Minesweeper, es un rompecabezas diseñado para un solo jugador, cuyo objetivo principal es despejar todas las celdas en un tablero rectangular sin activar las minas dispersas en el mismo. Buscaminas fue inicialmente lanzado en 1989 como parte del paquete de entretenimiento de Microsoft. A pesar de la percepción común de que Buscaminas implica adivinanza, en realidad se puede resolver de manera estratégica. Este rompecabezas puede ser resuelto por cualquier individuo que aplique la estrategia adecuada, y también puede ser abordado por programas que empleen soluciones algorítmicas.

El objetivo de nuestro proyecto es desarrollar un agente capaz de resolver partidas de Buscaminas, con el propósito de competir con otras soluciones algorítmicas previamente propuestas para este problema. Para lograr este objetivo, plantearemos el problema de *"resolver una partida de Buscaminas en un tablero de tamaño mxn con una cantidad de bombas igual a k"* como un problema de satisfacción de restricciones y como un problema abordable mediante machine learning.
## <a name="_jxkrjkmmk6iz"></a>Descripción del juego
Cuando un jugador inicia el juego, el programa inicializa un tablero de dimensiones m filas y n columnas, que contendrá celdas inicialmente vacías. El inicio del juego se efectúa cuando el jugador hace clic en una de las celdas, lo que conlleva a la revelación del valor asociado a dicha celda. La estrategia de juego se fundamenta en la interpretación de los valores asignados a las celdas numeradas. Los valores de estas celdas oscilan en el rango de 1 a 8, lo cual refleja el número de minas adyacentes a la celda en cuestión. Por ejemplo, una celda con el valor "8" indica que está rodeada por minas en todas sus celdas adyacentes. Si una celda se encuentra vacía, el programa procederá a mostrar todas las celdas adyacentes hasta que el perímetro de celdas accesibles esté compuesto únicamente por celdas numeradas.

El juego del Buscaminas presenta tres niveles de dificultad, definidos de la siguiente manera:

- Nivel Principiante: Se distribuyen 10 minas de forma aleatoria en un tablero de dimensiones 9 por 9.
- Nivel Intermedio: Se distribuyen 40 minas de forma aleatoria en un tablero de dimensiones 16 por 16.
- Nivel Experto: Se distribuyen 99 minas de forma aleatoria en un tablero de dimensiones 16 por 30.

El juego concluye una vez que el jugador haya despejado todas las celdas del tablero que no contienen minas. Para lograrlo, el jugador dispone de pistas proporcionadas por las celdas numeradas, así como de la capacidad de marcar las ubicaciones seguras y/o potenciales de las minas en el tablero mediante el uso de banderas (flags).
## <a name="_6aepx7ii1a3e"></a>Definición formal de Buscaminas como CSP
Sea $MinesweeperGame$ una partida de buscaminas de $m$ filas por $n$ columnas con $k$ minas dispersas al azar. Una formulación CSP [2] para MinesweeperGame puede definirse como sigue:

$$ X = \{X_{i,j}\ |\ i = 0, ..., m-1 ∧ j = 0, ...,n-1 \} $$

donde $X_{i,j}$ representa una casilla que se encuentra en la fila i y en la columna j;

$$ D = \{0, 1\} $$ 

que representa el dominio de valores que pueden ser asignados a una variable $X$, es decir, una casilla, que en este caso son:
  - Xi,j=0 (casilla sin mina)
  - Xi,j=1 (casilla con mina)
 
$$C = \{C_1, ..., C_f\}$$ 

donde $C_s= <(X_{a,b}, X_{c,d}),X_{a,b}≠X_{c,d}>$, es decir, cada restricción indica que existen dos casillas cuyos valores no son iguales y, según nuestra definición de dominio, esto significa que una casilla tiene una mina, mientras que la otra no.
## <a name="_9qgjxo8qitjx"></a>Descripción de objetivos
### <a name="_wh0nmzdzwenj"></a>Investigación de Técnicas Algorítmicas
La tarea inicial consiste en la investigación de técnicas algorítmicas para abordar el juego del Buscaminas. Este proceso se realiza con el propósito de incorporar dichas técnicas en nuestro proyecto con el fin de que puedan competir con nuestras soluciones.

Algunas estrategias que se han visto hasta el momento son:

- Random
- DFS Backtracking [1]

Sin embargo, hay otras estrategias que también pueden ser consideradas, como:

- Genetic Algorithms
- Single Point Strategies [3]
### <a name="_h98k5bopuhef"></a>Construcción de agente con enfoque en Machine Learning
La segunda tarea implica la generación de un conjunto de tableros de Buscaminas previamente despejados, destinados a entrenar a uno de los dos agentes. El propósito de este entrenamiento es permitir al agente adquirir la capacidad de reconocer patrones de resolución en el tablero, que posteriormente empleará en la resolución de partidas de Buscaminas.
### <a name="_dc0h4wotfd52"></a>Construcción de agente con enfoque en CSP
La tercera tarea implica la construcción de un agente que emplee diversas técnicas de resolución para abordar problemas de satisfacción de restricciones, incluyendo el algoritmo de propagación de restricciones AC-3 y el método de backtracking.
### <a name="_otie2opzhl45"></a>Ejecución de agentes
La presente fase se enfoca en la generación de un conjunto de tableros del juego Buscaminas, los cuales varían en dificultad. Se requiere la creación de un mínimo de 90 tableros, 30 por cada dificultad del juego. Posteriormente, se someterá a prueba cada agente en estos tableros generados, y se recopilarán los resultados para su posterior evaluación.
### <a name="_rgz838fntzjx"></a>Evaluación de agentes (métricas)
Para evaluar el rendimiento de los agentes, se utilizarán las siguientes métricas:

1. Porcentaje de partidas ganadas sobre partidas jugadas:


|**Agent**|**Easy**|**Medium**|**Hard**|**Avg**|
| :- | :- | :- | :- | :- |
|Random|0\.00%|0\.00%|0\.00%|0\.00%|
|Backtracking|0\.00%|0\.00%|0\.00%|0\.00%|
|ML|0\.00%|0\.00%|0\.00%|0\.00%|
|CSP|0\.00%|0\.00%|0\.00%|0\.00%|



1. Tiempo promedio que demanda cada agente para ganar una partida:


|**Agent**|**Easy**|**Medium**|**Hard**|**Avg**|
| :- | :- | :- | :- | :- |
|Random|0\.00s|0\.00s|0\.00s|0\.00s|
|Backtracking|0\.00s|0\.00s|0\.00s|0\.00s|
|ML|0\.00s|0\.00s|0\.00s|0\.00s|
|CSP|0\.00s|0\.00s|0\.00s|0\.00s|

1. Cantidad de estados promedios que necesitó cada agente para ganar una partida:



|**Agent**|**Easy**|**Medium**|**Hard**|**Avg**|
| :- | :- | :- | :- | :- |
|Random|0 states|0 states|0 states|0 states|
|Backtracking|0 states|0 states|0 states|0 states|
|ML|0 states|0 states|0 states|0 states|
|CSP|0 states|0 states|0 states|0 states|

De esta manera, estamos en capacidad de abordar cuestiones cruciales en el desarrollo de nuestro proyecto:

1. ¿Cuál método logra la tasa de aciertos más alta?
1. ¿Cuál método se muestra más eficiente en términos del tiempo requerido?
1. ¿Cuál método demanda la menor cantidad de exploración para alcanzar una solución deseada?

La primera pregunta ostenta un papel de suma importancia, dado que hasta la fecha no existe una solución definitiva que permita resolver todas las partidas de Buscaminas, en gran parte debido a la influencia del azar en el juego. El hallazgo de un agente altamente eficaz para el Buscaminas conlleva la resolución de problemas análogos.

Las dos preguntas subsiguientes también revisten gran relevancia, ya que el Buscaminas se cataloga como un problema NP-completo, lo que implica que su resolución óptima es computacionalmente demandante y, en muchos casos, requiere un tiempo considerablemente prolongado.

De las métricas anteriormente planteadas, subyace una nueva:

1. Porcentaje de casillas descubiertas sobre el total de casillas del tablero.


|**Agent**|**Easy**|**Medium**|**Hard**|**Avg**|
| :- | :- | :- | :- | :- |
|Random|0\.00%|0\.00%|0\.00%|0\.00%|
|Backtracking|0\.00%|0\.00%|0\.00%|0\.00%|
|ML|0\.00%|0\.00%|0\.00%|0\.00%|
|CSP|0\.00%|0\.00%|0\.00%|0\.00%|

En comparación con las métricas anteriores, esta métrica permite evaluar el desempeño de los agentes en situaciones en las que el azar puede influir en el desarrollo del juego. Un alto porcentaje de casillas descubiertas sugiere que existe un porcentaje reducido de casillas que podrían no resolverse correctamente debido al azar. Sin embargo, a través del análisis de patrones, es posible realizar predicciones precisas en tales situaciones o incluso evitar por completo estos escenarios.
### <a name="_8m2woibsv4h1"></a>Elaboración del Informe

Una vez que se hayan obtenido resultados satisfactorios que den respuesta a las interrogantes planteadas en la sección previa, procederemos a confeccionar el informe. El propósito de este informe es proporcionar una descripción detallada del juego Buscaminas, incluyendo sus instrucciones, reglas, patrones, niveles de dificultad, entre otros aspectos. Además, se expondrán los métodos utilizados en su resolución, abarcando el análisis, diseño, codificación y pruebas. También se presentarán los métodos de evaluación, que incluyen los resultados obtenidos y su representación a través de tablas y gráficos de barras, así como histogramas. Por último, se incluirán las conclusiones derivadas del proceso de desarrollo del proyecto, tanto durante su ejecución como en etapas posteriores.

### <a name="_ht7cw233l1s2"></a>Preparación de la Presentación en Diapositivas

Si nuestro proyecto satisface los criterios de evaluación establecidos por la cátedra, procederemos a la preparación de una presentación en diapositivas. En esta presentación se abordará la motivación que impulsó la realización del proyecto, se describirán las distintas etapas del mismo y se presentarán las conclusiones derivadas de la investigación y desarrollo del proyecto.


## <a name="_onln34d9leyl"></a>Listado de Actividades a Realizar
- *Actividad 1.* Investigación y recopilación de técnicas algorítmicas para resolver partidas de buscaminas. [7d]
- *Actividad 2.* Implementación de código fuente base para la ejecución de algoritmos. [3d]
- *Actividad 3.* Diseño algorítmico para resolver buscaminas por medio de técnicas CSP.* [4d]
- *Actividad 4.* Generación de tableros de buscaminas, y entrenamiento, testeo, validación de agente por medio de Machine Learning. [4d]
- *Actividad 5.* Implementación de agentes dentro del código. [4d]
- *Actividad 6.* Ejecución de agentes sobre un board set y recopilación de resultados. [2d]
- *Actividad 7.* Evaluación de resultados por medio de métricas. [2d]
- *Actividad 8.* Escritura del informe final. [7d]

![](Aspose.Words.d71ff86b-9c54-4b4e-ae2f-b17705062134.001.png)
## <a name="_cb37z39ae0ow"></a>Bibliografía
[1] Nayotama Pradipta (2022). *Implementation of Backtracking Algorithm in Minesweeper.* Link: <https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2021-2022/Makalah/Makalah-IF2211-Stima-2022-K2%20(30).pdf>

[2] Russell, S. J. 1., Norvig, P., & Davis, E. (2010). *Artificial intelligence: a modern approach.* 3rd ed. Upper Saddle River, NJ, Prentice Hall.

[3] Becerra, David J. (2015). *Algorithmic Approaches to Playing Minesweeper*. Bachelor's thesis, Harvard College. Link: <https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf>

[4] Kaye, Richard. *Minesweeper is NP-Complete.* Link: <https://www.minesweeper.info/articles/MinesweeperIsNPComplete.pdf>
