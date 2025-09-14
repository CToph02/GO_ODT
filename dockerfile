FROM python:3.13.7-alpine

RUN apk add --no-cache mariadb-dev pkgconfig build-base

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/ordenes_trabajo