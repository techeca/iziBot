from rutina.accion import Accion
from utils.log import log_info

class Rutina:
    def __init__(self):
        self.listaAccionesUsuario = []  # Lista que almacena las acciones

    def agregar_accion(self, tipo_accion, *args):
        accion = Accion(tipo_accion, *args)
        self.listaAccionesUsuario.append(accion)
        log_info(f"Acción '{tipo_accion}' agregada a la rutina con argumentos {args}")
    
    def ejecutar_rutina(self):
        log_info("Ejecutando rutina...")
        for accion in self.listaAccionesUsuario:
            accion.ejecutar()
        log_info("Rutina finalizada.")
