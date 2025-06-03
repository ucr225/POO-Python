import os
import re
from datetime import datetime

class Estudiante:
    def __init__(self, nombre, apellido, edad, carnet, carrera, promedio,
                 creditos_aprobados, materias_cursadas, fecha_ingreso,
                 estado_academico, beca, correo_electronico, telefono,
                 direccion, nacionalidad):
        # atributos privados 
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__carnet = carnet
        self.__carrera = carrera
        self.__promedio = promedio
        self.__creditos_aprobados = creditos_aprobados
        self.__materias_cursadas = materias_cursadas
        self.__fecha_ingreso = fecha_ingreso
        self.__estado_academico = estado_academico
        self.__beca = beca
        self.__correo_electronico = correo_electronico
        #atributos publicos
        self.telefono = telefono
        self.direccion = direccion
        self.nacionalidad = nacionalidad


    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_edad(self):
        return self.__edad

    def get_carnet(self):
        return self.__carnet

    def get_carrera(self):
        return self.__carrera

    def get_promedio(self):
        return self.__promedio

    def get_creditos_aprobados(self):
        return self.__creditos_aprobados

    def get_materias_cursadas(self):
        return self.__materias_cursadas

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def get_estado_academico(self):
        return self.__estado_academico

    def get_beca(self):
        return self.__beca

    def get_correo_electronico(self):
        return self.__correo_electronico


    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self.__nombre = nuevo_nombre.strip()
        else:
            print("Error: El nombre no puede estar vacío.")

    def set_apellido(self, nuevo_apellido):
        if nuevo_apellido.strip():
            self.__apellido = nuevo_apellido.strip()
        else:
            print("Error: El apellido no puede estar vacío.")

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 16 <= nueva_edad < 100:
            self.__edad = nueva_edad
        else:
            print("Error: La edad debe ser un número entero entre 16 y 99.")

    def set_carnet(self, nuevo_carnet):
        if nuevo_carnet.strip():
            self.__carnet = nuevo_carnet.strip()
        else:
            print("Error: El carnet no puede estar vacío.")

    def set_carrera(self, nueva_carrera):
        if nueva_carrera.strip():
            self.__carrera = nueva_carrera.strip()
        else:
            print("Error: La carrera no puede estar vacía.")

    def set_promedio(self, nuevo_promedio):
        if isinstance(nuevo_promedio, (int, float)) and 0.0 <= nuevo_promedio <= 20.0:
            self.__promedio = nuevo_promedio
        else:
            print("Error: El promedio debe ser un número entre 0 y 20.")

    def set_creditos_aprobados(self, nuevos_creditos):
        if isinstance(nuevos_creditos, int) and nuevos_creditos >= 0:
            self.__creditos_aprobados = nuevos_creditos
        else:
            print("Error: Los créditos aprobados deben ser un número entero no negativo.")

    def set_materias_cursadas(self, nuevas_materias):
        if isinstance(nuevas_materias, list) and nuevas_materias and all(materia.strip() for materia in nuevas_materias):
            self.__materias_cursadas = [materia.strip() for materia in nuevas_materias]
        else:
            print("Error: Las materias cursadas deben ser una lista no vacía con elementos válidos.")

    def set_fecha_ingreso(self, nueva_fecha):
        if nueva_fecha.strip() and self.__validar_fecha(nueva_fecha):
            self.__fecha_ingreso = nueva_fecha.strip()
        else:
            print("Error: La fecha debe tener el formato YYYY-MM-DD y ser válida.")

    def set_estado_academico(self, nuevo_estado):
        estados_validos = ["Activo", "Suspendido", "Graduado", "Egresado"]
        if nuevo_estado.strip() and nuevo_estado in estados_validos:
            self.__estado_academico = nuevo_estado
        else:
            print(f"Error: Estado académico inválido. Los estados válidos son: {', '.join(estados_validos)}")

    def set_beca(self, tiene_beca):
        if isinstance(tiene_beca, bool):
            self.__beca = tiene_beca
        else:
            print("Error: El estado de beca debe ser True o False.")

    def set_correo_electronico(self, nuevo_correo):
        if nuevo_correo.strip() and "@" in nuevo_correo and "." in nuevo_correo:
            self.__correo_electronico = nuevo_correo.strip()
        else:
            print("Error: Formato de correo electrónico inválido o vacío.")


    def __validar_fecha(self, fecha_str):
        try:
            datetime.strptime(fecha_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

