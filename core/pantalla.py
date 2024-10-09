import pyautogui
import time
from core.image import capturaPantalla, recorte_Imagen
from core.ocr import OCR

def clicEnPantalla(x, y):
    pyautogui.click(x, y)

def esperar(segundos):
    time.sleep(segundos)
    
def leerTextoEnPantalla(coords):
    capturaPantalla()
    recorte_Imagen(coords)
    texto = OCR()
    return texto

def escribir(texto):
    pyautogui.write(texto)