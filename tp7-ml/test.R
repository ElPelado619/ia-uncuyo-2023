# Cargar la biblioteca dplyr
library(dplyr)

# Leer el archivo arbolado-mza-dataset.csv
data <- read.csv("data/arbolado-mza-dataset.csv")

# Establecer una semilla para la reproducibilidad
set.seed(123)

# Dividir el conjunto de datos en entrenamiento (80%) y validación (20%)
train_data <- data %>% sample_frac(0.8)
validation_data <- data %>% anti_join(train_data)

# Escribir los conjuntos de datos divididos en archivos separados
write.csv(train_data, 
          "arbolado-mendoza-dataset-train.csv", row.names = FALSE)
write.csv(validation_data, 
          "arbolado-mendoza-dataset-validation.csv", row.names = FALSE)

# Distribución de las clases de inclinacion_peligrosa
class_distribution <- table(train_data$inclinacion_peligrosa)
print(class_distribution)

# Sección más peligrosa
head(train_data)

section_danger <- train_data %>%
  group_by(seccion) %>%
  summarize(danger_rate = mean(inclinacion_peligrosa == "1")) %>%
  arrange(desc(danger_rate))
head(section_danger)

species_danger <- train_data %>%
  group_by(especie) %>%
  summarize(danger_rate = mean(inclinacion_peligrosa == "1")) %>%
  arrange(desc(danger_rate))
head(species_danger)

# Leer el archivo de entrenamiento
train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")

# Crear un histograma con diferentes números de bins
dev.new(width = 10, height = 10)  # Crear una ventana gráfica más grande
par(mfrow = c(2, 2))  # Dividir la ventana gráfica  # Dividir la ventana gráfica # Divide la ventana gráfica en 2 filas y 2 columnas para mostrar múltiples histogramas

# Histograma con 10 bins
hist(train_data$circ_tronco_cm, breaks = 10, main = "Histograma (10 bins)", 
     xlab = "Circunferencia del Tronco (cm)")

# Histograma con 20 bins
hist(train_data$circ_tronco_cm, breaks = 20, main = "Histograma (20 bins)", 
     xlab = "Circunferencia del Tronco (cm)")

# Histograma con 30 bins
hist(train_data$circ_tronco_cm, breaks = 30, main = "Histograma (30 bins)", 
     xlab = "Circunferencia del Tronco (cm)")

# Histograma con 50 bins
hist(train_data$circ_tronco_cm, breaks = 50, main = "Histograma (50 bins)", 
     xlab = "Circunferencia del Tronco (cm)")

# Dividir en dos grupos: "si" y "no" de inclinación_peligrosa
data_si <- train_data[train_data$inclinacion_peligrosa == "1", ]
data_no <- train_data[train_data$inclinacion_peligrosa == "0", ]

# Crear histogramas separados por la clase "si"
dev.new(width = 10, height = 10)  # Crear una ventana gráfica más grande
par(mfrow = c(2, 2)) # Divide la ventana gráfica en 2 filas y 2 columnas

hist(data_si$circ_tronco_cm, breaks = 10, main = "Histograma (si, 10 bins)", 
     xlab = "Circunferencia del Tronco (cm)")
hist(data_si$circ_tronco_cm, breaks = 20, main = "Histograma (si, 20 bins)", 
     xlab = "Circunferencia del Tronco (cm)")
hist(data_si$circ_tronco_cm, breaks = 30, main = "Histograma (si, 30 bins)", 
     xlab = "Circunferencia del Tronco (cm)")
hist(data_si$circ_tronco_cm, breaks = 50, main = "Histograma (si, 50 bins)", 
     xlab = "Circunferencia del Tronco (cm)")

# Crear histogramas separados por la clase "no"
par(mfrow = c(2, 2)) # Divide la ventana gráfica en 2 filas y 2 columnas

hist(data_no$circ_tronco_cm, breaks = 10, main = "Histograma (no, 10 bins)", 
     xlab = "Circunferencia del Tronco (cm)")
hist(data_no$circ_tronco_cm, breaks = 20, main = "Histograma (no, 20 bins)", 
     xlab = "Circunferencia del Tronco (cm)")
hist(data_no$circ_tronco_cm, breaks = 30, main = "Histograma (no, 30 bins)", 
     xlab = "Circunferencia del Tronco (cm)")
hist(data_no$circ_tronco_cm, breaks = 50, main = "Histograma (no, 50 bins)", 
     xlab = "Circunferencia del Tronco (cm)")

# Crear el histograma
dev.new(width = 10, height = 10)  # Crear una ventana gráfica más grande
hist(train_data$circ_tronco_cm, breaks = 10, main = "Histograma (10 bins)", 
     xlab = "Circunferencia del Tronco (cm)")

# Seleccionar manualmente los puntos de corte
puntos_de_corte <- c(100, 200, 300)  

# Asignar categorías
train_data$circ_tronco_cm_cat <- cut(train_data$circ_tronco_cm, 
                                     breaks = c(-Inf, puntos_de_corte, Inf), 
                                     labels = c("bajo", "medio", 
                                                "alto", "muy alto"))

# Guardar el nuevo dataframe con la variable categórica
write.csv(train_data, "arbolado-mendoza-dataset-circ_tronco_cm-train.csv", 
          row.names = FALSE)

# Función para agregar una columna con valores aleatorios entre 0 y 1
add_random_prediction_prob <- function(data) {
  # Generar valores aleatorios entre 0 y 1
  data$prediction_prob <- runif(nrow(data))
  
  # Devolver el data.frame actualizado
  return(data)
}

# Aplicar la función a los conjuntos de datos de entrenamiento y validación
train_data <- add_random_prediction_prob(train_data)
validation_data <- add_random_prediction_prob(validation_data)

# Impresión de los primeros registros
head(train_data)
head(validation_data)

# Función para agregar una columna que clasifica según prediction_prob
random_classifier <- function(data) {
  # Crear la nueva columna "prediction_class" según el criterio
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  
  # Devolver el data.frame actualizado
  return(data)
}

# Aplicar la función a los conjuntos de datos de entrenamiento y validación
train_data <- random_classifier(train_data)
validation_data <- random_classifier(validation_data)

# Impresión de los primeros registros
head(train_data)
head(validation_data)

# Leer archivo de validacion de datos
validation_data_v2 <- read.csv("data/arbolado-mendoza-dataset-validation.csv")
validation_data_v2 <- add_random_prediction_prob(validation_data_v2)
validation_data_v2 <- random_classifier(validation_data_v2)
head(validation_data_v2)

# Función para calcular la precisión
confusion_matrix <- table(validation_data_v2$inclinacion_peligrosa, 
                          validation_data_v2$prediction_class)
  
print(confusion_matrix)

biggerclass_classifier <- function(data) {
  majority_class <- names(sort(table(data$inclinacion_peligrosa), decreasing = TRUE)[1])
  data$prediction_class <- majority_class
  return(data)
}

# Leer archivo de validacion de datos
validation_data_v3 <- read.csv("data/arbolado-mendoza-dataset-validation.csv")
validation_data_v3 <- biggerclass_classifier(validation_data_v3)
head(validation_data_v3)

confusion_matrix <- table(validation_data_v3$inclinacion_peligrosa, 
                          validation_data_v3$prediction_class)

print(confusion_matrix)


### CROSS VALIDATION ###

#Instalar libreria caret
install.packages("caret")

library(rpart)
library(caret)

create_folds <- function(data, num_folds) {
  # Obtener el número total de observaciones
  total_observations <- nrow(data)
  
  # Calcular el tamaño de cada fold
  fold_size <- floor(total_observations / num_folds)
  
  # Crear una lista para almacenar los índices de los folds
  fold_list <- list()
  
  # Dividir el dataframe en folds
  for (i in 1:num_folds) {
    start_index <- (i - 1) * fold_size + 1
    end_index <- min(i * fold_size, total_observations)
    
    # Obtener los índices de las observaciones para este fold
    fold_indices <- start_index:end_index
    
    # Agregar los índices a la lista
    fold_list[[paste("Fold", i)]] <- fold_indices
  }
  
  return(fold_list)
}

cross_validation <- function(data, num_folds) {
  
  # Crear una lista para almacenar las métricas de evaluación de cada fold
  evaluation_metrics <- list()
  
  # Crear los folds utilizando la función createFolds
  set.seed(123) # Establecer una semilla para la reproducibilidad
  folds <- createFolds(data$inclinacion_peligrosa, k = num_folds)
  
  for (fold_index in 1:num_folds) {
    train_indices <- unlist(folds[-fold_index])
    test_indices <- folds[[fold_index]]
    
    train_data <- data[train_indices, ]
    test_data <- data[test_indices, ]
    
    train_formula <- inclinacion_peligrosa ~ altura + circ_tronco_cm + lat + long + seccion
    
    tree_model <- rpart(train_formula, data = train_data, method = "class")
    
    p <- predict(tree_model, test_data, type = 'class')
    
    # Calcular la matriz de confusión
    confusion_matrix <- table(Real = test_data$inclinacion_peligrosa, Prediccion = p)
    
    # Calcular las métricas de evaluación
    TP <- confusion_matrix[2, 2] # Verdaderos positivos
    TN <- confusion_matrix[1, 1] # Verdaderos negativos
    FP <- confusion_matrix[1, 2] # Falsos positivos
    FN <- confusion_matrix[2, 1] # Falsos negativos
    
    accuracy <- (TP + TN) / sum(confusion_matrix)
    precision <- TP / (TP + FP)
    sensitivity <- TP / (TP + FN)
    specificity <- TN / (TN + FP)
    
    # Almacena las métricas en la lista
    evaluation_metrics[[fold_index]] <- list(
      ConfusionMatrix = confusion_matrix,
      Accuracy = accuracy,
      Precision = precision,
      Sensitivity = sensitivity,
      Specificity = specificity
    )
  }
  
  # Calcular la media y desviación estándar de las métricas de evaluación
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
df <- read.csv("data/arbolado-mza-dataset.csv")
head(df)
result <- cross_validation(df, num_folds = 5)

# Imprimir la matriz de confusión, media y desviación estándar de la precisión
for (i in 1:length(result$EvaluationMetrics)) {
  cat("Fold", i, ":\n")
  print(result$EvaluationMetrics[[i]]$ConfusionMatrix)
  cat("Accuracy:", result$EvaluationMetrics[[i]]$Accuracy, "\n\n")
  cat("Precision:", result$EvaluationMetrics[[i]]$Precision, "\n\n")
  cat("Sensitivity:", result$EvaluationMetrics[[i]]$Sensitivity, "\n\n")
  cat("Specificity:", result$EvaluationMetrics[[i]]$Specificity, "\n\n")
}

cat("Media de Accuracy:", result$MeanAccuracy, "\n")
cat("Desviación estándar de Accuracy:", result$StdAccuracy, "\n")

cat("Media de Precision:", result$MeanPrecision, "\n")
cat("Desviación estándar de Precision:", result$StdPrecision, "\n")

cat("Media de Sensitivity:", result$MeanSensitivity, "\n")
cat("Desviación estándar de Sensitivity:", result$StdSensitivity, "\n")

cat("Media de Specificity:", result$MeanSpecificity, "\n")
cat("Desviación estándar de Specificity:", result$StdSpecificity, "\n")
