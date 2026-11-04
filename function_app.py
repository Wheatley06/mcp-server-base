## #######################################################################################################
##
## @copyright Big Data Academy [info@bigdataacademy.org]
## @professor Alonso Melgarejo [alonsoraulmgs@gmail.com]
##
## #######################################################################################################

## #######################################################################################################
## @section Librerías
## #######################################################################################################

#Importamos las librerías necesarias para Azure Functions y el Blueprint de herramientas MCP
import azure.functions as func

#Importamos el Blueprint de herramientas MCP desde el módulo correspondiente
from modules.tools.mcp_tools import bp

## #######################################################################################################
## @section Azure Functions con Servidor MCP
## #######################################################################################################

#Creamos la aplicación de Azure Functions
app = func.FunctionApp()

#Registramos las tools del servidor MCP
app.register_functions(bp)