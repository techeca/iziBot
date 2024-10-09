from core import clicEnPantalla, leerTextoEnPantalla, esperar, escribir
#from core import clickEnImagen
from utils.log import log_error

class Accion:
    def __init__(self, tipo_accion, *args):
        self.tipo_accion = tipo_accion  # Ejemplo: "clicEnPantalla"
        self.args = args  # Argumentos necesarios para la acción (x, y, etc.)
    
    def ejecutar(self):
        # Diccionario de acciones posibles con sus funciones respectivas
        acciones = {
            'clicEnPantalla': clicEnPantalla,
            'leerTextoEnPantalla': leerTextoEnPantalla,
            'esperar': esperar,
            #'buscarImagenEnPantalla': clickEnImagen,
            'escribir': escribir
        }
        
        # Ejecuta la acción llamando a la función correspondiente
        if self.tipo_accion in acciones:
            acciones[self.tipo_accion](*self.args)
        else:
            log_error(f"Acción {self.tipo_accion} no reconocida.")
