FROM mcr.microsoft.com/playwright/python:v1.42.0

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "scrape.py"]

