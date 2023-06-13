FROM python:3.11-slim

RUN pip install poetry

COPY . /app
WORKDIR /app

RUN poetry install

EXPOSE 8000
CMD poetry run uvicorn main:app --host 0.0.0.0 --port 8000