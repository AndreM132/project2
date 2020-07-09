FROM python:latest

RUN mkdir ./app2

COPY . /app2

WORKDIR /app2

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
