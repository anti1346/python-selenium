FROM python:3.13-slim

WORKDIR /app

RUN pip install selenium

COPY crawl.py .

CMD ["python", "crawl.py"]