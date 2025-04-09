FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "scrape.py"]


