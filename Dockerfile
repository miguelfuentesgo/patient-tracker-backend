FROM python:3.8-slim

# Instalar netcat para esperar la base de datos
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
