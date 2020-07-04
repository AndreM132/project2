FROM python:latest

RUN mkdir ./app3

COPY . /app3

WORKDIR /app3

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
