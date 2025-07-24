# Usar una imagen base de Python 3.8
FROM python:3.8-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo pyproject.toml al contenedor
COPY pyproject.toml ./

# Instalar las dependencias del proyecto
RUN pip install --upgrade pip && \
    pip install .[dev]  # Instala dependencias desde el archivo pyproject.toml

# Copiar el código y otros archivos necesarios
COPY . .

# Exponer el puerto (si es necesario, dependiendo de tu aplicación)
# EXPOSE 8000

# Definir el comando para ejecutar el proyecto (ajustar según sea necesario)
CMD ["python", "codigo/mi_script.py"]
