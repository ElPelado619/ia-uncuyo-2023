suppressMessages(library(rpart))
suppressMessages(library(caret))
suppressMessages(library(readr))
suppressMessages(library(dplyr))
library(randomForest)
library(glm2)

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

logistic_model <- 
  glm(inclinacion_peligrosa ~ lat + long + circ_tronco_cm
      + especie + altura, data = data_train, 
      family = binomial(link = 'logit'))
preds_logistic <- predict(logistic_model, newdata = data_test, type = 'response')

# Transforma las probabilidades en clases
preds_logistic_class <- ifelse(preds_logistic >= 0.1128359, "si", "no")

# Genera el archivo de envío
submission_logistic <- data.frame(id = data_test$id, inclinacion_peligrosa = preds_logistic_class)
submission_logistic$inclinacion_peligrosa <- ifelse(submission_logistic$inclinacion_peligrosa == "no", 0, 1)
# Elimina de submission_logistic las columnas que no se piden en el envío
submission_logistic <- submission_logistic[, c("id", "inclinacion_peligrosa")]
readr::write_csv(submission_logistic,"./data/arbolado-mza-dataset-envio-logistic.csv")
head(submission_logistic)

# Correccion de archivo
library(readr)
arbolado_mza_dataset_envio_ejemplo_logistic <- read_csv("data/arbolado-mza-dataset-envio-ejemplo-logistic.csv")
View(arbolado_mza_dataset_envio_ejemplo_logistic)
# Deja unicamente de arbolado_mza_dataset_envio_ejemplo_logistic las columnas 2 y 3
arbolado_mza_dataset_envio_ejemplo_logistic <- arbolado_mza_dataset_envio_ejemplo_logistic[,c(2,3)]
submission_logistic <- arbolado_mza_dataset_envio_ejemplo_logistic

# Busca cuantos arboles tienen inclinacion peligrosa
table(submission_logistic$inclinacion_peligrosa)

# Imprime las columnas de submission_logistic
colnames(submission_logistic)

# Imprime la cantidad de columnas de submission_logistic
length(colnames(submission_logistic))


set.seed(100) # para que sea un ejemplo reproducible
data_validation_index<-sample(nrow(data_train),nrow(data_train)*0.1)
data_validation<-data_train[data_validation_index,]
data_train<-data_train[-data_validation_index,]

# Evalúa el modelo en el conjunto de validación
preds_logistic_validation <- predict(logistic_model, newdata = data_validation, 
                                     type = 'response')

# Transforma las probabilidades en clases
preds_logistic_class_validation <- 
  ifelse(preds_logistic_validation >= 0.1128359, "si", "no")


# Asegurémonos de que los factores tengan los mismos niveles
preds_logistic_class_validation <- factor(preds_logistic_class_validation, 
                                          levels = levels(data_validation$inclinacion_peligrosa))

# Genera la matriz de confusión
confusionMatrix(data = preds_logistic_class_validation, reference = data_validation$inclinacion_peligrosa)


library(pROC)

roc_obj <- roc(data_validation$inclinacion_peligrosa, preds_logistic_validation)
plot(roc_obj)

# Encuentra el umbral óptimo
optimal_threshold <- coords(roc_obj, "best")$threshold
print(optimal_threshold)
# Utiliza el umbral óptimo
preds_logistic_class <- ifelse(preds_logistic >= optimal_threshold, "si", "no")


### IMPORTANCIA DE CARACTERISTICAS
# Ajusta un modelo de Random Forest
model_rf <- randomForest(inclinacion_peligrosa ~ ., data = data_train)

# Calcula la importancia de características
feature_importance <- importance(model_rf)

# Ordena la importancia de características
feature_importance <- feature_importance[order(feature_importance[,1], decreasing = TRUE),]
# Muestra la importancia de características
print(feature_importance)
