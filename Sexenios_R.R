library(DBI)
library(RPostgres)

# Establecer la conexión
conexion <- dbConnect(
  RPostgres::Postgres(),
  dbname = "metodos",
  host = "localhost",
  port = 5432,
  user = "jose",
  password = "12345678"
)

procesar_sexenio <- function(conexion, nombre_tabla, nombre_sexenio) {
  # Consultar datos ordenados por id
  query <- sprintf("SELECT * FROM %s ORDER BY id", nombre_tabla)
  datos <- dbGetQuery(conexion, query)
  
  # Extraer la columna cotización y omitir valores nulos
  cotizaciones <- datos[["cotizacion"]]
  cotizaciones <- cotizaciones[!is.na(cotizaciones)]
  
  media <- mean(cotizaciones)
  varianza <- var(cotizaciones)
  desviacion <- sd(cotizaciones)
  
  cat(sprintf("=== %s ===\n", nombre_sexenio))
  cat(sprintf("Total registros válidos: %d\n", length(cotizaciones)))
  cat(sprintf("Media: %.4f\n", media))
  cat(sprintf("Varianza (muestral): %.6f\n", varianza))
  cat(sprintf("Desviación estándar (muestral): %.6f\n\n", desviacion))
  
  return(datos)
}

datos_2012_2018 <- procesar_sexenio(conexion, "sexenio2012_2018", "Sexenio 2012-2018")
datos_2018_2024 <- procesar_sexenio(conexion, "sexenio2018_2024", "Sexenio 2018-2024")

write.csv(datos_2012_2018, file = "/tmp/sexenio_2012_2018_exportado.csv", row.names = FALSE)
write.csv(datos_2018_2024, file = "/tmp/sexenio_2018_2024_exportado.csv", row.names = FALSE)

# Cerrar la conexión con la base de datos
dbDisconnect(conexion)
