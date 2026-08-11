FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

# Настройка рабочего каталога внутри контейнера
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-s", "-v", "--alluredir=reports"]