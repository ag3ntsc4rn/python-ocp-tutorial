FROM python:3.11.2-slim

WORKDIR /app
COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python", "./main.py"]