# methods.py

class Estudiante:
    def __init__(self, nombre, apellido, edad, carnet, carrera, promedio,
                 creditos_aprobados, materias_cursadas, fecha_ingreso,
                 estado_academico, beca, correo_electronico, telefono,
                 direccion, nacionalidad):
        # Atributos que se pueden modificar mediante funciones (12 atributos)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carnet = carnet
        self.carrera = carrera
        self.promedio = promedio
        self.creditos_aprobados = creditos_aprobados
        self.materias_cursadas = materias_cursadas
        self.fecha_ingreso = fecha_ingreso
        self.estado_academico = estado_academico  # Ej: Activo, Suspendido, Graduado
        self.beca = beca  # Booleano
        self.correo_electronico = correo_electronico

        # Atributos que se deben modificar directamente (3 atributos)
        self.telefono = telefono
        self.direccion = direccion
        self.nacionalidad = nacionalidad

    # Métodos para modificar los 12 atributos variables
    def set_nombre(self, nuevo_nombre):
        """Modifica el nombre del estudiante."""
        self.nombre = nuevo_nombre

    def set_apellido(self, nuevo_apellido):
        """Modifica el apellido del estudiante."""
        self.apellido = nuevo_apellido

    def set_edad(self, nueva_edad):
        """Modifica la edad del estudiante."""
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self.edad = nueva_edad
        else:
            print("Error: La edad debe ser un número entero positivo.")

    def set_carnet(self, nuevo_carnet):
        """Modifica el número de carnet del estudiante."""
        self.carnet = nuevo_carnet

    def set_carrera(self, nueva_carrera):
        """Modifica la carrera del estudiante."""
        self.carrera = nueva_carrera

    def set_promedio(self, nuevo_promedio):
        """Modifica el promedio académico del estudiante."""
        if isinstance(nuevo_promedio, (int, float)) and 0.0 <= nuevo_promedio <= 20.0:
            self.promedio = nuevo_promedio
        else:
            print("Error: El promedio debe ser un número entre 0 y 20.")

    def set_creditos_aprobados(self, nuevos_creditos):
        """Modifica la cantidad de créditos aprobados por el estudiante."""
        if isinstance(nuevos_creditos, int) and nuevos_creditos >= 0:
            self.creditos_aprobados = nuevos_creditos
        else:
            print("Error: Los créditos aprobados deben ser un número entero no negativo.")

    def set_materias_cursadas(self, nuevas_materias):
        """Modifica la lista de materias cursadas."""
        if isinstance(nuevas_materias, list):
            self.materias_cursadas = nuevas_materias
        else:
            print("Error: Las materias cursadas deben ser una lista.")

    def set_fecha_ingreso(self, nueva_fecha):
        """Modifica la fecha de ingreso del estudiante."""
        self.fecha_ingreso = nueva_fecha

    def set_estado_academico(self, nuevo_estado):
        """Modifica el estado académico del estudiante."""
        estados_validos = ["Activo", "Suspendido", "Graduado", "Egresado"]
        if nuevo_estado in estados_validos:
            self.estado_academico = nuevo_estado
        else:
            print(f"Error: Estado académico inválido. Los estados válidos son: {', '.join(estados_validos)}")

    def set_beca(self, tiene_beca):
        """Modifica el estado de beca del estudiante (True/False)."""
        if isinstance(tiene_beca, bool):
            self.beca = tiene_beca
        else:
            print("Error: El estado de beca debe ser True o False.")

    def set_correo_electronico(self, nuevo_correo):
        """Modifica el correo electrónico del estudiante."""
        if "@" in nuevo_correo and "." in nuevo_correo:
            self.correo_electronico = nuevo_correo
        else:
            print("Error: Formato de correo electrónico inválido.")

    # Método para mostrar la información del estudiante
    def mostrar_informacion(self):
        """Muestra toda la información del estudiante."""
        print("\n--- Información del Estudiante ---")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Carnet: {self.carnet}")
        print(f"Carrera: {self.carrera}")
        print(f"Promedio: {self.promedio}")
        print(f"Créditos Aprobados: {self.creditos_aprobados}")
        print(f"Materias Cursadas: {', '.join(self.materias_cursadas) if self.materias_cursadas else 'Ninguna'}")
        print(f"Fecha de Ingreso: {self.fecha_ingreso}")
        print(f"Estado Académico: {self.estado_academico}")
        print(f"Beca: {'Sí' if self.beca else 'No'}")
        print(f"Correo Electrónico: {self.correo_electronico}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("----------------------------------")