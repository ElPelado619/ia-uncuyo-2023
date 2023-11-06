# TP7: Arbolado Público de Mendoza

- Hecho por: Agustín Yornet
- Legajo: 13921

# Preprocesamiento de Datos

El primer paso para el preprocesamiento es la carga de datos. En este caso, son dos los datasets que se incluyen en este proceso: `data_train` y `data_test`.

```R
data_train <-  readr::read_csv("./data/arbolado-mza-dataset.csv",col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double()
))

data_test <-  readr::read_csv("./data/arbolado-mza-dataset-test.csv",col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double()
))
```

Luego, se introduce un análisis de las variables que pueden afectar a la inclinación del arbolado público.

```R
summary(data_train)
table(data_train$inclinacion_peligrosa)
```

- `summary` otorga una descripción numérica de las variables que participan en el dataset de entrenamiento.
- `table(data_train$inclinacion_peligrosa)` otorga un conteo de la cantidad de árboles que tienen inclinación peligrosa y los que no. 

Por último, para este ejemplo, se eliminan las variables que se consideran innecesarias para entrenar al modelo. Las variables que se eliminaron fueron `id`, `ultima_modificacion`, `altura`, `seccion`, `nombre_seccion` y `area_seccion`.

```R
data_train <- data_train[, -c(1,3,4,9,10,11)]
```

Las variables que se utilizan para el entrenamiento son las siguientes:
```R
[1] "especie"               "circ_tronco_cm"       
[3] "diametro_tronco"       "long"                 
[5] "lat"                   "inclinacion_peligrosa"
```

La decisión de eliminar variables y dejar otras es resultado de varias pruebas sobre el dataset de entrenamiento, testeo y validación para analizar qué conjunto de variables es más factible para predecir `inclinacion_peligrosa`.

Además, luego de cada entrenamiento, se visualizan las variables que más inciden en el valor de `inclinacion_peligrosa` de la siguiente manera:

```R
> coefficients <- coef(model)
> rounded_coefficients <- round(coefficients, digits = 4)
> rounded_coefficients <- rounded_coefficients[order(rounded_coefficients, decreasing = TRUE)]
> print(rounded_coefficients)
             (Intercept)                     long 
                509.4525                  20.5922 
        especieAlgarrobo    diametro_troncoGrande 
                  1.8670                   1.5989 
  diametro_troncoMediano         especieAguaribay 
                  0.7453                   0.4153 
         especieJacarand           especieCatalpa 
                  0.2773                   0.1085 
           especieMorera           circ_tronco_cm 
                  0.0602                   0.0020 
       especieEucalyptus       especieCaducifolio 
                 -0.4955                  -0.6008
                 ...
```

# Entrenamiento del modelo

Para este problema de clasificación binaria, se utilizó el método de Regresión Logística de la librería `glm2`.

```R
model <- glm(inclinacion_peligrosa ~ ., data = data_train, family = binomial)
```

- La fórmula a utilizar es `"inclinacion_peligrosa ~ ."`.
- El argumento ``"family"`` especifica la distribución de probabilidad que se utilizará en el modelo. En este caso, utilizamos ``"binomial"`` para indicar que estamos ajustando un modelo de regresión logística cuya variable de respuesta es binaria.

Luego, con los resultados del modelo obtenido, predecimos los valores de nuestro dataset de entrenamiento.

```R
predictions <- predict(model, newdata = data_test, type = "response")
umbral <- 0.16
predictions_class <- ifelse(predictions >= umbral, 1, 0)
```

Por último, generamos nuestro dataset de envío.

```R
submission_logistic <- data.frame(id = data_test$id, inclinacion_peligrosa = predictions_class)
```

# Resultados sobre el conjunto de validación

```R
> predictions_val <- predict(model, newdata = data_validation, 
+                                      type = 'response')
> predictions_class_val <- ifelse(predictions_val >= umbral, 1, 0)
> 
> cm = confusionMatrix(data = factor(predictions_class_val), 
+                      reference = factor(data_validation$inclinacion_peligrosa))
> print(cm)
Confusion Matrix and Statistics

          Reference
Prediction    0    1
         0 2107  140
         1  735  209
                                        
               Accuracy : 0.7258        
                 95% CI : (0.71, 0.7412)
    No Information Rate : 0.8906        
    P-Value [Acc > NIR] : 1             
                                        
                  Kappa : 0.1947        
                                        
 Mcnemars Test P-Value : <2e-16        
                                        
            Sensitivity : 0.7414        
            Specificity : 0.5989        
         Pos Pred Value : 0.9377        
         Neg Pred Value : 0.2214        
             Prevalence : 0.8906        
         Detection Rate : 0.6603        
   Detection Prevalence : 0.7042        
      Balanced Accuracy : 0.6701        
                                        
       'Positive' Class : 0  
```

# Resultado obtenido en Kaggle
![Alt text](image.png)

# Descripción de la Regresión Logística

La Regresión Logística es un algoritmo de clasificación de Aprendizaje Automático que se utiliza para predecir la probabilidad de ciertas clases basadas en algunas variables dependientes. En resumen, el modelo de regresión logística calcula una suma de las características de entrada (en la mayoría de los casos, hay un término de sesgo) y calcula el logaritmo de los resultados.

La salida de la regresión logística siempre se encuentra entre 0 y 1, lo que es adecuado para una tarea de clasificación binaria. Cuanto mayor sea el valor, mayor será la probabilidad de que la muestra actual se clasifique como $clase=1$, y viceversa.

$$
h_\Theta(X) = \frac{1}{1 + e^{-\Theta X}}
$$

Como muestra la fórmula anterior, $\Theta$ es el parámetro que queremos aprender, entrenar u optimizar, y $X$ es el conjunto de datos de entrada. La salida es el valor de predicción cuando el valor está más cerca de $1$, lo que significa que la instancia es más probable que sea una muestra positiva ($y=1$). Si el valor está más cerca de $0$, esto significa que la instancia es más probable que sea una muestra negativa ($y=0$).

Para optimizar nuestra tarea, necesitamos definir una función de pérdida (función de costo u objetivo) para esta tarea. En la regresión logística, utilizamos la función de pérdida de log-likelihood.

$$
J(\Theta)=-\frac{1}{m}\sum^{i-1}_m (y^i\times log(p^i) + (1-y^i)\times log(1-p^i))
$$

Aqui, $m$ es el número de muestras en los datos de entrenamiento, $y^i$ es la etiqueta de la i-ésima muestra, y $p^i$ es el valor de predicción de la i-ésima muestra. Cuando la etiqueta de la muestra actual es 1, entonces el segundo término de la fórmula es 0. Esperamos que cuanto mayor sea el primer término, mejor sea, y viceversa. Finalmente, sumamos la pérdida de todas las muestras, tomamos el promedio y le agregamos un signo negativo. 

Queremos minimizar la función de costo cuadrático $J(\Theta)$. Cuando $J(\Theta)$ es más pequeña, significa que el modelo se ajusta mejor al conjunto de datos. Dado que $J(\Theta)$ es una función convexa, el descenso de gradiente está garantizado para encontrar un mínimo global.

En la práctica, el algoritmo de regresión logística analiza las relaciones entre variables. Asigna probabilidades a resultados discretos utilizando la función Sigmoide, que convierte los resultados numéricos en una expresión de probabilidad entre 0.0 y 1.0. La probabilidad es 0 o 1, dependiendo de si el evento ocurre o no. Para predicciones binarias, es posible dividir la población en dos grupos con un umbral de 0.5, o definido por el usuario. Todo lo que esté por encima de ese umbral se considera que pertenece al grupo A, y todo lo que esté por debajo se considera que pertenece al grupo B.