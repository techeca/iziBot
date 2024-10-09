import pytesseract
import cv2
from core import ruta_imagen_recortada

def OCR():
    # Configura la ruta al ejecutable de Tesseract (puede variar según tu instalación)
    ruta_tesseract = "C:\Program Files\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = fr'{ruta_tesseract}\tesseract.exe'

    # Cargar la imagen y convertirla a escala de grises
    imagen = cv2.imread(ruta_imagen_recortada)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Realizar OCR en la imagen en escala de grises
    texto = pytesseract.image_to_string(gray)

    # Liberar la imagen de la memoria
    cv2.destroyAllWindows()
    del gray
    del imagen

    # Retornar el texto procesado
    return texto    