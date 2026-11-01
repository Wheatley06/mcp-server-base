## #######################################################################################################
##
## @copyright Big Data Academy [info@bigdataacademy.org]
## @professor Alonso Melgarejo [alonsoraulmgs@gmail.com]
##
## #######################################################################################################

## #######################################################################################################
## @section Librerías
## #######################################################################################################

#Utilitario para trabajar con funciones de Azure Functions
import azure.functions as func

#Utilitario para trabajar con JSONs
import json

#Utilitario para acceder a la configuración del proyecto
from modules.conf import conf

#Utilitario para acceder a las funciones utilitarias del proyecto
from modules.util import funciones_utilitarias

## #######################################################################################################
## @section Blueprint
## #######################################################################################################

#Creamos el Blueprint que agrupa las herramientas
#El blueprint se utiliza para agrupar las herramientas relacionadas en un solo objeto
#Podemos entenderlo como un contenedor que organiza y agrupa las herramientas relacionadas
bp = func.Blueprint()

## #######################################################################################################
## @section Herramientas MCP (Tools)
## #######################################################################################################

##########################################################################################################
# Herramienta para obtener el esquema de clientes
#
# @param context Contexto enviado por el cliente MCP
# @return Esquema de la tabla de clientes en formato JSON
##########################################################################################################
@bp.mcp_tool_trigger(
    #Nombre de la variable que contiene todas las sub-variables recibidas
    arg_name = "context", 

    #Nombre de la herramienta MCP
    tool_name = "tool_obtener_esquema_clientes", 

    #Descripción de la herramienta MCP
    description = ("""
        Obtiene las columnas y los tipos de datos del DataFrame de pandas.
        Consulta esta herramienta antes de preparar el SQL. La tabla siempre se llama df.
        SALARIO es mensual y MONTO_TOTAL_COMPRAS es acumulado, ambos en USD. 
    """),

    #Propiedades de la herramienta MCP, es decir las sub-variables que se esperan dentro de "context"
    tool_properties = "[]",
)
def tool_obtener_esquema_clientes(context: str) -> str:
    
    ##################################################################################################
    # @section Extracción de parámetros
    ##################################################################################################

    #No aplica, ya que esta herramienta no requiere parámetros adicionales del contexto

    ##################################################################################################
    # @section Procesamiento
    ##################################################################################################
    
    #Obtenemos el esquema de metadatos
    esquema = funciones_utilitarias.obtenerEsquemaDeMetadatos()

    ##################################################################################################
    # @section Resultados como texto
    ##################################################################################################

    #Convertimos el resultado a texto JSON
    outputTool = json.dumps(esquema, ensure_ascii = False)

    #Devolvemos el resultado como texto
    return outputTool


##########################################################################################################
# Herramienta para consultar clientes mediante SQL
#
# @param context Contexto enviado por el cliente MCP
# @return Registros de la tabla de clientes en formato JSON
##########################################################################################################
@bp.mcp_tool_trigger(
    #Nombre de la variable que contiene todas las sub-variables recibidas
    arg_name = "context",

    #Nombre de la herramienta MCP
    tool_name = "tool_consultar_clientes",

    #Descripción de la herramienta MCP
    description = ("""
        Ejecuta una consulta SQL en DuckDB sobre la tabla df y devuelve los registros.
        Obtén primero el esquema y utiliza consultas de lectura SELECT.
    """),

    #Propiedades de la herramienta MCP, es decir las sub-variables que se esperan dentro de "context"
    tool_properties = json.dumps([
        #Para este ejemplo, tenemos solo una propiedad que es la consulta SQL
        {
            "propertyName": "consultaSQL",
            "propertyType": "string",
            "description": """
                Consulta SQL de lectura lista para ser ejecutada por DuckDB.
                Usa df como nombre de tabla. 
                Solo coloca la consulta SQL, no agregues ningún tipo de comentarios.
            """,
            "isRequired": True,
        }
    ]),
)
def tool_consultar_clientes(context: str) -> str:

    ##################################################################################################
    # @section Extracción de parámetros
    ##################################################################################################
    
    #Leemos en un JSON los paraámetros enviados por el cliente MCP
    contenido = json.loads(context)
    
    #Extraemos cada parámetro
    consultaSQL = contenido["arguments"]["consultaSQL"]

    ##################################################################################################
    # @section Procesamiento
    ##################################################################################################

    #Leemos los datos
    df = funciones_utilitarias.leerArchivoDeDatos()

    #Ejecutamos la consulta
    dfResultado = funciones_utilitarias.ejecutarConsultaSQLEnDataframe(
        df = df,
        consultaSQL = consultaSQL
    )

    ##################################################################################################
    # @section Resultados como texto
    ##################################################################################################

    #Convertimos el resultado en una lista de diccionarios
    resultado = funciones_utilitarias.resultadosEnListaLegible(
        df = dfResultado,
    )

    #Devolvemos el resultado como texto
    outputTool = json.dumps(resultado, ensure_ascii = False)

    # Devolvemos los registros como texto JSON
    return outputTool
