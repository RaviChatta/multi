FROM python:3.12-slim-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    jq \
    libavif-dev \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    poppler-utils \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel
RUN python -m pip install --upgrade pip setuptools wheel

# Set work directory
WORKDIR /app

# Copy your application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your setup script for bots
RUN bash run.sh

# Start your services
CMD flask run -h 0.0.0.0 -p 10000 & python3 ping_server.py & python3 worker.py
