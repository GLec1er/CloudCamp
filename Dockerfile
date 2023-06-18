# Используем образ Python в качестве базового образа
FROM python:3.9

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходных файлов в контейнер
COPY . .

# Запуск тестов
CMD ["python", "test_run.py"]
