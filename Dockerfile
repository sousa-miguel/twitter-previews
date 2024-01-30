FROM python:3.10.10-alpine

ARG DISCORD_TOKEN
ENV DISCORD_TOKEN=$DISCORD_TOKEN

LABEL   org.opencontainers.image.authors="Miguel Sousa" \
        org.opencontainers.image.title="twitter-previews" \
        org.opencontainers.image.version="1.0.0"

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]