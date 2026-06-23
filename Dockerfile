# Usa una imagen base oficial de Python ligera
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instala las dependencias sin guardar la caché para reducir el tamaño de la imagen
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Expone el puerto 5000 que utilizará Gunicorn
EXPOSE 5000

# Comando para ejecutar la aplicación usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
