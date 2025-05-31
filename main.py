# main.py

from methods import Estudiante 
def mostrar_menu():
    """Muestra las opciones de atributos que se pueden modificar."""
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
    print("--- Modificación Directa (Sin función setter) ---")
    print("13. Teléfono")
    print("14. Dirección")
    print("15. Nacionalidad")
    print("0. Mostrar Información y Salir")
    print("------------------------------------------")

def main():
    print("¡Bienvenido al sistema de gestión de estudiantes!")
    print("Por favor, ingrese los datos iniciales para el nuevo estudiante.")

    # Solicitar al usuario los datos iniciales para el estudiante
    nombre_inicial = input("Nombre: ")
    apellido_inicial = input("Apellido: ")
    
    # Validar edad como entero positivo
    while True:
        try:
            edad_inicial = int(input("Edad: "))
            if edad_inicial > 0:
                break
            else:
                print("La edad debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la edad.")

    carnet_inicial = input("Carnet: ")
    carrera_inicial = input("Carrera: ")
    
    # Validar promedio como número entre 0 y 20
    while True:
        try:
            promedio_inicial = float(input("Promedio (0-20): "))
            if 0.0 <= promedio_inicial <= 20.0:
                break
            else:
                print("El promedio debe ser un número entre 0 y 20.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para el promedio.")

    # Validar créditos aprobados como entero no negativo
    while True:
        try:
            creditos_iniciales = int(input("Créditos Aprobados: "))
            if creditos_iniciales >= 0:
                break
            else:
                print("Los créditos aprobados deben ser un número entero no negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para los créditos.")
            
    materias_iniciales_str = input("Materias Cursadas (separadas por coma, ej: Matematicas,Fisica): ")
    materias_iniciales = [materia.strip() for materia in materias_iniciales_str.split(',') if materia.strip()]
    
    fecha_ingreso_inicial = input("Fecha de Ingreso (ej: 2023-09-01): ")
    
    # Validar estado académico
    estados_validos = ["Activo", "Suspendido", "Graduado", "Egresado"]
    while True:
        estado_academico_inicial = input(f"Estado Académico ({', '.join(estados_validos)}): ")
        if estado_academico_inicial in estados_validos:
            break
        else:
            print(f"Estado académico inválido. Por favor, elija entre: {', '.join(estados_validos)}")
            
    # Validar beca
    while True:
        beca_inicial_str = input("¿Tiene Beca? (Sí/No): ").lower()
        if beca_inicial_str in ['si', 'no']:
            beca_inicial = True if beca_inicial_str == 'si' else False
            break
        else:
            print("Respuesta inválida. Por favor, escriba 'Sí' o 'No'.")
            
    correo_inicial = input("Correo Electrónico: ")
    telefono_inicial = input("Teléfono: ")
    direccion_inicial = input("Dirección: ")
    nacionalidad_inicial = input("Nacionalidad: ")


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

    # Bucle  para la interacción con el usuario
    while True:
        estudiante1.mostrar_informacion() # Mostrar información actual antes del menú
        mostrar_menu()
        opcion = input("Seleccione el número del atributo a modificar (0 para salir): ")

        if opcion == '0':
            print("¡Gracias por usar el sistema! Saliendo del programa.")
            break
        elif opcion == '1':
            nuevo_valor = input("Ingrese el nuevo nombre: ")
            estudiante1.set_nombre(nuevo_valor)
        elif opcion == '2':
            nuevo_valor = input("Ingrese el nuevo apellido: ")
            estudiante1.set_apellido(nuevo_valor)
        elif opcion == '3':
            try:
                nuevo_valor = int(input("Ingrese la nueva edad: "))
                estudiante1.set_edad(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para la edad.")
        elif opcion == '4':
            nuevo_valor = input("Ingrese el nuevo carnet: ")
            estudiante1.set_carnet(nuevo_valor)
        elif opcion == '5':
            nuevo_valor = input("Ingrese la nueva carrera: ")
            estudiante1.set_carrera(nuevo_valor)
        elif opcion == '6':
            try:
                nuevo_valor = float(input("Ingrese el nuevo promedio (0-20): "))
                estudiante1.set_promedio(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número para el promedio.")
        elif opcion == '7':
            try:
                nuevo_valor = int(input("Ingrese la nueva cantidad de créditos aprobados: "))
                estudiante1.set_creditos_aprobados(nuevo_valor)
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para los créditos.")
        elif opcion == '8':
            materias_str = input("Ingrese las nuevas materias cursadas (separadas por coma, ej: Matematicas,Fisica): ")
            nuevas_materias = [materia.strip() for materia in materias_str.split(',') if materia.strip()]
            estudiante1.set_materias_cursadas(nuevas_materias)
        elif opcion == '9':
            nuevo_valor = input("Ingrese la nueva fecha de ingreso (ej: 2024-01-15): ")
            estudiante1.set_fecha_ingreso(nuevo_valor)
        elif opcion == '10':
            estados_validos = ["Activo", "Suspendido", "Graduado", "Egresado"]
            nuevo_estado = input(f"Ingrese el nuevo estado académico ({', '.join(estados_validos)}): ")
            estudiante1.set_estado_academico(nuevo_estado)
        elif opcion == '11':
            respuesta_beca = input("¿El estudiante tiene beca ahora? (Sí/No): ").lower()
            if respuesta_beca == 'si':
                estudiante1.set_beca(True)
            elif respuesta_beca == 'no':
                estudiante1.set_beca(False)
            else:
                print("Entrada inválida. Por favor, responda 'Sí' o 'No'.")
        elif opcion == '12':
            nuevo_valor = input("Ingrese el nuevo correo electrónico: ")
            estudiante1.set_correo_electronico(nuevo_valor)
        elif opcion == '13':
            nuevo_valor = input("Ingrese el nuevo teléfono: ")
            estudiante1.telefono = nuevo_valor
            print("Teléfono actualizado directamente.")
        elif opcion == '14':
            nuevo_valor = input("Ingrese la nueva dirección: ")
            estudiante1.direccion = nuevo_valor
            print("Dirección actualizada directamente.")
        elif opcion == '15':
            nuevo_valor = input("Ingrese la nueva nacionalidad: ")
            estudiante1.nacionalidad = nuevo_valor
            print("Nacionalidad actualizada directamente.")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...") 

if __name__ == "__main__":
    main()