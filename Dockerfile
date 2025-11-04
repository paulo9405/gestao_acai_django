FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema necessárias para Pillow e ReportLab
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    tcl8.6-dev tk8.6-dev \
    python3-tk \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "gestao_acai.wsgi:application", "--bind", "0.0.0.0:8080"]

