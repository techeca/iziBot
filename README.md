# IziBot
Bot simple para automatizar tareas, consta con acciones simples como escribir, esperar, clic y lectura con OCR.

## Pre-Requisitos
Descargar e instalar [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

## Descargas
--onefile  
[Ejecutable único](https://github.com/techeca/iziBot/releases/download/v1.0.0/main.exe)

--onedir  
[Carpeta completa](https://github.com/techeca/iziBot/releases/download/v1.0.0/iziBot.rar)

## Uso
1.- Ejecutar `main.exe` para iniciar  el programa.
2.- Ingresa la acciones que deseas para generar una rutina.
3.- Inicia la rutina. 

### Clic
Realiza un Clic en el lugar especificado.

### Esperar
Espera el tiempo especificado.

### Escribir
Escribe el texto especificado.

## Core
Las funciones principales del `core` pueden ser reutilizadas en otros proyectos de la siguiente forma:

### Estructura

Core: Contiene las funciones principales para realizar las tareas de automatización.  

Utils: Funcione necesarias para apoyar la automatización.

Rutina: Clases para la adminitración de acciones de una rutina.

`NOTA` Por defecto se genera una imagen de captura de pantalla y recorte en la raíz del proyecto, esta ruta puede ser modificada en `config.py`.

```py
ruta_imagen_captura = './captura.png'
ruta_imagen_recortada = './recorte.png'
```

Instalar
```bash
git clone https://github.com/techeca/iziBot.git
```

### Ejemplo de Funciones
clicEnPantalla
```py
from core import clicEnPantalla
clicEnPantalla(100, 200) #Coordenadas x1, y1
```

esperar
```py
from core import esperar
esperar(10) #Tiempo en segundos
```

escribir
```py
from core import escribir
escribir('Hola Mundo!') #Cadena de texto
```

leerTextoEnPantalla
```py
from core import leerTextoEnPantalla,
leerTextoEnPantalla(100, 200, 250, 100) #Coordenadas x1, y1, x2, y2
``` 
Devuelve una `cadena de texto` leído con OCR.

