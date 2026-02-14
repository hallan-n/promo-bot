FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium
RUN playwright install-deps

COPY . .

CMD ["python", "app/main.py"]