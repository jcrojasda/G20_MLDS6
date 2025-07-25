# Usar una imagen base de Python 3.8
FROM python:3.8-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto 8000 (puerto por defecto de FastAPI)
EXPOSE 8001

# Comando para iniciar la aplicación FastAPI usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
