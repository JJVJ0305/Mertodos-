import math
from sqlalchemy import Column, Date, Numeric, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = "jose"
PASSWORD = "12345678"
HOST = "localhost"
PORT = "5432"
DB_NAME = "metodos"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

# Modelos mapeados con las tablas ya existentes
class Sexenio2012_2018(Base):
    __tablename__ = "sexenio2012_2018"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    cotizacion = Column(Numeric(precision=10, scale=4))

class Sexenio2018_2024(Base):
    __tablename__ = "sexenio2018_2024"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    cotizacion = Column(Numeric(precision=10, scale=4))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def calcular_media_de(lista):
    n = len(lista)
    return sum(lista) / n if n > 0 else 0

def obtener_varianza_de(lista, poblacional=False):
    n = len(lista)
    if n < 2 and not poblacional:
        return 0
    if n == 0:
        return 0
    media = calcular_media_de(lista)
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    return suma_cuadrados / n if poblacional else suma_cuadrados / (n - 1)

def obtener_desviacion_estandar(lista, poblacional=False):
    return math.sqrt(obtener_varianza_de(lista, poblacional))

def procesar_sexenio(modelo, nombre_sexenio):
    registros = session.query(modelo).order_by(modelo.id).all()
    lista_cotizaciones = [float(r.cotizacion) for r in registros if r.cotizacion is not None]

    varianza = obtener_varianza_de(lista_cotizaciones, poblacional=False)
    desviacion = obtener_desviacion_estandar(lista_cotizaciones, poblacional=False)
    media = calcular_media_de(lista_cotizaciones)

    print(f"=== {nombre_sexenio} ===")
    print(f"Total registros válidos: {len(lista_cotizaciones)}")
    print(f"Media: {media:.4f}")
    print(f"Varianza (muestral): {varianza:.6f}")
    print(f"Desviación estándar (muestral): {desviacion:.6f}\n")

procesar_sexenio(Sexenio2012_2018, "Sexenio 2012-2018")
procesar_sexenio(Sexenio2018_2024, "Sexenio 2018-2024")

session.close()
