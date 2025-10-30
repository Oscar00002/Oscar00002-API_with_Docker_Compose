
FROM python:3.12-slim

# Variables de entorno
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Wolf_P.settings

# Directorio de trabajo
WORKDIR /usr/src/app

#Requisitos y dependencias
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código del proyecto
COPY . /usr/src/app/

# Exponer el puerto de Django
EXPOSE 8000

# Comando por defecto para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]