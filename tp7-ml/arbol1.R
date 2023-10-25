suppressMessages(library(rpart))
suppressMessages(library(caret))
suppressMessages(library(readr))
suppressMessages(library(dplyr))
library(randomForest)

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

# Ordeno el dataset por id
data_train <- data_train[order(data_train$id),]
head(data_train)

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

# Transformo la variable inclinacion_peligrosa a factor
data_test<-data_test %>% mutate(inclinacion_peligrosa=
                                  ifelse(inclinacion_peligrosa=='1','si','no'))
data_test$inclinacion_peligrosa <-as.factor(data_test$inclinacion_peligrosa)

# Entrene un modelo de bosque aleatorio
train_formula <- inclinacion_peligrosa ~ circ_tronco_cm + especie + altura + diametro_tronco
random_forest_model <- randomForest(train_formula, data = data_train)

# Predigo sobre el set de test
preds_rf <- predict(random_forest_model, data_test, type = 'response')
head(preds_rf)

# Transformo las probabilidades en clases
preds_rf_class <- preds_rf
head(preds_rf_class)

# Genero el archivo de envío
submission_rf <- data.frame(id = data_test$id, inclinacion_peligrosa = preds_rf_class)
# Ordeno submission_rf por id
submission_rf <- submission_rf[order(submission_rf$id),]
submission_rf$inclinacion_peligrosa <- ifelse(submission_rf$inclinacion_peligrosa == "no", 0, 1)
readr::write_csv(submission_rf, "./data/arbolado-mza-dataset-envio-ejemplo-random-forest.csv")
head(submission_rf)

set.seed(100) # para que sea un ejemplo reproducible
data_validation_index<-sample(nrow(data_train),nrow(data_train)*0.1)
data_validation<-data_train[data_validation_index,]
data_train<-data_train[-data_validation_index,]

# Evaluo el modelo en el conjunto de validación
preds_rf_validation <- predict(random_forest_model, data_validation, type = 'response')

# Transformo las probabilidades en clases
preds_rf_class_validation <- preds_rf_validation

# Genero el archivo de envío para la validación
resultados_validation_rf <- data.frame(inclinacion_peligrosa = preds_rf_class_validation)
head(resultados_validation_rf)

# Armo la matriz de confusión
confusionMatrix(as.factor(resultados_validation_rf$inclinacion_peligrosa), as.factor(data_validation$inclinacion_peligrosa))
