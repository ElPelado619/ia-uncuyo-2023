# Cargar la biblioteca dplyr
library(dplyr)

# Leer el archivo arbolado-mza-dataset.csv
data <- read.csv("C:/Users/usuario/Documents/RStudio/arbolado-mza-dataset.csv")

# Establecer una semilla para la reproducibilidad
set.seed(123)

# Dividir el conjunto de datos en entrenamiento (80%) y validación (20%)
train_data <- data %>% sample_frac(0.8)
validation_data <- data %>% anti_join(train_data)

# Escribir los conjuntos de datos divididos en archivos separados
write.csv(train_data, "arbolado-mendoza-dataset-train.csv", row.names = FALSE)
write.csv(validation_data, "arbolado-mendoza-dataset-validation.csv", row.names = FALSE)

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
