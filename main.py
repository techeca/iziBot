import pathlib
import pygubu
from rutina.accion import Accion
from utils.helpers import select_area
from tkinter import Toplevel, Label, Entry, Button

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main.ui"

class IziBot:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('main', master)
        builder.connect_callbacks(self)
        
        # Obtener referencia al Treeview de Rutina
        self.treeview_rutina = self.builder.get_object('tvRutina')
        # Configurar columnas del Treeview
        self.treeview_rutina['columns'] = ('#1', '#2')
        self.treeview_rutina.heading('#0', text='ID')
        self.treeview_rutina.column('#0', width=50)
        self.treeview_rutina.heading('#1', text='Acción')
        self.treeview_rutina.heading('#2', text='Cordenadas/Texto/Tiempo')
        # Lista que contiene las acciones de la rutina (simulación)
        self.listaAccionesUsuario = []
        
        # Obtener referencia de boton Clic
        self.btnAddClic = self.builder.get_object('btnClic')
 
        # Variable para guardar area seleccionada       
        self.temp_area = None
        # Variable para guardar texto leído
        self.texto_leido = None 
        
    def run(self):
        self.mainwindow.mainloop()
        
    def agregar_accion(self, tipo_accion, *args):
        accion = Accion(tipo_accion, *args)
        
        if len(args) == 1:
            args = args[0]  # Si solo hay un valor en args, lo desempaquetamos
        
        self.listaAccionesUsuario.append(accion)

        # Insertar nueva acción en el Treeview
        idx = len(self.listaAccionesUsuario)
        self.treeview_rutina.insert('', 'end', text=str(idx), values=(tipo_accion, str(args)))

    def add_clic(self):
        self.temp_area = select_area(self.mainwindow)
        x1, y1, x2, y2 = self.temp_area
        self.agregar_accion("clicEnPantalla", x1, y1)
        
    def add_esperar(self):
        # Crear un cuadro de diálogo para ingresar el tiempo de espera
        self.dialog = Toplevel(self.mainwindow)
        self.dialog.title("Ingrese el tiempo de espera")

        Label(self.dialog, text="Ingrese el tiempo en segundos:").pack(pady=10)

        # Entrada para el tiempo
        self.entry_tiempo = Entry(self.dialog)
        self.entry_tiempo.pack(pady=5)

        # Botón para confirmar la entrada
        Button(self.dialog, text="Aceptar", command=self.confirmar_espera).pack(pady=10)
    
    def confirmar_espera(self):
        # Obtener el valor ingresado
        tiempo = self.entry_tiempo.get()
        
        # Verificar que el valor sea un número válido
        try:
            tiempo = int(tiempo)
            if tiempo < 0:
                raise ValueError("El tiempo no puede ser negativo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return

        # Cerrar el cuadro de diálogo
        self.dialog.destroy()

        # Agregar la acción de esperar con el tiempo ingresado
        self.agregar_accion("esperar", tiempo)

    def add_escribir(self):
        # Crear ventana emergente para que el usuario ingrese el texto
        self.dialog = Toplevel(self.mainwindow)
        self.dialog.title("Ingresar texto para escribir")
        
        # Etiqueta
        label = Label(self.dialog, text="Texto a escribir:")
        label.pack(padx=10, pady=10)
        
        # Campo de entrada de texto
        self.entry_texto = Entry(self.dialog)
        self.entry_texto.pack(padx=10, pady=10)
        
        # Botón para confirmar
        boton_confirmar = Button(self.dialog, text="Confirmar", command=self.confirmar_escribir)
        boton_confirmar.pack(padx=10, pady=10)
        
    def confirmar_escribir(self):
        # Obtener el texto ingresado
        texto = self.entry_texto.get()
        
        # Verificar que se haya ingresado algún texto
        if not texto:
            print("Por favor, ingrese un texto válido.")
            return

        # Cerrar la ventana emergente
        self.dialog.destroy()
        
        # Agregar la acción de 'escribir' con el texto ingresado
        self.agregar_accion("escribir", texto)    

    def add_leer(self):
        self.temp_area = select_area(self.mainwindow)
        self.agregar_accion("leerTextoEnPantalla", self.temp_area)
        
    def iniciar_rutina(self):
        for accion in self.listaAccionesUsuario:
            accion.ejecutar()

    def eliminar_accion(self):
        # Obtener el elemento seleccionado en el Treeview
        selected_item = self.treeview_rutina.selection()

        if selected_item:
            # Obtener el índice del elemento seleccionado
            item_index = int(self.treeview_rutina.item(selected_item, "text")) - 1  # Restar 1 porque el índice es 1-based

            # Eliminar el elemento de listaAccionesUsuario
            if 0 <= item_index < len(self.listaAccionesUsuario):
                del self.listaAccionesUsuario[item_index]

            # Eliminar el elemento del Treeview
            self.treeview_rutina.delete(selected_item)

            # Actualizar el Treeview para reflejar los nuevos índices y argumentos correctamente
            self.actualizar_treeview()
        else:
            print("No se ha seleccionado ninguna acción.")

    def actualizar_treeview(self):
        # Eliminar todos los elementos del Treeview
        for item in self.treeview_rutina.get_children():
            self.treeview_rutina.delete(item)

        # Volver a agregar todos los elementos de listaAccionesUsuario
        for idx, accion in enumerate(self.listaAccionesUsuario, start=1):
            # Si los argumentos tienen un solo elemento, lo mostramos sin paréntesis
            args = accion.args if len(accion.args) > 1 else accion.args[0] if accion.args else ''
            
            # Insertar de nuevo en el Treeview
            self.treeview_rutina.insert('', 'end', text=str(idx), values=(accion.tipo_accion, str(args)))

if __name__ == "__main__":
    app = IziBot()
    app.run()