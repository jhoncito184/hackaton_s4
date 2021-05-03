# -*- coding: utf-8 -*-
import json
from json import load, decoder, dump
from time import sleep
from uuid import uuid4

data = {
    'alumnos_creados': [],
    'docentes_creados': []
}


class Usuario:
    def __init__(self, nombres, dni, edad="", notas=""):
        self.nombres = nombres
        self.dni = dni
        self.edad = edad
        self.notas = notas

    def interfaz(self):
        while True:
            print('''
                Qué deseas hacer?
                1) Crear Usuario
                2) Agregar Notas
                3) Salir
            ''')
            opcion = input('> ')
            if opcion == "1":
                self.configurar_usuario()
            elif opcion == "2":
                self.verificar_alumnos()
            elif opcion == "3":
                print("\n Gracias")
                sleep(1)
                quit()
            else:
                print("\nIntroduciste una opcion incorrecta")

    def cargar_alumnos(self):
        try:
            archivo = open("alumnos.json")
            data["alumnos_creados"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n creando registro de alumnos..")
            sleep(1)
            archivo = open("alumnos.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\n No hay alumnos creados")

    def cargar_docentes(self):
        try:
            archivo = open("docentes.json")
            data["docentes_creados"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n creando registro de docentes..")
            sleep(1)
            archivo = open("docentes.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\n No hay docentes creados")

    def verificar_alumnos(self):
        try:
            print('''Escribir el DNI del alumno?''')
            dni_alumno = input('> ')
            archivo = open("alumnos.json", "r")
            with archivo as contenido:
                mostrar_archivos = json.load(contenido)
                for linea in mostrar_archivos:
                    if dni_alumno == linea["dni"]:
                        self.agregar_notas(linea)
                        print(linea)
                        # Aquí debería guardar o actualizar el json con linea que son los datos de 1 alumno
                        return
        except Exception as error:
            print(error)

    def configurar_usuario(self):
        print('''\n¿Que tipo de usuario deseas crear?\n
            1) Alumno
            2) Docente ''')
        tipo = input("> ")
        if tipo == "1":
            self.tipo_usuario(tipo)
        elif tipo == "2":
            self.tipo_usuario(tipo)
        else:
            print("\Haz introducido una tipo erronea")

    def agregar_notas(self, datos_alumno):
        try:
            print('''Cuantas Notas se llenaran?''')
            list_notas = input('> ')
            for _ in range(int(list_notas)):
                print('''Escribir Nota: ''')
                nota = str(input('> '))
                datos_alumno['notas'].append(nota)
                # archivo = open("alumnos.json", "w")
                print(datos_alumno)
        except FileNotFoundError:
            print("\n creando registro de personajes..")
            sleep(1)
            archivo = open("personajes.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\n No hay personajes creados")

    def tipo_usuario(self, tipo):
        tipo = tipo
        if tipo == "1":
            print('''\n¿Escribir nombre y apellido''')
            nombres = input("> ")
            print('''\Escribir DNI''')
            dni = input("> ")
            self.crear_usuario_alumno(nombres, dni, tipo)
        elif tipo == "2":
            print('''\n¿Escribir nombre y apellido''')
            nombres = input("> ")
            print('''\Escribir DNI''')
            dni = input("> ")
            print('''\Escribir edad''')
            edad = input("> ")
            self.crear_usuario_docente(nombres, dni, edad, tipo)

    def crear_usuario_alumno(self, nombres, dni, tipo):
        nuevo_usuario = Usuario(nombres, dni)
        datos = {
            "id": str(uuid4()),
            "nombres": nuevo_usuario.nombres,
            "dni": nuevo_usuario.dni,
            "notas": [],
        }
        self.guardar_usuario(datos, tipo)
        print(f"\se creo el Alumno {nombres} con exito")

    def crear_usuario_docente(self, nombres, dni, edad, tipo):
        nuevo_docente = Usuario(nombres, dni, edad)
        datos = {
            "id": str(uuid4()),
            "nombres": nuevo_docente.nombres,
            "dni": int(nuevo_docente.dni),
            "edad": nuevo_docente.edad,
        }
        self.guardar_usuario(datos, tipo)
        print(f"\se creo el Docente {nombres} con exito")

    def guardar_usuario(self, datos, tipo):
        if tipo == "1":
            data['alumnos_creados'].append(datos)
            create_alumnos = data['alumnos_creados']
            archivo_alumno = open("alumnos.json", "w")
            dump(create_alumnos, archivo_alumno, indent=4)
            archivo_alumno.close()
        if tipo == "2":
            data['docentes_creados'].append(datos)
            create_docentes = data['docentes_creados']
            archivo_docente = open("docentes.json", "w")
            dump(create_docentes, archivo_docente, indent=4)
            archivo_docente.close()
