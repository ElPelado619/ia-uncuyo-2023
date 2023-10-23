# TP7: Cross Validation

- Hecho por: Agustín Yornet
- Legajo: 13921

## Código de las funciones

```R
create_folds <- function(data, num_folds) {

  total_observations <- nrow(data)
  fold_size <- floor(total_observations / num_folds)
  fold_list <- list()

  for (i in 1:num_folds) {
    start_index <- (i - 1) * fold_size + 1
    end_index <- min(i * fold_size, total_observations)
    fold_indices <- start_index:end_index
    fold_list[[paste("Fold", i)]] <- fold_indices
  }
  
  return(fold_list)
}

cross_validation <- function(data, num_folds) {
  
  evaluation_metrics <- list()
  set.seed(123) 
  folds <- createFolds(data$inclinacion_peligrosa, k = num_folds)
  
  for (fold_index in 1:num_folds) {
    train_indices <- unlist(folds[-fold_index])
    test_indices <- folds[[fold_index]]
    
    train_data <- data[train_indices, ]
    test_data <- data[test_indices, ]
    
    train_formula <- inclinacion_peligrosa ~ altura + circ_tronco_cm + lat + long + seccion
    
    tree_model <- rpart(train_formula, data = train_data, method = "class")
    
    p <- predict(tree_model, test_data, type = 'class')
    
 
    confusion_matrix <- table(Real = test_data$inclinacion_peligrosa, Prediccion = p)
    
    TP <- confusion_matrix[2, 2]
    TN <- confusion_matrix[1, 1] 
    FP <- confusion_matrix[1, 2] 
    FN <- confusion_matrix[2, 1] 
    
    accuracy <- (TP + TN) / sum(confusion_matrix)
    precision <- TP / (TP + FP)
    sensitivity <- TP / (TP + FN)
    specificity <- TN / (TN + FP)
    
    evaluation_metrics[[fold_index]] <- list(
      ConfusionMatrix = confusion_matrix,
      Accuracy = accuracy,
      Precision = precision,
      Sensitivity = sensitivity,
      Specificity = specificity
    )
  }
  
  accuracy_values <- sapply(evaluation_metrics, function(metric) metric$Accuracy)
  precision_values <- sapply(evaluation_metrics, function(metric) metric$Precision)
  sensitivity_values <- sapply(evaluation_metrics, function(metric) metric$Sensitivity)
  specificity_values <- sapply(evaluation_metrics, function(metric) metric$Specificity)
  
  mean_accuracy <- mean(accuracy_values)
  mean_precision <- mean(precision_values)
  mean_sensitivity <- mean(sensitivity_values)
  mean_specificity <- mean(specificity_values)
  
  std_accuracy <- sd(accuracy_values)
  std_precision <- sd(precision_values)
  std_sensitivity <- sd(sensitivity_values)
  std_specificity <- sd(specificity_values)
  
  return(list(EvaluationMetrics = evaluation_metrics, 
              MeanAccuracy = mean_accuracy, 
              StdAccuracy = std_accuracy,
              MeanPrecision = mean_precision,
              StdPrecision = std_precision,
              MeanSensitivity = mean_sensitivity,
              StdSensitivity = std_sensitivity,
              MeanSpecificity = mean_specificity,
              StdSpecificity = std_specificity))
}
```

## Resultados

- |Accuracy|Precision|Sensitivity|Specificity
--|--|--|--|--
Media|0.887848|NaN|0|1
Desv. Estándar|0.002|Nan|0|0 

### Resultados con 5 folds

```R
Fold 1 :
    Prediccion
Real    0    1
   0 5671    0
   1  711    0
Accuracy: 0.8885929 
Precision: NaN 
Sensitivity: 0 
Specificity: 1 

Fold 2 :
    Prediccion
Real    0    1
   0 5656    0
   1  727    0
Accuracy: 0.8861037 
Precision: NaN 
Sensitivity: 0 
Specificity: 1 

Fold 3 :
    Prediccion
Real    0    1
   0 5650    0
   1  733    0
Accuracy: 0.8851637 
Precision: NaN 
Sensitivity: 0 
Specificity: 1 

Fold 4 :
    Prediccion
Real    0    1
   0 5677    0
   1  705    0
Accuracy: 0.8895331 
Precision: NaN 
Sensitivity: 0 
Specificity: 1 

Fold 5 :
    Prediccion
Real    0    1
   0 5679    0
   1  703    0
Accuracy: 0.8898464 
Precision: NaN 
Sensitivity: 0 
Specificity: 1
```