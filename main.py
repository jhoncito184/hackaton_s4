# -*- coding: utf-8 -*-
from objetos import Usuario


class Start(Usuario):
    def __init__(self):
        try:
            self.cargar_alumnos()
            self.cargar_docentes()
            self.interfaz()
        except KeyboardInterrupt:
            print("\nAplicacion Interrumpida")


Start()
