"""SGE académico: proyecto de Algoritmos y Programación.
"""

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_APROBACION = 3.5
CANTIDAD_NOTAS = 3


def leer_texto_obligatorio(mensaje):
    """while: insistir hasta obtener un texto no vacío."""
    texto = input(mensaje).strip()
    while texto == "":
        print("ERROR: el dato no puede estar vacío.")
        texto = input(mensaje).strip()
    return texto


def leer_nota(numero):
    """Validar que la nota sea numérica y esté en el rango 0 a 5."""
    while True:
        texto = input(f"Nota {numero} (0 a 5): ").strip()
        try:
            nota = float(texto.replace(",", "."))
            if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
                return nota
            print("ERROR: la nota debe estar entre 0 y 5.")
        except ValueError:
            print("ERROR: escribe una nota numérica (ejemplo 4.2).")


def buscar_por_id(estudiantes, identificacion):
    """for + if: localizar un registro por identificación."""
    for estudiante in estudiantes:
        if estudiante["id"] == identificacion:
            return estudiante
    return None


def calcular_promedio(notas):
    """Acumulador explícito para sumar las notas y calcular su media."""
    suma = 0.0
    for nota in notas:
        suma = suma + nota
    return suma / len(notas)


def obtener_estado(promedio):
    """Decisión anidada: distinguir aprobado, destacado y reprobado."""
    if promedio >= NOTA_APROBACION:
        if promedio >= 4.5:
            return "APROBADO - DESTACADO"
        else:
            return "APROBADO"
    else:
        return "REPROBADO"


def mostrar_estudiante(estudiante):
    
    promedio = calcular_promedio(estudiante["notas"])
    print(f"ID: {estudiante['id']}")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Programa: {estudiante['programa']}")
    for indice in range(len(estudiante["notas"])):
        print(f"Nota {indice + 1}: {estudiante['notas'][indice]:.2f}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {obtener_estado(promedio)}")


def registrar_estudiante(estudiantes):
    print("\n--- REGISTRAR ESTUDIANTE ---")
    identificacion = leer_texto_obligatorio("ID: ")
    if buscar_por_id(estudiantes, identificacion) is not None:
        print("ERROR: ya existe un estudiante con ese ID.")
        return

    nombre = leer_texto_obligatorio("Nombre completo: ")
    programa = leer_texto_obligatorio("Programa académico: ")
    notas = []
    
    for numero in range(1, CANTIDAD_NOTAS + 1):
        notas.append(leer_nota(numero))

    estudiantes.append({
        "id": identificacion,
        "nombre": nombre,
        "programa": programa,
        "notas": notas,
    })
    print("Estudiante registrado correctamente.")


def leer_orden_listado():
    
    while True:
        print("1. Orden de registro (ascendente)")
        print("2. Orden inverso (descendente)")
        opcion = input("Orden del listado (1 o 2): ").strip()
    
        if opcion == "1" or opcion == "2":
            break
        print("ERROR: solo se permite 1 o 2.")
    return opcion


def listar_estudiantes(estudiantes):
    print("\n--- LISTADO DE ESTUDIANTES ---")
    if len(estudiantes) == 0:
        print("No existen estudiantes registrados.")
        return

    orden = leer_orden_listado()
    if orden == "1":
    
        for indice in range(0, len(estudiantes)):
            print(f"\nESTUDIANTE {indice + 1}")
            mostrar_estudiante(estudiantes[indice])
    else:
    
        for indice in range(len(estudiantes) - 1, -1, -1):
            print(f"\nESTUDIANTE {indice + 1}")
            mostrar_estudiante(estudiantes[indice])

    print(f"\nTotal registrados: {len(estudiantes)}")


def consultar_estudiante(estudiantes):
    print("\n--- BUSCAR POR ID ---")
    identificacion = leer_texto_obligatorio("ID a buscar: ")
    estudiante = buscar_por_id(estudiantes, identificacion)
    if estudiante is None:
        print("No se encontró un estudiante con ese ID.")
    else:
        mostrar_estudiante(estudiante)


def modificar_calificaciones(estudiantes):
    print("\n--- MODIFICAR CALIFICACIONES ---")
    identificacion = leer_texto_obligatorio("ID del estudiante: ")
    estudiante = buscar_por_id(estudiantes, identificacion)
    if estudiante is None:
        print("No se encontró un estudiante con ese ID.")
        return

    print(f"Estudiante: {estudiante['nombre']}")
    notas_nuevas = []
    for numero in range(1, CANTIDAD_NOTAS + 1):
        notas_nuevas.append(leer_nota(numero))
    estudiante["notas"] = notas_nuevas
    print("Calificaciones actualizadas correctamente.")
    mostrar_estudiante(estudiante)


def consultar_estadisticas(estudiantes):
    print("\n--- ESTADÍSTICAS ACADÉMICAS ---")
    if len(estudiantes) == 0:
        print("No hay estudiantes para calcular estadísticas.")
        return

    contador_aprobados = 0
    contador_reprobados = 0
    suma_promedios = 0.0
    contador_estudiantes = 0

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        suma_promedios = suma_promedios + promedio
        contador_estudiantes = contador_estudiantes + 1
        if promedio >= NOTA_APROBACION:
            contador_aprobados = contador_aprobados + 1
        else:
            contador_reprobados = contador_reprobados + 1

    promedio_general = suma_promedios / contador_estudiantes
    print(f"Total de estudiantes: {contador_estudiantes}")
    print(f"Aprobados: {contador_aprobados}")
    print(f"Reprobados: {contador_reprobados}")
    print(f"Promedio general: {promedio_general:.2f}")


def mostrar_menu():
    print("\n" + "=" * 45)
    print(" SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 45)
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Modificar calificaciones")
    print("5. Consultar estadísticas")
    print("6. Salir")


def main():
    estudiantes = []  # Lista dinámica de registros (diccionarios).
    salir = False  # Bandera que controla el ciclo del menú.

    # while condicionado al comienzo: se revisa antes de cada vuelta.
    while not salir:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        # Decisión múltiple: equivalente al switch de otros lenguajes.
        match opcion:
            case "1":
                registrar_estudiante(estudiantes)
            case "2":
                listar_estudiantes(estudiantes)
            case "3":
                consultar_estudiante(estudiantes)
            case "4":
                modificar_calificaciones(estudiantes)
            case "5":
                consultar_estadisticas(estudiantes)
            case "6":
                salir = True
                print("Fin del programa. ¡Hasta pronto!")
            case _:
                print("ERROR: selecciona una opción entre 1 y 6.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nEjecución interrumpida. Fin del programa.")