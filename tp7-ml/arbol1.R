suppressMessages(library(rpart))
suppressMessages(library(caret))
suppressMessages(library(readr))
suppressMessages(library(dplyr))
library(pROC)
library(ranger)

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

# Leo el set de entrenamiento
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

# Transformo la variable inclinacion_peligrosa a factor
data_train<-data_train %>% mutate(inclinacion_peligrosa=
                                    ifelse(inclinacion_peligrosa=='1','si','no'))
data_train$inclinacion_peligrosa <-as.factor(data_train$inclinacion_peligrosa)

# Define la fórmula de entrenamiento
train_formula <- inclinacion_peligrosa ~ . - id - ultima_modificacion - nombre_seccion - area_seccion

# Entrena el modelo de bosque aleatorio con 'ranger'
ranger_model <- ranger(train_formula, data = data_train, 
                       probability = TRUE, importance = 'impurity', 
                       num.trees = 1000, mtry = 3, min.node.size = 1, 
                       replace = FALSE, verbose = TRUE, max.depth = 10)

# Predice sobre el conjunto de prueba
preds_rf <- predict(ranger_model, data_test, type = 'response')

# Muestra las primeras filas de las predicciones
head(preds_rf)

# Genera el archivo de envío
submission_rf <- data.frame(id = data_test$id, inclinacion_peligrosa = preds_rf$predictions)

# Elimina la columna inclinacion_peligrosa.no
submission_rf <- subset(submission_rf, select = -c(inclinacion_peligrosa.no))

# Umbral para la conversión (ajusta según tus necesidades)
umbral <- 0.1112722
submission_rf$inclinacion_peligrosa <- ifelse(submission_rf$inclinacion_peligrosa.si >= umbral, 1, 0)
submission_rf <- subset(submission_rf, select = -c(inclinacion_peligrosa.si))
submission_rf <- submission_rf[order(submission_rf$id),]

# head(submission_rf)

set.seed(100) # para que sea un ejemplo reproducible
data_validation_index<-sample(nrow(data_train),nrow(data_train)*0.1)
data_validation<-data_train[data_validation_index,]
data_train<-data_train[-data_validation_index,]

# Evaluo el modelo en el conjunto de validación
preds_rf_validation <- predict(ranger_model, data_validation, type = 'response')$predictions
# head(preds_rf_validation)

# Convierte los resultados de preds_rf_validation a una sola fila
resultados_validation_rf <- ifelse(preds_rf_validation[, "si"] >= umbral, "si", "no")
# head(resultados_validation_rf)
# Armo la matriz de confusión
confusionMatrix(as.factor(resultados_validation_rf), 
                as.factor(data_validation$inclinacion_peligrosa))



roc_obj <- roc(data_validation$inclinacion_peligrosa, preds_rf_validation[, "si"])
plot(roc_obj)

# Encuentra el umbral óptimo
optimal_threshold <- coords(roc_obj, "best")$threshold
print(optimal_threshold)

readr::write_csv(submission_rf, "./data/arbolado-mza-dataset-envio-random-forest.csv")
