FROM python:3.9-slim

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY application /app/application
COPY conf /app/conf
COPY etc app/etc
COPY metabase-plugins /app/metabase-plugins
COPY .env /app/.env
COPY main.py /app

CMD ["tail", "-f", "/dev/null"]
