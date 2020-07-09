FROM python:latest

RUN mkdir ./app1

COPY . /app1

WORKDIR /app1

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
