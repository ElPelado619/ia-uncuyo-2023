suppressMessages(library(rpart))
suppressMessages(library(caret))
suppressMessages(library(readr))
suppressMessages(library(dplyr))
library(glm2)
library(pROC)
library(ggplot2)

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

train_formula <- inclinacion_peligrosa ~ especie + diametro_tronco
logistic_model <- 
  glm(formula = train_formula, data = data_train, 
      family = binomial(link = 'logit'))
preds_logistic <- predict(logistic_model, newdata = data_test, type = 'response')

umbral <- 0.17
# Transforma las probabilidades en clases
preds_logistic_class <- ifelse(preds_logistic >= umbral, "si", "no")

# Genera el archivo de envío
submission_logistic <- data.frame(id = data_test$id, inclinacion_peligrosa = preds_logistic_class)
submission_logistic$inclinacion_peligrosa <- ifelse(submission_logistic$inclinacion_peligrosa == "no", 0, 1)
# Elimina de submission_logistic las columnas que no se piden en el envío
submission_logistic <- submission_logistic[, c("id", "inclinacion_peligrosa")]
head(submission_logistic)

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
head(preds_logistic_validation)
# Transforma las probabilidades en clases
preds_logistic_class_validation <- 
  ifelse(preds_logistic_validation >= umbral, "si", "no")


# Asegurémonos de que los factores tengan los mismos niveles
preds_logistic_class_validation <- factor(preds_logistic_class_validation, 
                                          levels = levels(data_validation$inclinacion_peligrosa))
head(preds_logistic_class_validation)
# Genera la matriz de confusión
cm = confusionMatrix(data = preds_logistic_class_validation, 
                reference = data_validation$inclinacion_peligrosa)
print(cm)

precision <- cm$table[2, 2] / (cm$table[2, 1] + cm$table[2, 2])
print(precision)

roc_obj <- roc(data_validation$inclinacion_peligrosa, preds_logistic_validation)
plot(roc_obj)

# Encuentra el umbral óptimo
optimal_threshold <- coords(roc_obj, "best")$threshold
print(optimal_threshold)

readr::write_csv(submission_logistic,"./data/arbolado-mza-dataset-envio-logistic.csv")
