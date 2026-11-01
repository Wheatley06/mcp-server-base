## #######################################################################################################
##
## @copyright Big Data Academy [info@bigdataacademy.org]
## @professor Alonso Melgarejo [alonsoraulmgs@gmail.com]
##
## #######################################################################################################

## #######################################################################################################
## @section Librerías
## #######################################################################################################

#Utilitario para trabajar con JSONs
import json

#Utilitario para leer archivos de datos en dataframes
import pandas as pd

#Utilitario para procesar dataframes con SQL
import duckdb

#Utilitario para acceder a la configuración del proyecto
from modules.conf import conf

## #######################################################################################################
## @section Funciones Utilitarias
## #######################################################################################################

##########################################################################################################
# Lee todos los registros del archivo de datos en un Dataframe
#
# @return DataFrame con todos los registros leídos
##########################################################################################################
def leerArchivoDeDatos():
    
    #Leemos el archivo CSV
    df = pd.read_csv(
        conf.CONF_RUTA_CLIENTES,
        dtype = conf.CONF_TIPOS_DATOS,
        encoding = "utf-8",
    )

    #Devolvemos el DataFrame con todos los registros leídos
    return df

##########################################################################################################
# Ejecuta una consulta SQL en el DataFrame llamado df
#
# @param df DataFrame sobre el cual se ejecutará la consulta SQL
# @param consultaSQL Consulta SQL a ejecutar
# @return DataFrame con el resultado de la consulta SQL
##########################################################################################################
def ejecutarConsultaSQLEnDataframe(
    df = None,
    consultaSQL = None,
):
    #Ejecutamos la consulta SQL en el DataFrame llamado df
    dfResultado = duckdb.sql(consultaSQL).df()

    #Devolvemos el resultado
    return dfResultado


##########################################################################################################
# Convierte un DataFrame en una lista de diccionarios legible
#
# @param df DataFrame a convertir
# @return Lista de diccionarios con los datos del DataFrame
##########################################################################################################
def resultadosEnListaLegible(
    df = None,
):  
    #Convertimos el DataFrame a un JSON en formato de registros
    registros = df.to_json(
        orient = "records", #Formato de registros para JSON (filas)
        date_format = "iso", #Formato de fecha ISO 8601 que tiene la estructura YYYY-MM-DDTHH:MM:SS
        force_ascii = False, #No forzar ASCII, mantener caracteres Unicode, es decir permitir caracteres especiales y acentos
    )

    #Cargamos el JSON en una lista de diccionarios legible
    resultado = json.loads(registros)

    #Devolvemos la lista de diccionarios legible
    return resultado

##########################################################################################################
# Obtiene el esquema de metadatos del DataFrame de clientes
#
# @return Diccionario con el esquema de metadatos del DataFrame de clientes
##########################################################################################################
def obtenerEsquemaDeMetadatos():
    #Leemos el archivo de datos
    df = leerArchivoDeDatos()

    #Construimos el esquema con información que le será útil al cliente MCP
    esquema = {
        "tabla": "df",
        "columnas": df.dtypes.astype(str).to_dict(),
    }

    #Devolvemos el esquema como un diccionario
    return esquema