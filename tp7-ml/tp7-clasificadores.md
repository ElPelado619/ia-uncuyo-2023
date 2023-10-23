# TP7: Clasificadores
- Hecho por: Agustín Yornet
- Legajo: 13921

# Matrices de Confusión

## Clasificador Aleatorio

Luego de la siguiente secuencia de instrucciones:

```R
add_random_prediction_prob <- function(data) {
  data$prediction_prob <- runif(nrow(data))
  return(data)
}


random_classifier <- function(data) {
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  return(data)
}

validation_data_v2 <- read.csv("data/arbolado-mendoza-dataset-validation.csv")
validation_data_v2 <- add_random_prediction_prob(validation_data_v2)
validation_data_v2 <- random_classifier(validation_data_v2)
confusion_matrix <- table(validation_data_v2$inclinacion_peligrosa, 
                          validation_data_v2$prediction_class)
  
print(confusion_matrix)
```

El resultado fue el siguiente:
```R
       0    1
  0 2772 2866
  1  368  376
```

Esto indica que hay:
- True Negatives: 2772
- True Positives: 376
- False Positives: 2866
- False Negatives: 368

Las métricas que se obtienen son las siguientes:
- Acurracy: $\frac{TP + TN}{total} = \frac{2772+376}{6382} = 0.4933$

- Precission: $\frac{TP}{TP+FP} = \frac{376}{376+2866} = 0.116$

- Recall: $\frac{TP}{TP+FN}=\frac{376}{744} = 0.5054$

- Specificity: $\frac{TN}{TN+FP}=\frac{2772}{5638}=0.4917$

## Clasificador por Clase Mayoritaria

Luego de la siguiente secuencia de instrucciones:

```R
biggerclass_classifier <- function(data) {
  majority_class <- names(sort(table(data$inclinacion_peligrosa), decreasing = TRUE)[1])
  data$prediction_class <- majority_class
  return(data)
}

validation_data_v3 <- read.csv("data/arbolado-mendoza-dataset-validation.csv")
validation_data_v3 <- biggerclass_classifier(validation_data_v3)

confusion_matrix <- table(validation_data_v3$inclinacion_peligrosa, 
                          validation_data_v3$prediction_class)

print(confusion_matrix)
```

La función ``biggerclass_classifier`` asumió que la clase mayoritaria es la clase $0$. Por lo tanto, la matriz de confusión se muestra como sigue:
```R
       0
  0 5638
  1  744
```
La matriz de confusión completa sería la siguiente:
```R
       0    1
  0 5638    0
  1  744    0
```
Esto indica que hay:
- True Negatives: 5638
- True Positives: 0
- False Positives: 0
- False Negatives: 744

Las métricas que se obtienen son las siguientes:
- Acurracy: $\frac{TP + TN}{total} = \frac{5638}{6382} = 0.8834$

- Precission: no hay predicciones positivas en el modelo.

- Recall: $\frac{TP}{TP+FN}=\frac{0}{744} = 0$

- Specificity: $\frac{TN}{TN+FP}=\frac{5638}{5638}=1$
