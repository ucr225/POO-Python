import os
import re
from datetime import datetime,date
from methods import Estudiante

#ELABORADO POR:
#Valentina Labrador V-30496048
#Diego Gonzalez V-30722066
#Uriel Caceres V-29664183


def mostrar_informacion(estudiante):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("\n--- Info del Estudiante ---")
    print("ATRIBUTOS PRIVADOS")
    print(f"1.- Nombre: {estudiante.get_nombre()}")
    print(f"2.- Apellido: {estudiante.get_apellido()}")
    print(f"3.- Edad: {estudiante.get_edad()}")
    print(f"4.- Carnet: {estudiante.get_carnet()}")
    print(f"5.- Carrera: {estudiante.get_carrera()}")
    print(f"6.- Promedio: {estudiante.get_promedio()}")
    print(f"7.- Créditos Aprobados: {estudiante.get_creditos_aprobados()}")
    print(f"8.- Materias Cursadas: {', '.join(estudiante.get_materias_cursadas()) if estudiante.get_materias_cursadas() else 'Ninguna'}")
    print(f"9.- Fecha de Ingreso: {estudiante.get_fecha_ingreso()}")
    print(f"10.- Estado Académico: {estudiante.get_estado_academico()}")
    print(f"11.- Beca: {'Sí' if estudiante.get_beca() else 'No'}")
    print(f"12.- Correo Electrónico: {estudiante.get_correo_electronico()}")
    print("ATRIBUTOS PUBLICOS")
    print(f"13.- Teléfono: {estudiante.telefono}")
    print(f"14.- Dirección: {estudiante.direccion}")
    print(f"15.- Nacionalidad: {estudiante.nacionalidad}")
    print("----------------------------------")

def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        return fecha<=date.today()
    except ValueError:
        return False

def validar_telefono(telefono): 
    digitos = re.sub(r'[^0-9]', '', telefono)
    return len(digitos) >= 7 and re.match(r'^[\d\s+-]+$', telefono)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("¡Bienvenido al sistema de gestión de estudiantes!")
    print("Por favor, ingrese los datos iniciales para el nuevo estudiante.")

    while True:
        nombre_inicial = input("Nombre (ej: Juan): ").strip()  
        if nombre_inicial:
            break
        print("Error: El nombre no puede estar vacío.")

    while True:
        apellido_inicial = input("Apellido (ej: Pérez): ").strip()  
        if apellido_inicial:
            break
        print("Error: El apellido no puede estar vacío.")

    while True:
        try:
            edad_inicial = int(input("Edad (ej: 20): "))  
            if 16 <= edad_inicial < 100:
                break
            else:
                print("La edad debe estar entre 16 y 99 años.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la edad.")

    while True:
        carnet_inicial = input("Carnet (ej: 20210001): ").strip()  
        if carnet_inicial:
            break
        print("Error: El carnet no puede estar vacío.")

    while True:
        carrera_inicial = input("Carrera (ej: Ingeniería Informática): ").strip()  
        if carrera_inicial:
            break
        print("Error: La carrera no puede estar vacía.")

    while True:
        try:
            promedio_inicial = float(input("Promedio (0-20, ej: 15.5): "))  
            if 0.0 <= promedio_inicial <= 20.0:
                break
            else:
                print("El promedio debe ser un número entre 0 y 20.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para el promedio.")

    while True:
        try:
            creditos_iniciales = int(input("Créditos Aprobados (ej: 60): ")) 
            if creditos_iniciales >= 0:
                break
            else:
                print("Los créditos aprobados deben ser un número entero no negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para los créditos.")

    while True:
        materias_iniciales_str = input("Materias Cursadas (separadas por coma, ej: Matemáticas,Física,Química): ").strip()  
        materias_iniciales = [materia.strip() for materia in materias_iniciales_str.split(',') if materia.strip()]
        if materias_iniciales:
            break
        print("Error: Debe ingresar al menos una materia válida.")

    while True:
        fecha_ingreso_inicial = input("Fecha de Ingreso (YYYY-MM-DD, ej: 2023-09-01): ").strip()  
        if validar_fecha(fecha_ingreso_inicial):
            break
        print("Error: La fecha debe tener el formato YYYY-MM-DD y ser válida.")

    estados_validos = ["Activo", "Suspendido", "Graduado", "Egresado"]
    while True:
        estado_academico_inicial = input(f"Estado Académico ({', '.join(estados_validos)}, ej: Activo): ").strip()  
        if estado_academico_inicial.capitalize() in estados_validos:
            break
        print(f"Estado académico inválido. Por favor, elija entre: {', '.join(estados_validos)}")

    while True:
        beca_inicial_str = input("¿Tiene Beca? (Sí/No, ej: Sí): ").lower().strip()  
        if beca_inicial_str.lower() in ['si', 'no','sí']:
            beca_inicial = True if beca_inicial_str == 'si' else False
            break
        print("Respuesta inválida. Por favor, escriba 'Sí' o 'No'.")

    while True:
        correo_inicial = input("Correo Electrónico (ej: juan.perez@universidad.com): ").strip()  
        if correo_inicial and "@" in correo_inicial and "." in correo_inicial:
            break
        print("Error: Formato de correo electrónico inválido o vacío.")

    while True:
        telefono_inicial = input("Teléfono (mínimo 7 dígitos, ej: +123-456-7890): ").strip() 
        if validar_telefono(telefono_inicial):
            break
        print("Error: El teléfono debe contener al menos 7 dígitos y solo dígitos, guiones, espacios o '+'.")

    while True:
        direccion_inicial = input("Dirección (ej: Av. Principal 123, Ciudad): ").strip() 
        if direccion_inicial:
            break
        print("Error: La dirección no puede estar vacía.")

    while True:
        nacionalidad_inicial = input("Nacionalidad (ej: Venezolana): ").strip() 
        if nacionalidad_inicial and nacionalidad_inicial.replace(' ', '').isalpha():
            break
        print("Error: Nacionalidad no valida")

    estudiante1 = Estudiante(
        nombre_inicial,apellido_inicial,
        edad_inicial,carnet_inicial,
        carrera_inicial,promedio_inicial,
        creditos_iniciales,materias_iniciales,
        fecha_ingreso_inicial,estado_academico_inicial,
        beca_inicial,correo_inicial,
        telefono_inicial,direccion_inicial,
        nacionalidad_inicial
    )

    while True:
        mostrar_informacion(estudiante1)

        opcion = input("Seleccione el número del atributo a modificar (0 para salir, ej: 1): ").strip() 

        if opcion == '0':
            os.system('cls' if os.name == 'nt' else 'clear')  
            print("¡Gracias por usar el sistema! Saliendo del programa.")
            break
        elif opcion == '1':
            nuevo_valor = input("Ingrese el nuevo nombre (ej: María): ").strip() 
            estudiante1.set_nombre(nuevo_valor)
        elif opcion == '2':
            nuevo_valor = input("Ingrese el nuevo apellido (ej: Gómez): ").strip()  
            estudiante1.set_apellido(nuevo_valor)
        elif opcion == '3':
            try:
                nuevo_valor = int(input("Ingrese la nueva edad (ej: 22): "))  
                estudiante1.set_edad(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para la edad.")
        elif opcion == '4':
            nuevo_valor = input("Ingrese el nuevo carnet (ej: 20220002): ").strip() 
            estudiante1.set_carnet(nuevo_valor)
        elif opcion == '5':
            nuevo_valor = input("Ingrese la nueva carrera (ej: Medicina): ").strip()  
            estudiante1.set_carrera(nuevo_valor)
        elif opcion == '6':
            try:
                nuevo_valor = float(input("Ingrese el nuevo promedio (0-20, ej: 18.0): "))  
                estudiante1.set_promedio(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número para el promedio.")
        elif opcion == '7':
            try:
                nuevo_valor = int(input("Ingrese la nueva cantidad de créditos aprobados (ej: 80): "))  
                estudiante1.set_creditos_aprobados(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para los créditos.")
        elif opcion == '8':
            materias_str = input("Ingrese las nuevas materias cursadas (separadas por coma, ej: Historia,Literatura): ").strip()  
            nuevas_materias = [materia.strip() for materia in materias_str.split(',') if materia.strip()]
            estudiante1.set_materias_cursadas(nuevas_materias)
        elif opcion == '9':
            nuevo_valor = input("Ingrese la nueva fecha de ingreso (YYYY-MM-DD, ej: 2024-01-15): ").strip()  
            estudiante1.set_fecha_ingreso(nuevo_valor)
        elif opcion == '10':
            nuevo_estado = input(f"Ingrese el nuevo estado académico ({', '.join(estados_validos)}, ej: Graduado): ").strip()  
            estudiante1.set_estado_academico(nuevo_estado)
        elif opcion == '11':
            respuesta_beca = input("¿El estudiante tiene beca ahora? (Sí/No, ej: No): ").lower().strip()  
            if respuesta_beca == 'si':
                estudiante1.set_beca(True)
            elif respuesta_beca == 'no':
                estudiante1.set_beca(False)
            else:
                print("Entrada inválida. Por favor, responda 'Sí' o 'No'.")
        elif opcion == '12':
            nuevo_valor = input("Ingrese el nuevo correo electrónico (ej: maria.gomez@universidad.com): ").strip() 
            estudiante1.set_correo_electronico(nuevo_valor)
        elif opcion == '13':
            nuevo_valor = input("Ingrese el nuevo teléfono (mínimo 7 dígitos, ej: +987-654-3210): ").strip()  
            estudiante1.telefono = nuevo_valor
        elif opcion == '14':
            nuevo_valor = input("Ingrese la nueva dirección (ej: Calle Secundaria 456, Ciudad): ").strip()  
            estudiante1.direccion = nuevo_valor
        elif opcion == '15':
            nuevo_valor = input("Ingrese la nueva nacionalidad (ej: Colombiana): ").strip()  
            estudiante1.nacionalidad = nuevo_valor
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()