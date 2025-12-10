# Dockerfile
FROM --platform=linux/arm64 python:3.12-slim

# Variabili d'ambiente per Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Installa dipendenze di sistema
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Aggiorna pip
RUN pip install --upgrade pip

# Copia requirements (se li hai)
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["bash"]