from tkinter import Toplevel, Canvas
import pyautogui

def select_area(mainwindow):
    # Oculta la ventana principal durante la selección de área
    mainwindow.withdraw()
    
    # Crear una nueva ventana para seleccionar el área
    area_selector_window = Toplevel(mainwindow)
    area_selector_window.title("Select Area")
    area_selector_window.attributes('-alpha', 0.3)  # Transparencia
    area_selector_window.attributes('-topmost', True)  # Ventana siempre en primer plano
    area_selector_window.overrideredirect(True)  # Sin bordes
    screen_width, screen_height = pyautogui.size()
    area_selector_window.geometry(f"{screen_width}x{screen_height}+0+0")
    
    # Crear un Canvas para la selección del área
    canvas = Canvas(area_selector_window, cursor="cross", bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Diccionario para almacenar las coordenadas
    coords = {'start_x': 0, 'start_y': 0, 'end_x': 0, 'end_y': 0, 'search_area': None}

    def on_button_press(event):
        coords['start_x'] = event.x
        coords['start_y'] = event.y
        coords['rect'] = canvas.create_rectangle(
            coords['start_x'], coords['start_y'],
            coords['start_x'], coords['start_y'],
            outline='red'
        )

    def on_mouse_drag(event):
        canvas.coords(coords['rect'], coords['start_x'], coords['start_y'], event.x, event.y)

    def on_button_release(event):
        # Guardar las coordenadas finales
        coords['end_x'] = event.x
        coords['end_y'] = event.y

        # Asegúrate de que x1 < x2 y y1 < y2
        x1 = min(coords['start_x'], coords['end_x'])
        y1 = min(coords['start_y'], coords['end_y'])
        x2 = max(coords['start_x'], coords['end_x'])
        y2 = max(coords['start_y'], coords['end_y'])

        # Guarda las coordenadas absolutas
        coords['search_area'] = (x1, y1, x2, y2)
        area_selector_window.destroy()

        # Mostrar mensaje en la consola
        # print(f"Área seleccionada: {coords['search_area']}")

    # Vincular los eventos al Canvas
    canvas.bind("<ButtonPress-1>", on_button_press)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_button_release)

    # Esperar a que se cierre la ventana de selección
    mainwindow.wait_window(area_selector_window)
    mainwindow.deiconify()

    # Retornar el área seleccionada
    return coords['search_area']
