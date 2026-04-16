# Microservicio Unificado (ms-py)

Este proyecto es un microservicio desarrollado en Flask que integra módulos de usuarios, billeteras, comercios y transacciones, utilizando una base de datos PostgreSQL.

## Prerrequisitos

*   Python 3.10 o superior
*   PostgreSQL instalado y corriendo
*   Base de datos creada con el nombre `daviplata`

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd ms-py
```

### 2. Crear y activar el entorno virtual
En Windows:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto (o usa el que ya existe) con tu cadena de conexión:
```env
DATABASE_URL=postgresql://postgres@localhost:5432/daviplata
```

## Ejecución

### 1. Iniciar el servidor
```bash
python main.py
```
El servidor estará disponible en [http://localhost:5000](http://localhost:5000).

### 2. Inicializar datos maestros (Seed)
Antes de usar los módulos, debes cargar los tipos de documento y estados iniciales:
*   Visita: [http://localhost:5000/seed](http://localhost:5000/seed)

## Módulos Disponibles

*   **Usuarios**: `GET/POST /usuarios`
*   **Billeteras**: `GET/POST /billeteras`
*   **Comercios**: `GET/POST /comercios`
*   **Transacciones**: `GET/POST /transacciones`

## Estructura del Proyecto

*   `main.py`: Punto de entrada y configuración global.
*   `usuarios.py`, `billeteras.py`, etc.: Lógica de cada módulo (Blueprints).
*   `extensions.py`: Inicialización de base de datos (SQLAlchemy).
*   `config.py`: Manejo de configuraciones y variables de entorno.
