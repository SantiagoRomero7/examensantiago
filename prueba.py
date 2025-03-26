from artistas import ArtistManager, Artist

def main():
    manager = ArtistManager()
    
    while True:
        name = input("Ingrese el nombre del artista: ")
        country = input("Ingrese el país del artista: ")
        genre = input("Ingrese el género del artista: ")
        is_active = input("Ingrese si el artista está activo o no (sí/no): ")
        
        # Convert input to boolean
        is_active = True if is_active.lower() == 'sí' else False
        
        new_artist = Artist(name, country, genre, is_active)
        manager.add_artist(new_artist)
        
        print("Artista agregado exitosamente.")
        print("Lista de artistas:")
        print(manager.get_artists())
        
        continue_input = input("¿Desea agregar otro artista? (sí/no): ")
        if continue_input.lower() != 'sí':
            break

if __name__ == "__main__":
    main()