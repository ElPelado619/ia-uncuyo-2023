# TP7: Machine Learning
- Hecho por: Agustín Yornet
- Legajo: 13921

# Ejercicio 2

## Pregunta 1
> ¿Cual es la distribución de la clase inclinacion_peligrosa?

0|1
--|--
22695|2835

## Pregunta 2
> ¿Se puede considerar alguna sección más peligrosa que otra?

Si ejecutamos el siguiente código:
```R
section_danger <- train_data %>%
  group_by(seccion) %>%
  summarize(danger_rate = mean(inclinacion_peligrosa == "1")) %>%
  arrange(desc(danger_rate))
head(section_danger)
```

Vamos a obtener el siguiente resultado:
```R
  seccion danger_rate
    <int>       <dbl>
1       2      0.145 
2       3      0.144 
3       5      0.130 
4       4      0.127 
5       1      0.111 
6       7      0.0859
```

Por lo que podríamos suponer que la sección 2 es la que representa mayor peligro según nuestros datos de entrenamiento. Sin embargo, no es posible asegurar tal afirmación.

## Pregunta 3
> ¿Se puede considerar alguna especie más peligrosa que otra?

Si ejecutamos el siguiente código:
```R
species_danger <- train_data %>%
  group_by(especie) %>%
  summarize(danger_rate = mean(inclinacion_peligrosa == "1")) %>%
  arrange(desc(danger_rate))
head(species_danger)
```

Algo similar sucede con las especies:

```R
  especie   danger_rate
  <chr>           <dbl>
1 Algarrobo      0.4   
2 Morera         0.183 
3 Catalpa        0.148 
4 Acacia SP      0.145 
5 Aguaribay      0.0996
6 Jacarand       0.0927
```

En un principio, parece ser que el algarrobo es la especie más peligrosa. Sin embargo, ante la falta de información, no sería adecuado afirmar que lo es.

# Ejercicio 3

## Inciso b

![a](histogramas/h10.png)

![a](histogramas/h20.png)

![a](histogramas/h30.png)

![a](histogramas/h50.png)

## Inciso c

### Con Inclinación Peligrosa

![a](histogramas/hs10.png)

![a](histogramas/hs20.png)

![a](histogramas/hs30.png)

![a](histogramas/hs50.png)

### Sin Inclinación Peligrosa

![a](histogramas/hn10.png)

![a](histogramas/hn20.png)

![a](histogramas/hn30.png)

![a](histogramas/hn50.png)

## Inciso c

``` R
# Crear el histograma
dev.new(width = 10, height = 10)  # Crear una ventana gráfica más grande
hist(train_data$circ_tronco_cm, breaks = 10, main = "Histograma (10 bins)", xlab = "Circunferencia del Tronco (cm)")

# Seleccionar manualmente los puntos de corte
puntos_de_corte <- c(100, 200, 300) 

# Asignar categorías
train_data$circ_tronco_cm_cat <- cut(train_data$circ_tronco_cm, 
                                     breaks = c(-Inf, puntos_de_corte, Inf), 
                                     labels = c("bajo", "medio", "alto", "muy alto"))

# Guardar el nuevo dataframe con la variable categórica
write.csv(train_data, "arbolado-mendoza-dataset-circ_tronco_cm-train.csv", row.names = FALSE)
```

