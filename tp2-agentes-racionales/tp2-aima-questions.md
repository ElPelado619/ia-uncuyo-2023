# Trabajo Práctico 2: Preguntas AIMA

## Pregunta 2.10
Considera una versión modificada del entorno de aspiradora, en la cual el agente recibe una penalización de un punto por cada movimiento. 
1. ¿Puede un agente de reflejo simple ser perfectamente racional para este entorno? Explica. 
2. ¿Qué tal un agente de reflejo con estado? Diseña un agente así. 
3. ¿Cómo cambian tus respuestas en a y b si los perceptos del agente le dan el estado limpio/sucio de cada casilla en el entorno?

### Respuestas
1. Un agente de reflejo simple no puede ser perfectamente racional porque no busca maximizar su utilidad en un entorno parcialmente observable, y aún menos si cada movimiento es penalizado y no considera el mejor movimiento posible.
2. Con el agente de reflejo con estado, sucede algo similar. Evita movimientos innecesarios al mantener un estado interno de sus acciones, pero no los realiza en función a maximizar su utilidad.
3.  En este caso, como el agente conoce en totalidad su entorno, puede tomar  las mejores decisiones posibles en cada momento del tiempo, por lo cual puede ser perfectamente racional si se desea, aunque consuma mucho tiempo y sea un objetivo poco realista.

## Pregunta 2.11

Considera una versión modificada del entorno de aspiradora, en la cual la geografía del entorno, es decir, su extensión, límites y obstáculos, son desconocidos, al igual que la configuración inicial de suciedad. *El agente puede moverse hacia arriba y hacia abajo además de izquierda y derecha*. 
1. ¿Puede un agente de reflejo simple ser perfectamente racional para este entorno? Explica. 
2. ¿Puede un agente de reflejo simple con una función de agente aleatorizada superar a un agente de reflejo simple? 
3. ¿Puedes diseñar un entorno en el cual tu agente aleatorizado tenga un mal desempeño? 
4. ¿Puede un agente de reflejo con estado superar a un agente de reflejo simple? ¿Puedes diseñar un agente racional de este tipo?

### Respuestas
1. Al igual que en el ejercicio anterior:
	> Un agente de reflejo simple no puede ser perfectamente racional porque no busca maximizar su utilidad en un entorno parcialmente observable.

2.  En efectos prácticos, el agente aleatorio no supera al agente de reflejo simple porque éste último:
	- Sensa su entorno.
	- Revisa las reglas que gobiernan al entorno.
	- Realiza una acción en base a los dos items anteriores.

	El agente aleatorio no realiza ninguna de las acciones anteriores, por lo que podría encontrarse con un casillero sucio y, aún así, moverse hacia otro sin limpiarlo.
3. El agente aleatorio puede tener mal desempeño, si se lo compara con el agente de reflejo simple, ya que limpia menos casilleros sucios en el plazo de vida útil de la aspiradora. Para una vida útil de 1000 movimientos, un agente aleatorio limpia en promedio ~$270$ cuadros cuando $n \to \infin$ en mi implementación, donde $n \times n$ es el tamaño del casillero, mientras que mi agente de reflejo simple limpia en promedio mucho más.
4. Al mantener un registro de sus acciones anteriores y de los estados que ha visitado, el agente con estado podría evitar visitar repetidamente las mismas áreas y concentrarse en explorar regiones desconocidas con potencial para encontrar áreas limpias, por lo que podría superar a un agente de reflejo simple.
