# TP7: Reporte ID3
- Hecho por: Agustín Yornet
- Legajo: 13921

# Resultados sobre tennis.csv

Output de consola:
```
X_2 <= high ? 0.125
    left:X_0 <= rainy ? 0.2222222222222222
        left:yes
        right:no
    right:X_3 <= False ? 0.05555555555555547
        left:yes
        right:no
```

Reescrito a lenguaje natural:
```
¿La humedad es alta?
    Sí: ¿Está lloviendo?        
        Sí: JUGAR
        No: NO JUGAR
    No: ¿Hay viento?
        Si: NO JUGAR
        No: JUGAR
```
> Nota: se negó la pregunta "¿Hay viento?" para que sea más entendible en lenguaje natural.

¿Qué accuracy tiene el árbol?

- Ha acertado correctamente a 8 de los 10 casos, por lo que tiene un *accuracy* de 0.8.

# ¿Cómo se trabajan con datos de tipo real?

Para abordar los árboles de decisión, se utilizan datos discretos o categóricos, y cada característica tiene un conjunto finito de categorías. Sin embargo, para trabajar con datos de tipo real en árboles de decisión, se utilizan algunas estrategias, como la **división de nodos**. 

La división de nodos consiste en dividir los nodos en rangos o intervalos. Esto implica definir *umbrales* en los datos continuos para separarlos en subconjuntos. Por ejemplo, si se tiene una característica de altura, se pueden definir intervalos como *"mayor a 1.75 metros"*, *"menor o igual a 1.75 metros"*.

Al utilizar esta estrategia, es fundamental disminuir la varianza cuando dividimos los nodos en subconjuntos, así como podar el árbol para evitar el overfitting.

Por ejemplo, en el archivo *tennis.csv*, lo más probable es que se hayan definido umbrales para definir si hay humedad alta o normal, así como para definir si hay viento o no. La idea es aplicar la misma estrategia sobre datasets con variables continuas.
