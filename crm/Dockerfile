FROM python:3.8.5-slim

RUN apt-get update 

# Set some env varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app

EXPOSE 8000
