FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/karimmdjdb/link-shortener"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]