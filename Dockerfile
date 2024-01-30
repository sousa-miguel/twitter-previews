FROM python:3.10.10-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]