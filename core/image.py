import cv2
import gc
import pyautogui
import time
import numpy as np
from config import ruta_imagen_captura, ruta_imagen_recortada
from utils.log import log_info, log_error

def capturaPantalla():
        captura = ruta_imagen_captura
        try:
            # Verifica si la ruta es válida
            if not captura:
                raise ValueError(
                    "La ruta para guardar la captura de pantalla no está definida.")

            # Realiza la captura de pantalla
            imagen = pyautogui.screenshot()

            # Intenta guardar la imagen en la ruta especificada
            imagen.save(captura)
            log_info(f"Captura de pantalla guardada en {captura}")

            # Elimina la imagen para liberar memoria
            del imagen

            # Pausa para asegurar que la captura se complete
            time.sleep(1)

            # Forzar la recolección de basura para liberar memoria
            gc.collect()

        except Exception as e:
            log_error(f"Error al capturar o guardar la imagen: {e}")

def recorte_Imagen(coords):
    captura = ruta_imagen_captura
    imagen_recortada = ruta_imagen_recortada

    # Cargar la imagen guardada con OpenCV
    imagen_cv2 = cv2.imread(captura)

    # Verificar si la imagen se cargó correctamente
    if imagen_cv2 is None:
        raise FileNotFoundError(
            f"No se pudo cargar la imagen en la ruta: {captura}")

    try:
        # Definir las coordenadas del recorte (x1, y1, x2, y2)
        x1, y1, x2, y2 = coords

        # Verificar que las coordenadas estén dentro del rango de la imagen
        height, width = imagen_cv2.shape[:2]
        if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
            raise ValueError(
                "Las coordenadas de recorte están fuera de los límites de la imagen.")

        # Realizar el recorte de la región de interés
        recorte = imagen_cv2[y1:y2, x1:x2]

        # Verificar si el recorte es válido
        if recorte.size == 0:
            raise ValueError(
                "El recorte resultante está vacío. Verifica las coordenadas.")

        # Guardar el recorte en un archivo
        cv2.imwrite(imagen_recortada, recorte)

    finally:
        # Liberar recursos de OpenCV
        del imagen_cv2, recorte
        gc.collect()  # Llamar al recolector de basura para limpiar memoria
        # Asegurarse de que cualquier ventana de OpenCV se cierre correctamente
        cv2.destroyAllWindows()
   
def clickEnImagen(ruta_imagen, cantidad, clic=True):
    #Busca la imagen la cantidad de veces entregada, y si es necesario le da clic    
    # Seguimiento de los intentos realizados
    intentos_realizados = 0

    while intentos_realizados < cantidad:
        
        try:
            # Incrementar los intentos realizados
            intentos_realizados += 1

            # Carga la imagen de referencia y la captura de pantalla
            imagen_referencia = cv2.imread(ruta_imagen)
            captura_pantalla = pyautogui.screenshot()
            captura_pantalla_np = np.array(captura_pantalla)
            captura_pantalla_cv2 = cv2.cvtColor(captura_pantalla_np, cv2.COLOR_RGB2BGR)

            # Verifica que las imágenes se hayan cargado correctamente
            if imagen_referencia is None or captura_pantalla_cv2 is None:
                raise ValueError("Error al cargar las imágenes.")

            # Obtén las dimensiones de la imagen de referencia
            altura, ancho, _ = imagen_referencia.shape

            # Encuentra la posición de la imagen de referencia en la captura de pantalla
            resultado = cv2.matchTemplate(captura_pantalla_cv2, imagen_referencia, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

            # Define un umbral de confianza (ajusta según tus necesidades)
            umbral_confianza = 0.8
            log_info(f"Valor de coincidencia: {max_val}")

            if max_val >= umbral_confianza:
                # Obtiene las coordenadas del centro de la imagen de referencia
                centro_x = max_loc[0] + ancho // 2
                centro_y = max_loc[1] + altura // 2

                if clic:
                # Haz clic en el centro de la imagen encontrada
                    pyautogui.click(centro_x, centro_y)
                    log_info(f"Clic realizado en ({centro_x}, {centro_y})")
                
                time.sleep(1)
                # Libera la memoria de las imágenes antes de salir
                del imagen_referencia
                del captura_pantalla_cv2
                return  # Salir de la función después de hacer clic exitosamente

            else:
                log_info("Imagen no encontrada, intentando de nuevo...")
                # Añadir un pequeño retraso antes de reintentar
                time.sleep(0.5)

            # Libera la memoria de las imágenes antes de la siguiente iteración
            del imagen_referencia
            del captura_pantalla_cv2

        except Exception as e:
            log_error(f"Error en clickEnImagen: {e}")
            break  # Salir del bucle si hay un error crítico

    raise RuntimeError(
        "Límite de intentos alcanzado o error crítico, no se encontró la imagen.")