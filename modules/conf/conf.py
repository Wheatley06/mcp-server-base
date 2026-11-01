## #######################################################################################################
##
## @copyright Big Data Academy [info@bigdataacademy.org]
## @professor Alonso Melgarejo [alonsoraulmgs@gmail.com]
##
## #######################################################################################################

## #######################################################################################################
## @section Librerías
## #######################################################################################################

#Utilitario para navegar entre rutas
from pathlib import Path

## #######################################################################################################
## @section Variables de configuración
## #######################################################################################################

#Nombre del proyecto
CONF_NOMBRE_PROYECTO = "BIG DATA ACADEMY"

#Ruta del proyecto y del archivo de clientes
CONF_RUTA_PROYECTO = Path(__file__).resolve().parents[2]
CONF_RUTA_CLIENTES = CONF_RUTA_PROYECTO / "datos" / "clientes_100.csv"

#Tipos de datos para leer el archivos de datos
CONF_TIPOS_DATOS = {
    "DNI": "string",
    "NOMBRES": "string",
    "APELLIDOS": "string",
    "EDAD": "int64",
    "SALARIO": "float64",
    "CIUDAD": "string",
    "FECHA_REGISTRO": "string",
    "CANAL_CAPTACION": "string",
    "CANTIDAD_COMPRAS": "int64",
    "MONTO_TOTAL_COMPRAS": "float64",
    "FECHA_ULTIMA_COMPRA": "string",
}