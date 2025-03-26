from json import Artist

def datos(datos):
    while True:
        print("\n--- Datos de artistas ---")
        print("1. Registrar artista")
        print("2. Listar artistas")
        print("3. Eliminar artista")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_artista(datos)
        elif opcion == '2':
            listar_artistas(datos)
        elif opcion == '3':
            eliminar_artista(datos)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_artista(datos):
    nombre = input("Ingrese el nombre del artista: ")
    if nombre in datos:
        print("El artista ya existe.")
        return
    pais_origen = input("Ingrese pais de origen: ")
    anios_de_actividad = input("Ingrese años de actividad: ")
    año_lanzamiento_primer_disco = input("Ingrese el año del lanzamiento del primer disco: ")
    genero_musical = input("Ingrese el genero musical: ")
    unidades_certificadas_totales = int(input("Ingrese la cantidad de unidades certificadas totales: "))
    ventas_reclamadas = input("Ingrese el precio de compra: ")
    estado_del_artista = input("Ingrese si el artista está activo o no: ")

    artista = Artist(nombre, pais_origen, anios_de_actividad, año_lanzamiento_primer_disco, genero_musical, unidades_certificadas_totales, ventas_reclamadas, estado_del_artista)
    datos[nombre] = artista
    print("Artista agregado exitosamente.")

def listar_artistas(datos):
    if not datos:
        print("No hay artistas registrados.")
        return
    for artista in datos.values():
        print(artista)

def eliminar_artista(datos):
    nombre = input("Ingrese el nombre del artista a eliminar: ")
    if nombre in datos:
        del datos[nombre]
        print("Artista eliminado exitosamente.")
    else:
        print("El artista no existe.")