# - Título del Proyecto
**Sistema de Gestión de Artistas Musicales**

## - Descripción del Proyecto
Este proyecto implementa un sistema integral de gestión para manejar datos de artistas musicales, países y géneros musicales, permitiendo también la generación de informes relevantes sobre ventas y actividad artística.

## - ¿Qué hace el proyecto?
El sistema permite:
- Registrar y gestionar información de artistas musicales, incluyendo país de origen, años de actividad, géneros musicales, ventas y estado.
- Manejar datos de países y géneros musicales.
- Generar reportes específicos sobre artistas, géneros y ventas en distintos períodos de tiempo.

## - ¿Por qué este proyecto es útil?
Este sistema proporciona una solución estructurada para la administración de datos musicales, facilitando consultas específicas y la generación de informes detallados sobre la industria musical.

## - ¿Qué problema resuelve?
Automatiza la gestión y consulta de información musical, evitando la necesidad de búsquedas manuales y permitiendo obtener reportes con eficiencia y precisión.

---

## - Instalación

### - Requisitos previos
- Tener Python instalado (versión 3.x recomendada).
- Librerías necesarias (pueden instalarse con `requirements.txt` si es necesario).

### - Pasos de instalación
```sh
# Clonar el repositorio
git clone https://github.com/SantiagoRomero7/gestion-artistas.git
cd gestion-artistas

# Crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## - Uso

Para ejecutar el sistema, usa el siguiente comando:
```sh
python main.py
```

### - Funcionalidades principales
- **Gestión de datos de artistas:** Permite agregar y consultar información de artistas musicales.
- **Interacción con países y géneros musicales:** Maneja datos de países (nombre, códigos ISO e ISO3) y géneros musicales.
- **Generación de reportes:**
  - Artistas musicales de Reino Unido entre 1960 y 1970.
  - Artistas del género 'Rock/pop'.
  - Datos de artistas de los últimos 10 años.
  - Número de registros de artistas por año.
  - Unidades certificadas registradas en 2023.

---

## - ¿Qué aprendió el desarrollador?
Este proyecto permitió profundizar en:
- Manipulación y gestión de datos en formato JSON.
- Estructuración de sistemas de consulta de información.
- Generación de reportes dinámicos en Python.

---

## - Mantenimiento y Créditos
- **Santiago Romero** - [GitHub](https://github.com/SantiagoRomero7)

## - GitHub
Repositorio: [Sistema de Gestión de Artistas Musicales](https://github.com/SantiagoRomero7/gestion-artistas)
