# Proyecto de Práctica de IA con Hugging Face

Este proyecto aplica prácticas de inteligencia artificial utilizando la biblioteca Hugging Face en un entorno de desarrollo en Python. Las tareas principales implementadas son:

1. **Análisis de sentimientos**: Evaluar el tono emocional de un texto.
2. **Respuesta a preguntas sencillas**: Proveer respuestas a preguntas formuladas en lenguaje natural.
3. **Intercambio entre modelos**: Alternar entre diferentes modelos para tareas específicas.

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto:

### 1. Crear un entorno virtual
Ejecuta el siguiente comando para crear un entorno virtual en Python:

```bash
python -m venv venv
```

### 2. Activar el entorno virtual
Activa el entorno virtual dependiendo de tu sistema operativo:

- En Windows:

```bash
venv\Scripts\activate
```

- En macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias
Asegúrate de estar en el directorio principal del proyecto y ejecuta el siguiente comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el proyecto
Navega a la carpeta del proyecto que deseas probar y ejecuta la aplicación con el siguiente comando:

```bash
streamlit run main.py
```

## Uso

1. **Interfaz gráfica**: Una vez ejecutado, se abrirá una interfaz gráfica en tu navegador web donde podrás interactuar con las diferentes funcionalidades del proyecto.
2. **Seleccionar tarea**: Desde la interfaz, selecciona la tarea que deseas realizar (análisis de sentimientos, respuesta a preguntas, intercambio entre modelos, o generación de imágenes).

## Requisitos previos

- Python 3.8 o superior.
- Conexión a internet para descargar los modelos de Hugging Face.
- Tener instalado `pip` en tu sistema.

## Notas adicionales

- Si encuentras problemas durante la instalación o ejecución, asegúrate de que las dependencias en `requirements.txt` sean compatibles con tu versión de Python.
- Puedes modificar el archivo `main.py` para agregar funcionalidades o personalizar el comportamiento del proyecto.

---

