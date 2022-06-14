FROM python:3.8.5-slim

# Set some env varible
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get update

# Set work directory
WORKDIR /app
RUN mkdir -p /vol/web/static

RUN chmod -R 755 /vol/web
RUN chmod -R 755 /app
# Install dependencies

COPY requirements.txt /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app

EXPOSE 8000
