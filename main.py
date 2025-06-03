import os
import re
from datetime import datetime
from methods import Estudiante

def mostrar_menu():
    """Muestra las opciones de atributos que se pueden modificar."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola
    print("\n--- Modificar Atributos del Estudiante ---")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Carnet")
    print("5. Carrera")
    print("6. Promedio")
    print("7. Créditos Aprobados")
    print("8. Materias Cursadas")
    print("9. Fecha de Ingreso")
    print("10. Estado Académico")
    print("11. Beca")
    print("12. Correo Electrónico")
    print("13. Teléfono")
    print("14. Dirección")
    print("15. Nacionalidad")
    print("0. Mostrar Información y Salir")
    print("------------------------------------------")

def validar_fecha(fecha_str):
    """Valida que la fecha tenga el formato YYYY-MM-DD y sea una fecha válida."""
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validar_telefono(telefono):
    """Valida que el teléfono contenga solo dígitos, guiones, espacios o +, con al menos 7 dígitos."""
    # Extraer solo dígitos para contarlos
    digitos = re.sub(r'[^0-9]', '', telefono)
    if len(digitos) >= 7 and re.match(r'^[\d\s+-]+$', telefono):
        return True
    return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("¡Bienvenido al sistema de gestión de estudiantes!")
    print("Por favor, ingrese los datos iniciales para el nuevo estudiante.")

    # Datos iniciales 
    while True:
        nombre_inicial = input("Nombre (ej: Juan): ").strip()  # Ejemplo de entrada: Juan
        if nombre_inicial:
            break
        print("Error: El nombre no puede estar vacío.")

    while True:
        apellido_inicial = input("Apellido (ej: Pérez): ").strip()  # Ejemplo de entrada: Pérez
        if apellido_inicial:
            break
        print("Error: El apellido no puede estar vacío.")

    # Validar edad (16 a 99)
    while True:
        try:
            edad_inicial = int(input("Edad (ej: 20): "))  # Ejemplo de entrada: 20
            if 16 <= edad_inicial < 100:
                break
            else:
                print("La edad debe estar entre 16 y 99 años.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la edad.")

    while True:
        carnet_inicial = input("Carnet (ej: 20210001): ").strip()  # Ejemplo de entrada: 20210001
        if carnet_inicial:
            break
        print("Error: El carnet no puede estar vacío.")

    while True:
        carrera_inicial = input("Carrera (ej: Ingeniería Informática): ").strip()  # Ejemplo de entrada: Ingeniería Informática
        if carrera_inicial:
            break
        print("Error: La carrera no puede estar vacía.")

    # Validar promedio 
    while True:
        try:
            promedio_inicial = float(input("Promedio (0-20, ej: 15.5): "))  # Ejemplo de entrada: 15.5
            if 0.0 <= promedio_inicial <= 20.0:
                break
            else:
                print("El promedio debe ser un número entre 0 y 20.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para el promedio.")

    # Validar créditos aprobados 
    while True:
        try:
            creditos_iniciales = int(input("Créditos Aprobados (ej: 60): "))  # Ejemplo de entrada: 60
            if creditos_iniciales >= 0:
                break
            else:
                print("Los créditos aprobados deben ser un número entero no negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para los créditos.")

    while True:
        materias_iniciales_str = input("Materias Cursadas (separadas por coma, ej: Matemáticas,Física,Química): ").strip()  # Ejemplo de entrada: Matemáticas,Física,Química
        materias_iniciales = [materia.strip() for materia in materias_iniciales_str.split(',') if materia.strip()]
        if materias_iniciales:
            break
        print("Error: Debe ingresar al menos una materia válida.")

    # Validar fecha de ingreso
    while True:
        fecha_ingreso_inicial = input("Fecha de Ingreso (YYYY-MM-DD, ej: 2023-09-01): ").strip()  # Ejemplo de entrada: 2023-09-01
        if validar_fecha(fecha_ingreso_inicial):
            break
        print("Error: La fecha debe tener el formato YYYY-MM-DD y ser válida.")

    # Validar estado académico
    estados_validos = ["Activo", "Suspendido", "Graduado", "Egresado"]
    while True:
        estado_academico_inicial = input(f"Estado Académico ({', '.join(estados_validos)}, ej: Activo): ").strip()  # Ejemplo de entrada: Activo
        if estado_academico_inicial in estados_validos:
            break
        print(f"Estado académico inválido. Por favor, elija entre: {', '.join(estados_validos)}")

    # Validar beca
    while True:
        beca_inicial_str = input("¿Tiene Beca? (Sí/No, ej: Sí): ").lower().strip()  # Ejemplo de entrada: Sí
        if beca_inicial_str in ['si', 'no']:
            beca_inicial = True if beca_inicial_str == 'si' else False
            break
        print("Respuesta inválida. Por favor, escriba 'Sí' o 'No'.")

    while True:
        correo_inicial = input("Correo Electrónico (ej: juan.perez@universidad.com): ").strip()  # Ejemplo de entrada: juan.perez@universidad.com
        if correo_inicial and "@" in correo_inicial and "." in correo_inicial:
            break
        print("Error: Formato de correo electrónico inválido o vacío.")

    # Validar teléfono
    while True:
        telefono_inicial = input("Teléfono (mínimo 7 dígitos, ej: +123-456-7890): ").strip()  # Ejemplo de entrada: +123-456-7890
        if validar_telefono(telefono_inicial):
            break
        print("Error: El teléfono debe contener al menos 7 dígitos y solo dígitos, guiones, espacios o '+'.")

    # Validar dirección
    while True:
        direccion_inicial = input("Dirección (ej: Av. Principal 123, Ciudad): ").strip()  # Ejemplo de entrada: Av. Principal 123, Ciudad
        if direccion_inicial:
            break
        print("Error: La dirección no puede estar vacía.")

    # Validar nacionalidad
    while True:
        nacionalidad_inicial = input("Nacionalidad (ej: Venezolana): ").strip()  # Ejemplo de entrada: Venezolana
        if nacionalidad_inicial:
            break
        print("Error: La nacionalidad no puede estar vacía.")

    # Crear objeto
    estudiante1 = Estudiante(
        nombre=nombre_inicial,
        apellido=apellido_inicial,
        edad=edad_inicial,
        carnet=carnet_inicial,
        carrera=carrera_inicial,
        promedio=promedio_inicial,
        creditos_aprobados=creditos_iniciales,
        materias_cursadas=materias_iniciales,
        fecha_ingreso=fecha_ingreso_inicial,
        estado_academico=estado_academico_inicial,
        beca=beca_inicial,
        correo_electronico=correo_inicial,
        telefono=telefono_inicial,
        direccion=direccion_inicial,
        nacionalidad=nacionalidad_inicial
    )

    # Bucle para la interacción con el usuario
    while True:
        estudiante1.mostrar_informacion()  # Mostrar información actual 
        mostrar_menu()
        opcion = input("Seleccione el número del atributo a modificar (0 para salir, ej: 1): ").strip()  # Ejemplo de entrada: 1

        if opcion == '0':
            os.system('cls' if os.name == 'nt' else 'clear')  
            print("¡Gracias por usar el sistema! Saliendo del programa.")
            break
        elif opcion == '1':
            nuevo_valor07 = input("Ingrese el nuevo nombre (ej: María): ").strip()  # Ejemplo de entrada: María
            estudiante1.set_nombre(nuevo_valor)
        elif opcion == '2':
            nuevo_valor = input("Ingrese el nuevo apellido (ej: Gómez): ").strip()  # Ejemplo de entrada: Gómez
            estudiante1.set_apellido(nuevo_valor)
        elif opcion == '3':
            try:
                nuevo_valor = int(input("Ingrese la nueva edad (ej: 22): "))  # Ejemplo de entrada: 22
                estudiante1.set_edad(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para la edad.")
        elif opcion == '4':
            nuevo_valor = input("Ingrese el nuevo carnet (ej: 20220002): ").strip()  # Ejemplo de entrada: 20220002
            estudiante1.set_carnet(nuevo_valor)
        elif opcion == '5':
            nuevo_valor = input("Ingrese la nueva carrera (ej: Medicina): ").strip()  # Ejemplo de entrada: Medicina
            estudiante1.set_carrera(nuevo_valor)
        elif opcion == '6':
            try:
                nuevo_valor = float(input("Ingrese el nuevo promedio (0-20, ej: 18.0): "))  # Ejemplo de entrada: 18.0
                estudiante1.set_promedio(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número para el promedio.")
        elif opcion == '7':
            try:
                nuevo_valor = int(input("Ingrese la nueva cantidad de créditos aprobados (ej: 80): "))  # Ejemplo de entrada: 80
                estudiante1.set_creditos_aprobados(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para los créditos.")
        elif opcion == '8':
            materias_str = input("Ingrese las nuevas materias cursadas (separadas por coma, ej: Historia,Literatura): ").strip()  # Ejemplo de entrada: Historia,Literatura
            nuevas_materias = [materia.strip() for materia in materias_str.split(',') if materia.strip()]
            estudiante1.set_materias_cursadas(nuevas_materias)
        elif opcion == '9':
            nuevo_valor = input("Ingrese la nueva fecha de ingreso (YYYY-MM-DD, ej: 2024-01-15): ").strip()  # Ejemplo de entrada: 2024-01-15
            estudiante1.set_fecha_ingreso(nuevo_valor)
        elif opcion == '10':
            nuevo_estado = input(f"Ingrese el nuevo estado académico ({', '.join(estados_validos)}, ej: Graduado): ").strip()  # Ejemplo de entrada: Graduado
            estudiante1.set_estado_academico(nuevo_estado)
        elif opcion == '11':
            respuesta_beca = input("¿El estudiante tiene beca ahora? (Sí/No, ej: No): ").lower().strip()  # Ejemplo de entrada: No
            if respuesta_beca == 'si':
                estudiante1.set_beca(True)
            elif respuesta_beca == 'no':
                estudiante1.set_beca(False)
            else:
                print("Entrada inválida. Por favor, responda 'Sí' o 'No'.")
        elif opcion == '12':
            nuevo_valor = input("Ingrese el nuevo correo electrónico (ej: maria.gomez@universidad.com): ").strip()  # Ejemplo de entrada: maria.gomez@universidad.com
            estudiante1.set_correo_electronico(nuevo_valor)
        elif opcion == '13':
            nuevo_valor = input("Ingrese el nuevo teléfono (mínimo 7 dígitos, ej: +987-654-3210): ").strip()  # Ejemplo de entrada: +987-654-3210
            estudiante1.set_telefono(nuevo_valor)
        elif opcion == '14':
            nuevo_valor = input("Ingrese la nueva dirección (ej: Calle Secundaria 456, Ciudad): ").strip()  # Ejemplo de entrada: Calle Secundaria 456, Ciudad
            estudiante1.set_direccion(nuevo_valor)
        elif opcion == '15':
            nuevo_valor = input("Ingrese la nueva nacionalidad (ej: Colombiana): ").strip()  # Ejemplo de entrada: Colombiana
            estudiante1.set_nacionalidad(nuevo_valor)
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()