import pyautogui
import time
import image
import ocr

def clicEnPantalla(x, y):
    pyautogui.click(x, y)
    #print(f"Clic en {x}, {y}")

def esperar(segundos):
    time.sleep(segundos)
    
def leerTextoEnPantalla(coords):
    image.capturaPantalla()
    image.recorte_Imagen(coords)
    texto = ocr.OCR()
    return texto

def escribir(texto):
    pyautogui.write(texto)