 # Función para calcular y mostrar el resumen de la regresión lineal
regresion_lineal <- function(x, y) {
  # Crear un data frame con los datos
  datos <- data.frame(x = x, y = y)

  # Ajustar el modelo lineal (y ~ x)
  modelo <- lm(y ~ x, data = datos)

  # Retornar el objeto del modelo
  return(modelo)
}

x <- c()
y <- c()

modelo <- regresion_lineal(x, y)

modelo
