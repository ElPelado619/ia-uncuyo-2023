suppressMessages(library(rpart))
suppressMessages(library(caret))
suppressMessages(library(readr))
suppressMessages(library(dplyr))
library(glm2)
library(pROC)

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

summary(data_train)
table(data_train$inclinacion_peligrosa)

colnames(data_train)
# 4: Altura 6: Diametro_tronco
data_train <- data_train[, -c(1,3,4,9,10,11)]
colnames(data_train)

model <- glm(inclinacion_peligrosa ~ ., data = data_train, family = binomial)
summary(model)

coefficients <- coef(model)
rounded_coefficients <- round(coefficients, digits = 4)
rounded_coefficients <- rounded_coefficients[order(rounded_coefficients, decreasing = TRUE)]
print(rounded_coefficients)

predictions <- predict(model, newdata = data_test, type = "response")

umbral <- 0.16
predictions_class <- ifelse(predictions >= umbral, 1, 0)

submission_logistic <- data.frame(id = data_test$id, inclinacion_peligrosa = predictions_class)
head(submission_logistic)

set.seed(123) 
data_validation_index<-sample(nrow(data_train),nrow(data_train)*0.1)
data_validation<-data_train[data_validation_index,]
data_train<-data_train[-data_validation_index,]

predictions_val <- predict(model, newdata = data_validation, 
                                     type = 'response')
predictions_class_val <- ifelse(predictions_val >= umbral, 1, 0)

cm = confusionMatrix(data = factor(predictions_class_val), 
                     reference = factor(data_validation$inclinacion_peligrosa))
print(cm)

precision <- cm$table[2, 2] / (cm$table[2, 1] + cm$table[2, 2])
print(precision)

# ROC
roc_validation <- roc(data_validation$inclinacion_peligrosa, predictions_val)
plot(roc_validation, col = "blue", main = "ROC Logistic Regression")
auc(roc_validation)

optimal_threshold <- coords(roc_validation, "best")$threshold
print(optimal_threshold)

readr::write_csv(submission_logistic,"./data/arbolado-mza-dataset-envio-logistic.csv")
