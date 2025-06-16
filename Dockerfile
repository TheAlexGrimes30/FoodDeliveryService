FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/food_delivery

ENV DB_NAME postgres
ENV DB_USER postgres
ENV DB_PASSWORD postgres
ENV DB_HOST postgres
ENV DB_PORT 5432