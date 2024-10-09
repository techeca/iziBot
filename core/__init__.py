from .ocr import OCR
from .image import clickEnImagen
from .pantalla import clicEnPantalla, esperar, leerTextoEnPantalla, escribir

# Variables de configuración
ruta_imagen_captura = './captura.png'
ruta_imagen_recortada = './recorte.png'

__all__ = ['OCR', 'clickEnImagen', 'clicEnPantalla', 'esperar', 'leerTextoEnPantalla', 'escribir']