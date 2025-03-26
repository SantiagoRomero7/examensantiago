import artistas
from artistas import datos
from report import generate_report

def main():
    datos_artistas = {}
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar artistas")
        print("2. Generar reporte")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            datos(datos_artistas)
        elif opcion == '2':
            generate_report(datos_artistas)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()